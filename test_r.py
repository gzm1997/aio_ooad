from models import reservation
from aiohttp_polls.aio_engine import init_engine
import asyncio
import datetime

async def test_engine():
    # r_object = {
    #     "isPaid": True,
    #     "table_num": 12,
    #     "food_list": {"pork": 1, "fish": 2},
    #     "total": 34
    # }
    engine = await init_engine()
    #r = await reservation.insert(engine, r_object)
    # r = await reservation.select(engine, reserve_datetime = "2018-05-24 21:46:24", table_num = 12)
    n = datetime.datetime.now()
    year = n.year
    mon = n.month
    r = await reservation.select_count_by_month(engine, year, mon)
    print(r)
    # print("len of r", len(r))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(test_engine())



"""
    sa.Column("id", sa.Integer, primary_key = True),
    sa.Column("reserve_datetime", sa.DateTime, default = datetime.datetime.now()),
    sa.Column("pay_datetime", sa.DateTime),
    sa.Column("table_num", sa.Integer, nullable = False),
    sa.Column("food_list", sa.JSON)
"""