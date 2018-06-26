import pathlib
import sys
import aiohttp_cors
from aiojobs.aiohttp import setup


BASE_DIR = pathlib.Path(__file__).parent.parent
views_path = BASE_DIR / "views"
sys.path.append(str(views_path))
import food_view
import reservation_view
import keeper_view

def setup_routes(app):
    app.router.add_get("/api/product/{id}", food_view.get_food)
    app.router.add_get("/api/products", food_view.get_all_food)
    app.router.add_get("/api/order/{id}", reservation_view.get_order)
    app.router.add_post("/api/order", reservation_view.create_order)


    app.router.add_post("/api/login", keeper_view.login)
    app.router.add_get("/api/need_cookies_page", keeper_view.need_cookies_page)
    app.router.add_get("/api/reservation_count_by_month", keeper_view.reservation_count_by_month)
    app.router.add_get("/api/reservation_quantity_pie_data", keeper_view.reservation_quantity_piedata)
    app.router.add_get("/api/total_static_info", keeper_view.total_static_info)
    app.router.add_get("/api/transaction_count_by_month", keeper_view.transaction_count_by_month)
    app.router.add_get("/api/turnover_piedata", keeper_view.turnover_piedata)

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })
    for route in list(app.router.routes()):
        cors.add(route)
    setup(app)
    return app

    # redis = await aioredis.create_pool(('localhost', 6379))
    # storage = redis_storage.RedisStorage(redis)
    # setup(app, storage)

    # setup(app, EncryptedCookieStorage(b'Thirty  two  length  bytes  key.'))


