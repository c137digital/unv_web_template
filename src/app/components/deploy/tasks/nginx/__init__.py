from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, copy_ssh_key_for_user, as_user, sync_dir, local,
    put, upload_template, as_root, mkdir, filter_hosts
)
from unv.deploy.packages import NginxPackage

from app.settings import SETTINGS


DEPLOY = SETTINGS['deploy']
NGINX = DEPLOY['components']['nginx']

nginx = NginxPackage(__file__, NGINX)


@task
@as_user(NGINX['user'])
def setup():
    create_user(NGINX['user'])
    copy_ssh_key_for_user(NGINX['user'], Path(DEPLOY['keys']['public']))

    nginx.build()

    sync()
    start()


@task
@as_user(NGINX['user'])
def sync():
    # project_dir = Path(__file__).parents[5]
    # mkdir('app')
    nginx.sync()
    # upload_template(
    #     'configs' / 'app.j2.service', '/etc/systemd/system/{app_name}/')


@task
@as_user(NGINX['user'])
def start():
    nginx.start()


@task
@as_user(NGINX['user'])
def status():
    nginx.status()


@task
def restart():
    nginx.restart()
