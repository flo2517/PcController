import asyncio
import socketio


sio = socketio.AsyncClient()


@sio.event
async def connect():
    await sio.emit('source', data='Hello World')
    print('connection established')


@sio.on('test')
async def test(data):
    print(data['message'])


async def main():
    await sio.connect('http://localhost:8080')
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(main())
