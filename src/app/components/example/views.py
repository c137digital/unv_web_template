from aiohttp import web

from unv.web.helpers import url_for_static

# from .settings import SETTINGS


async def index(request):
    st = url_for_static('test/1.txt')
    return web.Response(body=st)
