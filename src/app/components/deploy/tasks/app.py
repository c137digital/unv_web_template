from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, copy_ssh_key_for_user, as_user, sync_dir
)
from unv.deploy.packages import python
from unv.deploy.settings import SETTINGS


@as_user('vagrant')
def setup_vagrant():
    run('sudo passwd root')
    copy_ssh_key_for_user('root', Path(SETTINGS['keys']['public']))


@task
def setup():
    setup_vagrant()
    user = SETTINGS['components']['app']['user']
    create_user(user)
    copy_ssh_key_for_user(user, Path(SETTINGS['keys']['public']))
    python.build(Path('/home/', user, 'python'))


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
