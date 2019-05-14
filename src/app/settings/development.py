from unv.app.core import create_settings

from .base import BASE_SETTINGS

SETTINGS = create_settings({
    'deploy': {
        'hosts': {
            'vagrant': {
                'public': '10.50.25.10',
                'private': '0.0.0.0',
                'components': ['web', 'nginx', 'iptables']
            }
        },
        'components': {
            'web': {
                'settings': 'app.settings.development',
                'use_https': False,
                'systemd': {
                    'instances': {'count': 2}
                }
            }
        }
    }
}, BASE_SETTINGS)
