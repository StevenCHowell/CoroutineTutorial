import time
from asyncio import sleep
from aiohttp import web

FARM = {
    'cow': 'Moo!',
    'pig': 'Oink!',
    'chicken': 'Cluck!',
    'dog': 'Woof!',
}

async def hello(request):
    msg = 'Welcome to the farm!'
    return web.Response(text=msg)

async def speak(request):
    animal = request.match_info['name']
    if animal not in FARM:
        return web.Response(
            text='The animal {} was not found'.format(animal),
            status=404
        )

    await sleep(4)
    # time.sleep(3)

    return web.Response(text=FARM[animal])

app = web.Application()
app.router.add_get('/animals', hello)
resource = app.router.add_resource('/animals/{name}')
resource.add_route('GET', speak)

web.run_app(app)
