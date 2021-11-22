import asyncio
import json

import socketio

sio = socketio.AsyncClient()


@sio.event
async def connect():
    await sio.emit('source', data='Hello World')
    print('connection established')


@sio.on('shutdown')
async def test():
    print('shutdown')

@sio.on('volumeUp')
async def volumeUp():
    print('volumeUp')


async def main():
    await sio.connect('http://localhost:8080')
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(main())
