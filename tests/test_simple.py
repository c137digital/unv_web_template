import pytest

from aiohttp import web

from unv.app.base import Application
from unv.web.deploy import SETTINGS as DEPLOY_SETTINGS


@pytest.fixture
async def client(aiohttp_client):
    app = Application()
    web_app = app[web.Application]
    return await aiohttp_client(web_app)


async def test_simple_web_app(client):
    resp = await client.get('/')
    assert resp.status == 200
