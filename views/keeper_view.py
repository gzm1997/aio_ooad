from aiohttp import web
import pathlib
import sys
import datetime
from aiohttp_session import get_session
# from aiohttp_session.cookie_storage import EncryptedCookieStorage

BASE_DIR = pathlib.Path(__file__).parent.parent
models_path = BASE_DIR / "models"
aiohttp_polls_path = BASE_DIR / "aiohttp_polls"
sys.path.append(str(models_path))
sys.path.append(str(aiohttp_polls_path))

import keeper
import aio_engine

# json format
# {
#     "name": "gzm",
#     "psw": "Gzm20125"
# }

async def login(request):
    engine = await aio_engine.init_engine()
    data = await request.json()
    print("data", data)
    if "name" not in data or "psw" not in data:
        return web.json_response({
            "status": False
        })
    name = data["name"]
    psw = data["psw"]
    verify = await keeper.verify(engine, name = name, psw = psw)
    if verify:
        session = await get_session(request)
        session["ooad"] = name
        session["login"] = psw
        session["time"] = str(datetime.datetime.now())
        return web.json_response({
            "status": True
        })
    return web.json_response({
        "status": False
    })



async def need_cookies_page(request):
    engine = await aio_engine.init_engine()
    session = await get_session(request)
    if "ooad" not in session or "login" not in session or "time" not in session:
        return web.json_response({
            "status": False
        })
    name = session["ooad"]
    psw = session["login"]
    r = await keeper.verify(engine, name = name, psw = psw)
    if r:
        return web.json_response({
            "status": True
        })
    return web.json_response({
        "status": False
    })

