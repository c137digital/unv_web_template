from pathlib import Path

from unv.deploy.helpers import (
    task, run, create_user, copy_ssh_key_for_user, as_user, sync_dir, local,
    put, upload_template, as_root, mkdir
)
from unv.deploy.packages import python
from unv.deploy.settings import SETTINGS


APP_SETTINGS = SETTINGS['components']['app']
PYTHON_SETTINGS = SETTINGS['components']['app'].get('python', {})


@as_user('vagrant')
def setup_vagrant():
    local('vagrant destroy -f')
    local('vagrant up')

    # verify server so no timeout on next connection
    local('vagrant ssh -c "sleep 0.1"')

    copy_ssh_key_for_user('root', Path(SETTINGS['keys']['public']))


@task
@as_user(APP_SETTINGS['user'])
def setup():
    setup_vagrant()
    create_user(APP_SETTINGS['user'])
    copy_ssh_key_for_user(
        APP_SETTINGS['user'],
        Path(SETTINGS['keys']['public'])
    )

    with python.use(PYTHON_SETTINGS):
        python.build()

    sync()
    start()


@task
@as_root
def sync_configs():
    # upload_template
    # configs / app.service
    # configs / app.target -> multiple services
    # configs / nginx as master
    upload_template(
        'configs' / 'app.j2.target', '/etc/systemd/system/unv_web_template/')
    upload_template(
        'configs' / 'app.j2.service', '/etc/systemd/system/unv_web_template/')


@task
@as_user(APP_SETTINGS['user'])
def sync():
    project_dir = Path(__file__).parents[5]

    mkdir('app')
    sync_dir(project_dir / 'src', Path('app', 'src'))
    put(project_dir / 'setup.py', Path('app', 'setup.py'))

    with python.use(PYTHON_SETTINGS):
        python.pip('install -e app')


@task
@as_user(APP_SETTINGS['user'])
def start():
    run('echo "Starting"')


# @task
# def stop():
#     pass


# @task
# def restart():
#     pass


# def get_upstream_servers():
#     for _, host in filter_hosts('app'):
#         ssh_host = '{}:{}'.format(host['public'], host['ssh'])
#         instances = SETTINGS['web'].get('instances', 1)
#         if callable(instances):
#             instances = execute_on_hosts(
#                 hosts=[ssh_host],
#                 task=instances,
#                 user=ENV.COMPONENTS['app']['user']
#             )
#         else:
#             instances = {ssh_host: instances}
#         for instance in range(instances[ssh_host]):
#             yield '{}:{}'.format(
#                 host['private'], SETTINGS['web']['port'].format(instance)
#             )
