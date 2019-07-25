# -*- coding: utf-8 -*-

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import json
import os
import re
import requests
import shutil

import pytest

import nbformat

from ..utils import pushd
from .utils import WEB_TEST_TIMEOUT, TEST_TOKEN, call


pjoin = os.path.join

_re_config = re.compile(
    """<script id='nbdime-config-data' type="application/json">(.*?)</script>"""
)

auth_header = {
    'Authorization': 'token %s' % TEST_TOKEN
}


@pytest.mark.timeout(timeout=WEB_TEST_TIMEOUT)
def test_isgit(git_repo2, server_extension_app):
    url = 'http://127.0.0.1:%i/nbdime/api/isgit' % server_extension_app['port']
    r = requests.post(
        url, headers=auth_header,
        data=json.dumps({
            'path': git_repo2,
        }))
    r.raise_for_status()
    assert r.json() == {'is_git': True}


@pytest.mark.timeout(timeout=WEB_TEST_TIMEOUT)
def test_isgit_nonrepo(git_repo2, server_extension_app):
    url = 'http://127.0.0.1:%i/nbdime/api/isgit' % server_extension_app['port']
    r = requests.post(
        url, headers=auth_header,
        data=json.dumps({
            'path': server_extension_app['path'],
        }))
    r.raise_for_status()
    assert r.json() == {'is_git': False}


@pytest.mark.timeout(timeout=WEB_TEST_TIMEOUT)
def test_difftool(git_repo2, server_extension_app):
    url = 'http://127.0.0.1:%i/nbdime/difftool' % server_extension_app['port']
    r = requests.get(url, headers=auth_header)
    r.raise_for_status()


@pytest.mark.timeout(timeout=WEB_TEST_TIMEOUT)
def test_git_difftool(git_repo2, server_extension_app):
    url = 'http://127.0.0.1:%i/nbdime/git-difftool' % server_extension_app['port']
    r = requests.get(
        url, headers=auth_header)
    r.raise_for_status()
    assert r.text.startswith('<!DOCTYPE html')
    # Extract config data
    match = _re_config.search(r.text)
    data = json.loads(match.group(1))
    assert data == {
        "base": "git:",
        "baseUrl": "/nbdime",
        "closable": False,
        "remote": "",
        "savable": False,
        "hideUnchanged": True,
        "mathjaxConfig": "TeX-AMS-MML_HTMLorMML-full,Safe",
        "mathjaxUrl": "/static/components/MathJax/MathJax.js",
    }


@pytest.mark.timeout(timeout=WEB_TEST_TIMEOUT)
def test_diff_api(git_repo2, server_extension_app):
    local_path = os.path.relpath(git_repo2, server_extension_app['path'])
    url = 'http://127.0.0.1:%i/nbdime/api/diff' % server_extension_app['port']
    r = requests.post(
        url, headers=auth_header,
        data=json.dumps({
            'base': 'git:' + pjoin(local_path, 'diff.ipynb'),
        }))
    r.raise_for_status()
    data = r.json()
    nbformat.validate(data['base'])
    assert data['diff']
    assert len(data.keys()) == 2


@pytest.mark.timeout(timeout=WEB_TEST_TIMEOUT)
def test_diff_api_checkpoint(tmpdir, filespath, server_extension_app):

    local_path = os.path.relpath(str(tmpdir), server_extension_app['path'])

    # Create base
    src = filespath
    shutil.copy(pjoin(src, 'src-and-output--1.ipynb'), pjoin(str(tmpdir), 'diff.ipynb'))

    url_path = pjoin(local_path, 'diff.ipynb')
    if os.sep == '\\':
        url_path = url_path.replace('\\', '/')


    # Create checkpoint
    url = 'http://127.0.0.1:%i/api/contents/%s/checkpoints' % (
        server_extension_app['port'],
        url_path,
    )
    r = requests.post(url, headers=auth_header)
    r.raise_for_status()

    # Overwrite:
    shutil.copy(pjoin(src, 'src-and-output--2.ipynb'), pjoin(str(tmpdir), 'diff.ipynb'))


    url = 'http://127.0.0.1:%i/nbdime/api/diff' % server_extension_app['port']
    r = requests.post(
        url, headers=auth_header,
        data=json.dumps({
            'base': 'checkpoint:' + url_path,
        }))
    r.raise_for_status()
    data = r.json()
    nbformat.validate(data['base'])
    assert data['diff']
    assert len(data.keys()) == 2


@pytest.mark.timeout(timeout=WEB_TEST_TIMEOUT)
def test_diff_api_symlink(git_repo2, server_extension_app, needs_symlink):
    root = server_extension_app['path']
    subdir = pjoin(root, 'has space', 'subdir')
    os.makedirs(subdir)
    symlink = pjoin(subdir, 'link')
    with pushd(subdir):
        call(['git', 'init'])
        with open('f', 'w') as f:
            f.write('stuff')
        call(['git', 'add', 'f'])
        call(['git', 'commit', '-m', 'initial commit'])
    os.symlink(git_repo2, symlink)

    local_path = os.path.relpath(symlink, server_extension_app['path'])
    url = 'http://127.0.0.1:%i/nbdime/api/diff' % server_extension_app['port']
    r = requests.post(
        url, headers=auth_header,
        data=json.dumps({
            'base': 'git:' + pjoin(local_path, 'diff.ipynb'),
        }))
    r.raise_for_status()
    data = r.json()
    nbformat.validate(data['base'])
    assert data['diff']
    assert len(data.keys()) == 2


@pytest.mark.timeout(timeout=WEB_TEST_TIMEOUT)
def test_fails_without_token(git_repo2, server_extension_app):
    url = 'http://127.0.0.1:%i/nbdime/api/isgit' % server_extension_app['port']
    r = requests.post(
        url,
        data=json.dumps({
            'path': git_repo2,
        }))
    with pytest.raises(requests.HTTPError):
        r.raise_for_status()


@pytest.mark.timeout(timeout=WEB_TEST_TIMEOUT)
def test_fails_with_wrong_token(git_repo2, server_extension_app):
    url = 'http://127.0.0.1:%i/nbdime/api/isgit' % server_extension_app['port']
    r = requests.post(
        url,
        data=json.dumps({
            'path': git_repo2,
        }),
        headers={
            'Authorization': 'token wrong-token-here'
        })
    with pytest.raises(requests.HTTPError):
        r.raise_for_status()
