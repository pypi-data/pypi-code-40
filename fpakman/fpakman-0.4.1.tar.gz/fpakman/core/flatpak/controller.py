import os
import shutil
from argparse import Namespace
from datetime import datetime
from typing import List, Dict

from fpakman.core import disk
from fpakman.core.controller import ApplicationManager
from fpakman.core.disk import DiskCacheLoader
from fpakman.core.flatpak import flatpak
from fpakman.core.flatpak.model import FlatpakApplication
from fpakman.core.flatpak.worker import FlatpakAsyncDataLoader, FlatpakUpdateLoader
from fpakman.core.model import ApplicationData, ApplicationUpdate
from fpakman.core.system import FpakmanProcess
from fpakman.util.cache import Cache


class FlatpakManager(ApplicationManager):

    def __init__(self, app_args: Namespace, api_cache: Cache, disk_cache: bool, http_session):
        super(FlatpakManager, self).__init__(app_args=app_args)
        self.api_cache = api_cache
        self.http_session = http_session
        self.disk_cache = disk_cache

    def get_app_type(self):
        return FlatpakApplication

    def _map_to_model(self, app_json: dict, installed: bool, disk_loader: DiskCacheLoader) -> FlatpakApplication:

        app = FlatpakApplication(arch=app_json.get('arch'),
                                 branch=app_json.get('branch'),
                                 origin=app_json.get('origin'),
                                 runtime=app_json.get('runtime'),
                                 ref=app_json.get('ref'),
                                 commit=app_json.get('commit'),
                                 base_data=ApplicationData(id=app_json.get('id'),
                                                           name=app_json.get('name'),
                                                           version=app_json.get('version'),
                                                           latest_version=app_json.get('latest_version')))
        app.installed = installed

        api_data = self.api_cache.get(app_json['id'])

        expired_data = api_data and api_data.get('expires_at') and api_data['expires_at'] <= datetime.utcnow()

        if not api_data or expired_data:
            if not app_json['runtime']:
                disk_loader.add(app)  # preloading cached disk data
                FlatpakAsyncDataLoader(app=app, api_cache=self.api_cache, manager=self, http_session=self.http_session).start()

        else:
            app.fill_cached_data(api_data)

        return app

    def search(self, word: str, disk_loader: DiskCacheLoader) -> Dict[str, List[FlatpakApplication]]:

        res = {'installed': [], 'new': []}
        apps_found = flatpak.search(word)

        if apps_found:
            already_read = set()
            installed_apps = self.read_installed(disk_loader=disk_loader)

            if installed_apps:
                for app_found in apps_found:
                    for installed_app in installed_apps:
                        if app_found['id'] == installed_app.base_data.id:
                            res['installed'].append(installed_app)
                            already_read.add(app_found['id'])

            if len(apps_found) > len(already_read):
                for app_found in apps_found:
                    if app_found['id'] not in already_read:
                        res['new'].append(self._map_to_model(app_found, False, disk_loader))

        return res

    def read_installed(self, disk_loader: DiskCacheLoader) -> List[FlatpakApplication]:
        installed = flatpak.list_installed()
        models = []

        if installed:

            available_updates = flatpak.list_updates_as_str()

            for app_json in installed:
                model = self._map_to_model(app_json=app_json, installed=True, disk_loader=disk_loader)
                model.update = app_json['id'] in available_updates
                models.append(model)

        return models

    def can_downgrade(self):
        return True

    def downgrade_app(self, app: FlatpakApplication, root_password: str) -> FpakmanProcess:

        commits = flatpak.get_app_commits(app.ref, app.origin)

        commit_idx = commits.index(app.commit)

        # downgrade is not possible if the app current commit in the first one:
        if commit_idx == len(commits) - 1:
            return None

        return FpakmanProcess(subproc=flatpak.downgrade_and_stream(app.ref, commits[commit_idx + 1], root_password),
                              success_phrase='Updates complete.')

    def clean_cache_for(self, app: FlatpakApplication):
        self.api_cache.delete(app.base_data.id)

        if app.supports_disk_cache() and os.path.exists(app.get_disk_cache_path()):
            shutil.rmtree(app.get_disk_cache_path())

    def update_and_stream(self, app: FlatpakApplication) -> FpakmanProcess:
        return FpakmanProcess(subproc=flatpak.update_and_stream(app.ref))

    def uninstall_and_stream(self, app: FlatpakApplication, root_password: str = None) -> FpakmanProcess:
        return FpakmanProcess(subproc=flatpak.uninstall_and_stream(app.ref))

    def get_info(self, app: FlatpakApplication) -> dict:
        app_info = flatpak.get_app_info_fields(app.base_data.id, app.branch)
        app_info['name'] = app.base_data.name
        app_info['type'] = 'runtime' if app.runtime else 'app'
        app_info['description'] = app.base_data.description
        return app_info

    def get_history(self, app: FlatpakApplication) -> List[dict]:
        return flatpak.get_app_commits_data(app.ref, app.origin)

    def install_and_stream(self, app: FlatpakApplication, root_password: str) -> FpakmanProcess:
        return FpakmanProcess(subproc=flatpak.install_and_stream(app.base_data.id, app.origin))

    def is_enabled(self):
        return flatpak.is_installed()

    def cache_to_disk(self, app: FlatpakApplication, icon_bytes: bytes, only_icon: bool):
        if self.disk_cache and app.supports_disk_cache():
            disk.save(app, icon_bytes, only_icon)

    def requires_root(self, action: str, app: FlatpakApplication):
        return action == 'downgrade'

    def refresh(self, app: FlatpakApplication, root_password: str) -> FpakmanProcess:
        raise Exception("'refresh' is not supported for {}".format(app.__class__.__name__))

    def prepare(self):
        flatpak.set_default_remotes()

    def list_updates(self) -> List[ApplicationUpdate]:
        updates = []
        installed = flatpak.list_installed(extra_fields=False)

        if installed:
            available_updates = flatpak.list_updates_as_str()

            if available_updates:
                loaders = None

                for app_json in installed:
                    if app_json['id'] in available_updates:
                        loader = FlatpakUpdateLoader(app=app_json, http_session=self.http_session)
                        loader.start()

                        if loaders is None:
                            loaders = []

                        loaders.append(loader)

                if loaders:
                    for loader in loaders:
                        loader.join()
                        app = loader.app
                        updates.append(ApplicationUpdate(app_id='{}:{}'.format(app['id'], app['branch']),
                                                         app_type='flatpak',
                                                         version=app.get('version')))

        return updates
