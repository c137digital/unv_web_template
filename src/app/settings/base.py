BASE_SETTINGS = {
    'app': {
        'debug': False,
        'components': [
            'unv.deploy',

            'app.components.example',
            'app.components.deploy',
        ]
    },
    'logging': {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(levelname)s - %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['file']
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '', # override?
                'formatter': 'default'
            }
        }
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
                'bin': 'unv_web_template_server',
                'user': 'unv_web_template',
                'instances': 4,
                'settings': 'secure.settings',
                'systemd': {
                    'dir': 'systemd',
                    'services': [
                        {
                            'name': 'unv_web_template_{INSTANCE}.service',
                            'template': 'server.service',
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
