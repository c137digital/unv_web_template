import sys
import code
import atexit
import asyncio

from aiohttp import web

from unv.web.core import create_app


def run():
    app = create_app()
    runner = web.AppRunner(app)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(runner.setup())

    def cleanup_atexit():
        loop.run_until_complete(runner.cleanup())
        loop.close()

    atexit.register(cleanup_atexit)
    code.interact(local={
        'app': app,
        'loop': loop,
        'run': loop.run_until_complete,
        'exit': sys.exit
    })
