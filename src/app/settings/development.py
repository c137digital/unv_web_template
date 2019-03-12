from unv.utils.collections import update_dict_recur
from unv.app.core import create_settings

from .base import BASE_SETTINGS

SETTINGS = create_settings(update_dict_recur(BASE_SETTINGS, {
    'app': {
        'debug': True,
    },
    'example': {
        'env': 'development'
    }
}))
