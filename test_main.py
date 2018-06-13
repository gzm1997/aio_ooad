from aiohttp_polls import main
from aiohttp import web
import argparse
import asyncio

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="aiohttp server example")
    parser.add_argument('--path')
    parser.add_argument('--port')
    app = main.app
    args = parser.parse_args()
    web.run_app(app, host="0.0.0.0", port=args.port, path=args.path)

