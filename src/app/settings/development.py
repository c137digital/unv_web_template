from unv.utils.collections import update_dict_recur

from .base import BASE_SETTINGS

SETTINGS = update_dict_recur(BASE_SETTINGS, {
    'app': {
        'debug': True
    }
})
