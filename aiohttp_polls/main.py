from aiohttp import web
from aiohttp_polls import routes
app = web.Application()
routes.setup_routes(app)