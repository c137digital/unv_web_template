from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, copy_ssh_key_for_user, as_user, sync_dir, local,
    put, mkdir
)
from unv.deploy.packages import PythonPackage
from unv.deploy.settings import SETTINGS as DEPLOY


APP = DEPLOY['components']['app']

python = PythonPackage(__file__, APP.get('python', {}))
as_app = as_user('app')


@as_user('vagrant')
def setup_vagrant():
    local('vagrant destroy -f')
    local('vagrant up')

    # verify server so no timeout on next connection
    local('vagrant ssh -c "sleep 0.1"')

    copy_ssh_key_for_user('root', Path(DEPLOY['keys']['public']))


@task
@as_app
def setup():
    setup_vagrant()

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
