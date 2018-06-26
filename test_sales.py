from models import sales
from aiohttp_polls.aio_engine import init_engine
import asyncio

async def test_sales():
    engine = await init_engine()
    r = await sales.reservation_quantity_piedata(engine)
    print(r)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(test_sales())