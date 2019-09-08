BASE_SETTINGS = {
    'app': {
        'components': [
            'unv.web',
            'app.components.example',
        ]
    },
    'web': {
        'redis': {
            'enabled': True
        },
    },
    'deploy': {
        'tasks': [
            'unv.deploy.components.vagrant:VagrantTasks',
            'unv.deploy.components.nginx:NginxTasks',
            'unv.deploy.components.iptables:IPtablesTasks',
            'unv.deploy.components.redis:RedisTasks',
            'unv.web.deploy:WebAppTasks'
        ],
    }
}
