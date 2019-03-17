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
        'disable_existing_loggers': True,
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
                'filename': '~/logs/session.log',
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
                'components': ['app', 'nginx']
            }
        },
        'components': {
            'app': {
                'bin': 'server',
                'user': 'app',
                'instances': 2,
                'settings_module': 'secure.production',
                'systemd': {
                    'dir': 'systemd',
                    'services': {
                        'server.service': {
                            'name': 'app_{INSTANCE}.service',
                            'boot': True
                        }
                    }
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
                    '../app/nginx.conf': 'app.conf'
                },
                'systemd': {
                    'dir': 'systemd',
                    'services': {
                        'server.service': {
                            'name': 'nginx.service',
                            'boot': True
                        }
                    }
                }
            }
        }
    }
}
