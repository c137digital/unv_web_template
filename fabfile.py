import os
import sys

from fabric.api import local

from unv.app.fabric import load_components_tasks, local_task

load_components_tasks()

DEPLOY_SETTINGS_SHORTCUTS = {
    'dev': 'app.components.deploy.development',
    'prod': 'secure.deploy.production'
}


@local_task
def run():
    local('vagrant up')
    # check if we have initial setup
    # local('dep dev setup')
    local('dev app.sync app.start')


def process_deployment_commands(args):
    hosts = ','.join([
        part.lstrip('host:') for part in args if part.startswith('host:')])
    settings, component, *actions = args
    settings = DEPLOY_SETTINGS_SHORTCUTS.get(settings, settings)
    actions = ' '.join([f'deploy.{component}.{action}' for action in actions])
    os.system(
        f"fab deploy.load:{settings},{component} "
        f"deploy.host:{hosts} {actions}"
    )


if __name__ == '__main__':
    if sys.argv[1] in DEPLOY_SETTINGS_SHORTCUTS:
        process_deployment_commands(sys.argv[1:])
