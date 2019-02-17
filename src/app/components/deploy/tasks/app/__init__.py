from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, as_user, sync_dir, put, mkdir,
    copy_ssh_key_for_user
)
from unv.deploy.packages import PythonPackage, VagrantPackage
from unv.deploy.settings import SETTINGS as DEPLOY


APP = DEPLOY['components']['app']

python = PythonPackage(__file__, APP.get('python', {}))
vagrant = VagrantPackage(__file__, DEPLOY)
as_app = as_user('app')


@task
@as_app
def setup():
    vagrant.setup()
    create_user(APP['user'])
    copy_ssh_key_for_user(APP['user'], Path(DEPLOY['keys']['public']))

    python.build()

    sync()
    start()


@task
@as_app
def sync():
    project_dir = Path(__file__).parents[5]

    mkdir('app')
    sync_dir(project_dir / 'src', Path('app', 'src'))
    put(project_dir / 'setup.py', Path('app', 'setup.py'))

    python.pip('install -e app')


@task
@as_app
def start():
    run('echo "Starting"')
