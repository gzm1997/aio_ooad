import time
from aiohttp import web
from aiohttp_session import get_session, setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

async def handler(request):
    session = await get_session(request)
    session['last_visit'] = time.time()
    return web.json_response({
        "status": True
    })

def init():
    app = web.Application()
    setup(app,
        EncryptedCookieStorage(b'Thirty  two  length  bytes  key.'))
    app.router.add_route('GET', '/', handler)
    return app

web.run_app(init())