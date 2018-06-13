import aiomysql.sa 
from aiohttp_polls.setting import config

config = config["mysql"]
async def init_engine():
    engine = await aiomysql.sa.create_engine(user = config["user"], db = config["database"], host = config["host"], password = config["password"])
    return engine
#engine = await init_engine()
