from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, copy_ssh_key_for_user, as_user
)
from unv.deploy.packages import python
from unv.deploy.settings import SETTINGS


def setup_vagrant():
    run('sudo passwd root')
    copy_ssh_key_for_user('root', Path(SETTINGS['keys']['public']))


@task
def setup():
    user = SETTINGS['components']['app']['user']
    as_user('vagrant', setup_vagrant)()
    create_user(user)
    copy_ssh_key_for_user(user, Path(SETTINGS['keys']['public']))
    python.build(Path('/home/', user, 'python'))


# @task
# def sync():
    # sync_dir()


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
