BASE_SETTINGS = {
    'app': {
        'debug': False,
        'components': [
            'unv.deploy',

            'app.components.example',
            'app.components.deploy',
        ]
    },
    'deploy': {
        'keys': {
            'public': '~/.ssh/id_rsa.pub',
            'private': '~/.ssh/id_rsa'
        },
        'hosts': {
            'vagrant': {
                'public': '10.50.25.10',
                'private': '0.0.0.0',
                'components': ['app', 'iptables']
            }
        },
        'components': {
            'app': {
                'kernel': {},
                'user': 'unv_web_template',
                'systemd': {
                    'main': 'app.target',
                }
            },
            'nginx': {
                'systemd': {},
            },
            'iptables': {
                'user': 'root',
                'systemd': {
                    ''
                }
            }
        }
    }
}
