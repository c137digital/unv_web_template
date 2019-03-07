import pkg_resources

from pathlib import Path

from unv.deploy.helpers import (
    task, create_user, as_user, put, copy_ssh_key_for_user, local
)
from unv.deploy.packages import PythonPackage, VagrantPackage, Package
from unv.deploy.settings import SETTINGS as DEPLOY


APP = DEPLOY['components']['app']


class AppPackage(Package):
    DEFAULT = {
        'secure_dir': '',
        'settings': '',
        'bin': 'unv_web_server'
    }

    @property
    def python(self):
        settings = self.settings.get('python', {})
        settings['user'] = self.user
        return PythonPackage(__file__, settings)

    @property
    def bin(self):
        return self.python.bin(self.settings['bin'], command_only=True)

    def sync(self):
        app_pkg = pkg_resources.require('app')
        version = app_pkg[0].version

        local('python setup.py sdist bdist_wheel')
        put(Path('dist', f'app-{version}.tar.gz'), '')
        local('rm -rf ./build ./dist')
        self.python.pip(f'install app-{version}.tar.gz')


vagrant = VagrantPackage(__file__, DEPLOY)
app = AppPackage(__file__, APP)
as_app = as_user(APP['user'])


@task
@as_app
def setup():
    vagrant.setup()

    create_user(APP['user'])
    copy_ssh_key_for_user(APP['user'], Path(DEPLOY['keys']['public']))

    app.python.build()
    app.sync()
    app.setup_systemd_units()
    app.start()


@task
def sync():
    app.sync()


@task
def start():
    app.start()


@task
def stop():
    app.stop()


@task
def restart():
    app.restart()
