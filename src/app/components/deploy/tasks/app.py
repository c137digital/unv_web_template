from fabric.api import task, run


@task
def setup():
    # TODO: build python using helpers
    run('echo "Setup"')


@task
def sync():
    # TODO: sync source code and reinstall package
    run('echo "Syncing"')


@task
def start():
    # TODO: start systemd daemon or other process
    run('echo "Starting"')
