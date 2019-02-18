from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, as_user, sync_dir, put, mkdir,
    copy_ssh_key_for_user
)
from unv.deploy.packages import PythonPackage, VagrantPackage, Package
from unv.deploy.settings import SETTINGS as DEPLOY


APP = DEPLOY['components']['app']


class AppPackage(Package):
    @property
    def bin(self):
        pass

    @property
    def secure_dir(self):
        pass

    @property
    def logs_dir(self):
        pass

    def setup(self):
        pass

    def sync(self):
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

    # project_dir = Path(__file__).parents[5]

    # mkdir('app')
    # sync_dir(project_dir / 'src', Path('app', 'src'))
    # put(project_dir / 'setup.py', Path('app', 'setup.py'))

    # python.pip('install -e app')


@task
def start():
    app.start()


@task
def stop():
    app.stop()


@task
def restart():
    app.restart()
