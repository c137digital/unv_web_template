from unv.web.core import create_app, run_app


def run():
    raise Exception('app was runned!!')
    app = create_app()
    run_app(app)
