from .api import TvaritAPI
from .resources import (
    Admin,
    Dashboard,
    Datasource,
    Folder,
    Organization,
    Organizations,
    Search,
    User,
    Users,
    Teams,
    Annotations,
    Alerting,
    Snapshot,
)


class Tvarit:
    def __init__(
        self,
        auth,
        host="localhost",
        port=None,
        url_path_prefix="",
        protocol="http",
        verify=True,
    ):
        self.api = TvaritAPI(
            auth,
            host=host,
            port=port,
            url_path_prefix=url_path_prefix,
            protocol=protocol,
            verify=verify,
        )
        self.admin = Admin(self.api)
        self.dashboard = Dashboard(self.api)
        self.datasource = Datasource(self.api)
        self.folder = Folder(self.api)
        self.organization = Organization(self.api)
        self.organizations = Organizations(self.api)
        self.search = Search(self.api)
        self.user = User(self.api)
        self.users = Users(self.api)
        self.teams = Teams(self.api)
        self.annotations = Annotations(self.api)
        self.alerting = Alerting(self.api)
        self.snapshot = Snapshot(self.api)
