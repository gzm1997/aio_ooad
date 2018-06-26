from aiohttp import web
from aiohttp_polls import routes
from aiohttp_polls import session_encrypt
from aiohttp_polls import session_redis

app = web.Application()
app = routes.setup_routes(app)
app = session_encrypt.setup_session_support(app)
# app = session_redis.setup_session_support(app)