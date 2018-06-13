from models import tag
from aiohttp_polls.aio_engine import init_engine
import asyncio

async def test_engine():
    engine = await init_engine()
    tag_object = {"description": "this is a new tag", "picture": "this is a tag picture"}
    r = await tag.insert(engine, tag_object)
    print(r)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(test_engine())


"""
    sa.Column("id", sa.Integer, primary_key = True),
    sa.Column("description", sa.String(50)),
    sa.Column("picture", sa.String(50))
"""