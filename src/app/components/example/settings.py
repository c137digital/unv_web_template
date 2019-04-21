from unv.app.core import create_component_settings

SCHEMA = {
    "somevar": {
        "type": "string",
        "required": False
    }
}

DEFAULTS = {
    'somevar': 'undefined',
}

SETTINGS = create_component_settings('example', DEFAULTS, SCHEMA)
