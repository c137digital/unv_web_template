from aiohttp import web

from unv.web.helpers import url_for_static

from .settings import SETTINGS


async def index(request):
    st = url_for_static('example/2.txt')
    test = f'130 {st} {SETTINGS["somevar"]}\n'
    return web.Response(body=test)
