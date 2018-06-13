from models import keeper
from aiohttp_polls.aio_engine import init_engine
import asyncio

async def test_keeper():
    engine = await init_engine()
    # keeper_object = {
    #     "name": "root",
    #     "psw": "Gzm20125"
    # }
    # r = await keeper.insert(engine, keeper_object)
    r = await keeper.verify(engine, "root", "Gzm20125")
    print(r)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(test_keeper())