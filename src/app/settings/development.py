import pathlib

from unv.app.core import create_settings

from .base import BASE_SETTINGS

APP_USER = 'app'
APP_HOME = str(pathlib.Path('/', 'home', APP_USER))

SETTINGS = create_settings({
    'app': {
        'root': APP_HOME,
    },
    'example': {
        'env': 'development'
    },
    'deploy': {
        'hosts': {
            'vagrant': {
                'public': '10.50.25.10',
                'private': '0.0.0.0',
                'components': ['app']
            }
        },
        'components': {
            'app': {
                'bin': 'server',
                'settings': 'app.settings.development',
                'user': APP_USER
            }
        }
    }
}, BASE_SETTINGS)
