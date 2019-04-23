import pathlib

from unv.app.core import create_settings

from .base import BASE_SETTINGS

APP_USER = 'app'
APP_HOME = str(pathlib.Path('/', 'home', APP_USER))

SETTINGS = create_settings({
    'app': {
        'root': APP_HOME,
    },
    'deploy': {
        'hosts': {
            'vagrant': {
                'public': '10.50.25.10',
                'private': '0.0.0.0',
                'components': ['app', 'nginx']
            }
        },
        'components': {
            'app': {
                'settings': 'app.settings.development',
                'user': APP_USER,
                'use_https': False,
                'systemd': {
                    'services': {
                        'app.service': {
                            'instances': 2
                        }
                    }
                },
            },
            'nginx': {'user': 'nginx'}
        }
    }
}, BASE_SETTINGS)
