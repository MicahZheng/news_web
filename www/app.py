import logging; logging.basicConfig(level=logging.INFO)

import asyncio,json,os,time
from datetime import datetime

from aiohttp import web
from aiohttp import web_runner


def index(request):
	return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init():
		app = web.Application()
		runner = web.AppRunner(app)
		app.router.add_route('GET', '/', index)
		await runner.setup()
		logging.info('server started at http://127.0.0.1:9000...')
		site = web.TCPSite(runner, '127.0.0.1', 9000)
		await site.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()