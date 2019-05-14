#!./venv/bin/python

import sys

from unv.deploy.tasks import DeployTasksManager
from unv.deploy.components.iptables import IPtablesDeployTasks
from unv.deploy.components.nginx import NginxComponentTasks
from unv.deploy.components.vagrant import VagrantTasks
from unv.web.deploy import WebAppComponentTasks


def create_manager():
    manager = DeployTasksManager()
    manager.register(WebAppComponentTasks)
    manager.register(NginxComponentTasks)
    manager.register(IPtablesDeployTasks)
    manager.register(VagrantTasks)
    return manager


if __name__ == '__main__':
    manager = create_manager()
    manager.run(' '.join(sys.argv[1:]))
