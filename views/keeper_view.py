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
import sales
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


async def verify_login(engine, session):
    if "ooad" not in session or "login" not in session or "time" not in session:
        # print("not login")
        return False
    name = session["ooad"]
    psw = session["login"]
    r = await keeper.verify(engine, name = name, psw = psw)
    # print("verify r", r)
    if r:
        return True
    return False

async def reservation_count_by_month(request):
    engine = await aio_engine.init_engine()
    session = await get_session(request)
    r = await verify_login(engine, session)
    print("r", r)
    if not r:
        return web.json_response({
            "info": "you have not login!"
        })
    result_l = []
    n = datetime.datetime.now()
    for i in range(1, 13):
        year = n.year
        if i <= 9:
            year_mon = str(year) + "-0" + str(i)
        else:
            year_mon = str(year) + "-" + str(i)
        num = await sales.sales_reservation.select_count_by_month(engine, year, str(i))
        num = len(num)
        result_l.append({
            "x": year_mon,
            "y": num
        })
    return web.json_response(result_l)


async def reservation_quantity_piedata(request):
    engine = await aio_engine.init_engine()
    session = await get_session(request)
    r = await verify_login(engine, session)
    if not r:
        return web.json_response({
            "info": "you have not login!"
        })
    r = await sales.reservation_quantity_piedata(engine)
    return web.json_response(r)




async def total_static_info(request):
    engine = await aio_engine.init_engine()
    session = await get_session(request)
    r = await verify_login(engine, session)
    if not r:
        return web.json_response({
            "info": "you have not login!"
        })
    r = await sales.sales_reservation.total_static_info(engine)
    return web.json_response(r)


async def transaction_count_by_month(request):
    engine = await aio_engine.init_engine()
    session = await get_session(request)
    r = await verify_login(engine, session)
    if not r:
        return web.json_response({
            "info": "you have not login!"
        })
    r_list = []
    n = datetime.datetime.now()
    year = n.year
    for i in range(1, 13):
        if i <= 9:
            year_mon = str(year) + "-0" + str(i)
        else:
            year_mon = str(year) + "-" + str(i)
        all_r_in_that_mon = await sales.sales_reservation.select_count_by_month(engine, year, i)
        transation_in_that_mon = 0
        for r in all_r_in_that_mon:
            transation_in_that_mon += r["total"]
        r_list.append({
            "x": year_mon,
            "y": transation_in_that_mon
        })
    return web.json_response(r_list)


async def turnover_piedata(request):
    engine = await aio_engine.init_engine()
    session = await get_session(request)
    r = await verify_login(engine, session)
    if not r:
        return web.json_response({
            "info": "you have not login!"
        })
    r_list = await sales.turnover_piedata(engine)
    return web.json_response(r_list)



