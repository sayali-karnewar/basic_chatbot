import jinja2
import aiohttp_jinja2
from aiohttp import web
import asyncio

from setup import setupDB
from routes import routes

loop = asyncio.get_event_loop()
db = loop.run_until_complete(setupDB())

app = web.Application()
app['db'] = db
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

routes(app)

web.run_app(app)