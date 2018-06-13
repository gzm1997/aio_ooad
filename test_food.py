from models import food
from aiohttp_polls.aio_engine import init_engine
import asyncio

async def test_engine():
    engine = await init_engine()
    food_object = {
        "name": "fish",
        "picture": "https://demo/fish.png",
        "price": 53,
        "description": "this is a fish",
        "rating": "0.76",
        "amount": "21",
        "tag_id": 1
    }
    r = await food.insert(engine, food_object)
    #r = await food.select(engine, food_id = 12)
    #r = await food.like(engine, id = 1)
    #r = await food.sales_permonth(engine, id = 1)
    print(r)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(test_engine())



"""
    sa.Column("id", sa.Integer, primary_key = True),
    sa.Column("name", sa.String(50), unique = True, nullable = False),
    sa.Column("picture", sa.String(50)),
    sa.Column("price", sa.Integer, nullable = False),
    sa.Column("description", sa.String(50)),
    sa.Column("rating", sa.Float),
    sa.Column("amount", sa.Integer, nullable = False),
    sa.Column("tag_id", sa.Integer, sa.ForeignKey("tag.id"), nullable = False)
"""