from models import food
from models import tag
from models import comment
from models import reservation
from models import keeper
from aiohttp_polls.aio_engine import init_engine
import asyncio

async def insert_sample_data():
    engine = await init_engine()
    tag_object = {"description": "this is a new tag", "picture": "this is a tag picture"}
    food_object = {
        "name": "pork",
        "picture": "https://i8.meishichina.com/attachment/recipe/2014/07/18/20140718114832312460803.jpg?x-oss-process=style/p800",
        "price": 53,
        "description": "this is a pork",
        "rating": "0.8",
        "amount": "100",
        "tag_id": 1
    }
    food_object1 = {
        "name": "fish",
        "picture": "https://www.jucanw.com/UploadFiles/2013-05/admin/2013051715282196795.jpg",
        "price": 32,
        "description": "this is a fish",
        "rating": "0.4",
        "amount": "10",
        "tag_id": 1
    }

    r_object = {
        "isPaid": True,
        "table_num": 12,
        "food_list": {"pork": 13, "fish": 2},
        "total": 34
    }
    keeper_object = {
        "name": "root",
        "psw": "Gzm20125"
    }
    r = await tag.insert(engine, tag_object)
    print("tag r", r)
    r = await food.insert(engine, food_object)
    print("food r", r)
    r = await food.insert(engine, food_object1)
    print("food r", r)
    r = await reservation.insert(engine, r_object)
    print("reservation r", r)
    r = await keeper.insert(engine, keeper_object)
    print("keeper r", r)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(insert_sample_data())
