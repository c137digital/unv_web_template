from unv.app.core import ComponentSettings

from .base import BASE_SETTINGS

SETTINGS = ComponentSettings.create({
    'deploy': {
        'hosts': {
            'vagrant': {
                'public_ip': '10.50.25.10',
                'private_ip': '10.50.25.10',
                'port': 22,
                'components': ['iptables', 'nginx', 'app']
            }
        },
        'components': {
            'app': {
                'settings': 'app.settings.development',
                'use_https': False,
                'systemd': {
                    'instances': {'cpu_count_percent': 100}
                }
            }
        }
    }
}, BASE_SETTINGS)
