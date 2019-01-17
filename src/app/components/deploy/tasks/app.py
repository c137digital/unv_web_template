from fabric.api import task


@task
def echo():
    print('test')
