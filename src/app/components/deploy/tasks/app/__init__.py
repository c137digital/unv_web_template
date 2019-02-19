from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, as_user, sync_dir, put, mkdir,
    copy_ssh_key_for_user
)
from unv.deploy.packages import PythonPackage, VagrantPackage, Package
from unv.deploy.settings import SETTINGS as DEPLOY


APP = DEPLOY['components']['app']


class AppPackage(Package):
    DEFAULT = {
        # 'dist': ''
        # TODO: add settings from sync block
        'secure_dir': '',
        'bin': '',
        'logs_dir': '',
    }

    def setup(self):
        pass

    # def build(self):
    #     local('python setup.py sdist bdist_wheel')
    #     # TODO: move to commands from .vscode / tasks.json

    def sync(self):
        # sync data
        # project_dir = Path(__file__).parents[5]
        # local('build')
        # mkdir('secure')
        # python.pip('install app.tar.gz')
        # run('rm app.tar.gz')
        pass


app = AppPackage(__file__, APP)
python = PythonPackage(__file__, APP.get('python', {}))
vagrant = VagrantPackage(__file__, DEPLOY)
as_app = as_user('app')


@task
@as_app
def setup():
    vagrant.setup()

    app.setup()
    app.setup_systemd_units()

    create_user(APP['user'])
    copy_ssh_key_for_user(APP['user'], Path(DEPLOY['keys']['public']))

    python.build()

    sync()
    start()


@task
@as_app
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
