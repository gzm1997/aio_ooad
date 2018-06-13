from aiohttp import web
import pathlib
import yaml
import sys

BASE_DIR = pathlib.Path(__file__).parent.parent
models_path = BASE_DIR / "models"
aiohttp_polls_path = BASE_DIR / "aiohttp_polls"
sys.path.append(str(models_path))
sys.path.append(str(aiohttp_polls_path))

import sales
import aio_engine

async def get_food(request):
    id = int(request.match_info['id'])
    engine = await aio_engine.init_engine()
    record = await sales.sales_food.select(engine, food_id = id)
    if record == []:
        return web.json_response({})
    record = record[0]
    sales_permonth = await sales.sales_permonth(engine, id = id)
    record["sales_permonth"] = sales_permonth
    return web.json_response(record)

async def get_all_food(request):
    engine = await aio_engine.init_engine()
    records = await sales.sales_food.select(engine)
    if records == []:
        return web.json_response({})
    #print("records", records)
    for r in records:
        #print("r", r)
        id = r["id"]
        sales_permonth = await sales.sales_permonth(engine, id = id)
        r["sales_permonth"] = sales_permonth
    return web.json_response({"result": records})
