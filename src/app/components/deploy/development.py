from unv.utils.collections import update_dict_recur

from .base import BASE_COMPONENTS

HOSTS = {
    'vagrant': {
        'public': '10.50.25.10',
        'private': '0.0.0.0',
        'ssh': 22,
        'components': ['app']
    }
}

COMPONENTS = update_dict_recur(BASE_COMPONENTS, {})
