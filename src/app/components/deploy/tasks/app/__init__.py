from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, copy_ssh_key_for_user, as_user, sync_dir, local,
    put, upload_template, as_root, mkdir, filter_hosts
)
from unv.deploy.packages import PythonPackage
from unv.deploy.settings import SETTINGS as DEPLOY

from app.settings import SETTINGS


APP = DEPLOY['components']['app']

python = PythonPackage(__file__, APP.get('python', {}))


def get_app_instances_hosts():
    for _, host in filter_hosts(DEPLOY['hosts'], 'app'):
        for instance in range(APP['instances']):
            yield '{}:{}'.format(
                host['private'], SETTINGS['web']['port'] + instance
            )


@as_user('vagrant')
def setup_vagrant():
    local('vagrant destroy -f')
    local('vagrant up')

    # verify server so no timeout on next connection
    local('vagrant ssh -c "sleep 0.1"')

    copy_ssh_key_for_user('root', Path(DEPLOY['keys']['public']))


@task
@as_user(APP['user'])
def setup():
    setup_vagrant()

    create_user(APP['user'])
    copy_ssh_key_for_user(APP['user'], Path(DEPLOY['keys']['public']))

    python.build()

    sync()
    start()


@task
@as_user(APP['user'])
def sync():
    project_dir = Path(__file__).parents[5]

    mkdir('app')
    sync_dir(project_dir / 'src', Path('app', 'src'))
    put(project_dir / 'setup.py', Path('app', 'setup.py'))

    python.pip('install -e app')


@task
@as_user(APP['user'])
def start():
    run('echo "Starting"')
