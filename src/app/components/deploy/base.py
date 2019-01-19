BASE_COMPONENTS = {
    'app': {
        'user': 'vagrant',
        'sync': {
            'dirs': ['dist'],
            'exclude': [],
        },
        'setup': [
            'pip install *.tar.gz'
        ],
        'systemd': {
            'target': 'app.target'
        }
    }
}
