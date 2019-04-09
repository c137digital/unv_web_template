from unv.app.core import create_component_settings

SCHEMA = {
    "env": {
        "type": "string",
        "required": False
    }
}

DEFAULTS = {
    'env': 'undefined',
}

SETTINGS = create_component_settings('example', DEFAULTS, SCHEMA)
