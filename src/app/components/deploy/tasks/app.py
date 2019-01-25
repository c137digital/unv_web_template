from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, copy_ssh_key_for_user, as_user, sync_dir, local
)
from unv.deploy.packages import python
from unv.deploy.settings import SETTINGS


APP_SETTINGS = SETTINGS['components']['app']
PYTHON_SETTINGS = SETTINGS['components']['app'].get('python', {})


@as_user('vagrant')
def setup_vagrant():
    local('vagrant destroy -f')
    local('vagrant up')
    local('rm -f ~/.ssh/known_hosts')
    copy_ssh_key_for_user('root', Path(SETTINGS['keys']['public']))


@task
def setup():
    setup_vagrant()
    create_user(APP_SETTINGS['user'])
    copy_ssh_key_for_user(
        APP_SETTINGS['user'],
        Path(SETTINGS['keys']['public'])
    )

    with python.use(PYTHON_SETTINGS):
        python.build()


@task
def sync():
    sync_dir('src', 'app')



# @task
# def start():
    # TODO: start systemd daemon or other process
    # run('echo "Starting"')


# @task
# def stop():
#     pass


# @task
# def restart():
#     pass
