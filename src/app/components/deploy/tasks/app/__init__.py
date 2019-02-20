from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, as_user, sync_dir, put, mkdir,
    copy_ssh_key_for_user, local
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
        put(Path('dist', 'app-0.1.tar.gz'), '')
        python.pip('install app-0.1.tar.gz')

    # def build(self):
    #     local('python setup.py sdist bdist_wheel')
    #     # TODO: move to commands from .vscode / tasks.json

    def build(self):
        # sync data
        project_dir = Path(__file__).parents[5]
        # local('b')
        # mkdir('secure')
        local('python setup.py sdist bdist_wheel')
        # python.pip('install app.tar.gz')
        # run('rm app.tar.gz')


app = AppPackage(__file__, APP)
python = PythonPackage(__file__, APP.get('python', {}))
vagrant = VagrantPackage(__file__, DEPLOY)
as_app = as_user('app')


@task
@as_app
def setup():
    # vagrant.setup()

    create_user(APP['user'])
    copy_ssh_key_for_user(APP['user'], Path(DEPLOY['keys']['public']))

    python.build()

    app.build()
    app.setup()
    app.setup_systemd_units()

    # sync()
    # start()


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
