from . import views


def setup(app):
    app.router.add_get('/', views.index, name='index')
