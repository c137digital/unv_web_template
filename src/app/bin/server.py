from unv.web.core import create_app, run_app


def run():
    app = create_app()
    run_app(app)


if __name__ == '__main__':
    run()
