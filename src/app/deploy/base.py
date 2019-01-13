BASE_COMPONENTS = {
    'app': {
        'sync': {
            'dirs': ['dist']
        },
        'build': [
            'pip install *.tar.gz'
        ],
        'systemd': {
            'target': 'app.target'
        }
    }
}
