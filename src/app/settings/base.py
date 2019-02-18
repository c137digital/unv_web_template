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
                    'root': 'python',
                },
                'systemd': {
                    'dir': 'systemd',
                    'services': [
                        {
                            'name': 'unv_web_template_{INSTANCE}.service',
                            'template': 'instance.service',
                            'boot': True
                        }
                    ]
                }
            },
            'nginx': {
                'user': 'nginx',
                'master': True,
                'dir': 'app',
                'config': {
                    'name': 'nginx.conf',
                    'template': 'server.conf'
                },
                'include': {
                    '../app/nginx.conf': 'unv_web_template.conf'
                },
                'systemd': {
                    'dir': 'systemd',
                    'services': [
                        {
                            'name': 'nginx.service',
                            'template': 'server.service',
                            'boot': True
                        }
                    ]
                },
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
