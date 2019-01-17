BASE_COMPONENTS = {
    'app': {
        'sync': {
            'dirs': ['dist'],
            'exclude': [],
        },
        'build': [
            'pip install *.tar.gz'
        ],
        'systemd': {
            'target': 'app.target'
        }
    }
}
