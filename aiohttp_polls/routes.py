import pathlib
import sys
import aiohttp_cors


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
    # app.router.add_post("/api/verify_cookies", keeper_view.verify_cookies)
    app.router.add_get("/api/need_cookies_page", keeper_view.need_cookies_page)

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })
    for route in list(app.router.routes()):
        cors.add(route)
    return app

    # redis = await aioredis.create_pool(('localhost', 6379))
    # storage = redis_storage.RedisStorage(redis)
    # setup(app, storage)

    # setup(app, EncryptedCookieStorage(b'Thirty  two  length  bytes  key.'))


