import sys

from unv.web.core import create_app, run_app


def run():
    instance, host, port = sys.argv[1], sys.argv[2], sys.argv[3]
    port = int(port) + int(instance)
    app = create_app()
    run_app(app, host, port)
