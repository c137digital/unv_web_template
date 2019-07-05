from unv.app.settings import ComponentSettings

from .base import BASE_SETTINGS

# NOTE: add check you don't import nothing with settings inside

SETTINGS = ComponentSettings.create({
    'app': {
        'env': 'dev'
    },
    'web': {
        'redis': {
            'enabled': True
        },
    },
    'deploy': {
        'tasks': [
            'unv.deploy.components.vagrant:VagrantTasks',
            'unv.deploy.components.nginx:NginxTasks',
            'unv.deploy.components.iptables:IPtablesTasks',
            'unv.deploy.components.redis:RedisTasks',
            'unv.web.deploy:WebAppTasks'
        ],
        'hosts': {
            'vagrant': {
                'public_ip': '10.50.25.10',
                'components': ['iptables', 'nginx', 'web', 'redis']
            }
        },
        'components': {
            'web': {
                'settings': 'app.settings.dev',
                'use_https': False,
                'systemd': {
                    'instances': {'percent': 100}
                },
            },
            'nginx': {
                'geoip2': True
            }
        }
    }
}, BASE_SETTINGS)
