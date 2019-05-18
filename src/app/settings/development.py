from unv.app.core import create_settings

from .base import BASE_SETTINGS

SETTINGS = create_settings({
    'deploy': {
        'hosts': {
            'vagrant': {
                'public_ip': '10.50.25.11',
                'private_ip': '10.50.25.11',
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
