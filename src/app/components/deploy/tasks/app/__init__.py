import pkg_resources

from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, as_user, sync_dir, put, mkdir,
    copy_ssh_key_for_user, local
)
from unv.deploy.packages import PythonPackage, VagrantPackage, Package
from unv.deploy.settings import SETTINGS as DEPLOY


APP = DEPLOY['components']['app']
PYTHON = APP.get('python', {})
PYTHON['user'] = APP['user']


class AppPackage(Package):
    DEFAULT = {
        # 'dist': ''
        # TODO: add settings from sync block
        'secure_dir': '',
        'bin': 'unv_web_server'
    }

    def sync(self):
        app_pkg = pkg_resources.require('app')
        version = app_pkg[0].version

        local('python setup.py sdist bdist_wheel')
        put(Path('dist', f'app-{version}.tar.gz'), '')
        python.pip(f'install app-{version}.tar.gz')
        local('rm -rf ./build ./dist')


app = AppPackage(__file__, APP)
python = PythonPackage(__file__, PYTHON)
vagrant = VagrantPackage(__file__, DEPLOY)
as_app = as_user(APP['user'])


@task
@as_app
def setup():
    vagrant.setup()

    create_user(APP['user'])
    copy_ssh_key_for_user(APP['user'], Path(DEPLOY['keys']['public']))

    python.build()

    app.sync()
    app.setup_systemd_units()
    app.start()


@task
def sync():
    app.sync()


@task
def start():
    app.start()


@task
def stop():
    app.stop()


@task
def restart():
    app.restart()
