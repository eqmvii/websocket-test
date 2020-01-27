#!/usr/bin/env python3.7

# WS client example
# Run with
# python3.7 python_socket_test.py 

print("hello, world")

import asyncio
import websockets

# dying here:
# eqmvii@eqmvii-VirtualBox:~/websocket-test$ python3.7 python_socket_test.py 
# hello, world
# Traceback (most recent call last):
#   File "python_socket_test.py", line 10, in <module>
#     import websockets
# ModuleNotFoundError: No module named 'websockets'


async def hello():
    uri = "ws://ericwstest.herokuapp.com/"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())