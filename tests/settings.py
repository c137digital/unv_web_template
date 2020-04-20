from unv.app.settings import ComponentSettings

from app.settings.base import BASE_SETTINGS

# NOTE: add check you don't import nothing with settings inside

SETTINGS = ComponentSettings.create({
    'app': {
        'env': 'test'
    },
    'web': {
        'redis': {
            'enabled': False
        }
    },
    'deploy': {
        'components': {
            'web': {
                'static': {
                    'link': False
                }
            }
        }
    }
}, BASE_SETTINGS)

print(SETTINGS)
