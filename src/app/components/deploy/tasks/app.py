import pathlib

from unv.deploy.helpers.core import (
    task, run, create_user, copy_ssh_key_for_user
)
from unv.deploy.helpers.packages import build_python

from ..settings import SETTINGS


@task
def setup():
    create_user(SETTINGS['app']['user'])
    copy_ssh_key_for_user(
        SETTINGS['app']['user'], pathlib.Path(SETTINGS['keys']['public']))
    build_python(pathlib.Path(SETTINGS['app']['python']['path']))


@task
def sync():
    # TODO: sync source code and reinstall package
    run('echo "Syncing"')


@task
def start():
    # TODO: start systemd daemon or other process
    run('echo "Starting"')
