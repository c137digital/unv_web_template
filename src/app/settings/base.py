BASE_SETTINGS = {
    'app': {
        'debug': False,
        'components': [
            'unv.deploy',

            'app.components.example',
            'app.components.deploy',
        ]
    },
    'web': {
        'port': 8000,
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
                'components': ['app', 'iptables', 'nginx']
            }
        },
        'components': {
            'app': {
                'user': 'unv_web_template',
                'instances': 4,
                'python': {
                    'root': '/home/unv_web_template/python',
                },
                'systemd': {
                    'main': 'app.target',
                }
            },
            'nginx': {
                'user': 'nginx',
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
