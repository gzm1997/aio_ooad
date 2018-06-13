from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/set_cookies")
async def set_cookies(request):
    data = await request.json()
    user = data["user"]
    psw = data["psw"]
    r = web.json_response({
        "status": True
    })
    r.set_cookie(name=user, value=psw)
    return r


app = web.Application()
app.router.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, port=5000)