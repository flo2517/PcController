import asyncio
import socketio

sio = socketio.AsyncClient()


class Receiver:

    def __init__(self, token, executor):
        self.token = token
        self.executor = executor

    async def task(self):
        await asyncio.gather(self.launchCom())

    async def launchCom(self):

        self.call_back()

        await sio.connect('http://thrallweb.fr:8080')



        await sio.wait()


    def call_back(self):
        @sio.event
        async def connect():
            await sio.emit('source', {'token': self.token})
            print('connection established')

        @sio.on('pause')
        async def pause():
            self.executor.exe(6)


