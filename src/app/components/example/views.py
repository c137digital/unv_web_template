from aiohttp import web

from unv.web.helpers import url_for_static

# from .settings import SETTINGS


async def index(request):
    st = url_for_static('example/1.txt')
    test = f'123 {st}'
    return web.Response(body=test)
