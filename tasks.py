#!./venv/bin/python

import sys

from unv.deploy.tasks import DeployTasksManager
from unv.deploy.components.app import AppComponentTasks
from unv.deploy.components.nginx import NginxComponentTasks


if __name__ == '__main__':
    manager = DeployTasksManager()
    manager.register(AppComponentTasks)
    manager.register(NginxComponentTasks)
    manager.run(' '.join(sys.argv[1:]))
