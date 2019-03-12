from .settings import SETTINGS

from aiohttp import web


async def index(request):
    return web.Response(body=SETTINGS['env'])
