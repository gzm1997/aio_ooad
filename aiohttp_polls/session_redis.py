from aiohttp_session import setup, redis_storage
import aioredis
import asyncio

async def get_storage():
    redis = await aioredis.create_pool(("localhost", 6379))
    return  redis_storage.RedisStorage(redis)

def setup_session_support(app):
    storage = asyncio.get_event_loop().run_until_complete(get_storage())
    setup(app, storage)
    return app