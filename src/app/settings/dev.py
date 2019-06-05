from unv.app.settings import ComponentSettings

from .base import BASE_SETTINGS

# NOTE: add check you don't import nothing with settings inside

SETTINGS = ComponentSettings.create({
    'deploy': {
        'tasks': [
            'unv.deploy.components.vagrant:VagrantTasks',
            'unv.deploy.components.app:AppComponentTasks'
        ],
        'hosts': {
            'vagrant': {
                'public_ip': '10.50.25.10',
                'components': ['iptables', 'nginx', 'app']
            }
        },
        'components': {
            'app': {
                'settings': 'app.settings.development',
                'use_https': False,
                'systemd': {
                    'instances': {'percent': 100}
                }
            }
        }
    }
}, BASE_SETTINGS)
