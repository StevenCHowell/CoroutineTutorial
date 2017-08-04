# # Initial
# import time

# # Manual coroutine
# import types
#
# @types.coroutine
# def manual_sleep(n):
#     yield 'Please call me back in {} seconds'.format(n)

import asyncio

async def square(x):
    print('Starting square for {}...'.format(x))
    sleep_time = 3
    # time.sleep(sleep_time)
    # await manual_sleep(sleep_time)
    await asyncio.sleep(sleep_time)
    print('Finishing square for {}.'.format(x))
    return x * x

async def cube(x):
    print('Starting cube for {}...'.format(x))
    sleep_time = 3
    # time.sleep(sleep_time)
    # await manual_sleep(sleep_time)
    await asyncio.sleep(sleep_time)
    y = await square(x)
    print('Finishing cube for {}.'.format(x))
    return y * x
