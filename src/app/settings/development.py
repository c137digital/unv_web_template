import pathlib

from unv.utils.collections import update_dict_recur
from unv.app.core import create_settings

from .base import BASE_SETTINGS

APP_USER = 'app'
APP_HOME = pathlib.Path('/', 'home', APP_USER)

SETTINGS = create_settings(update_dict_recur(BASE_SETTINGS, {
    'app': {
        'root': APP_HOME,
        'debug': True,
    },
    'example': {
        'env': 'development'
    },
    'deploy': {
        'components': {
            'app': {
                'user': APP_USER,
                'settings_module': 'app.settings.development'
            }
        }
    }
}))
