import asyncio
import socketio

import LocalUserData
from Executors import Executor

sio = socketio.AsyncClient()


class Server_communication:

    def __init__(self):
        self.tooken = LocalUserData()
        self.executor = Executor()

    async def task(self):
        await asyncio.gather(self.launchCom())

    async def launchCom(self):

        self.callBack()

        await sio.connect('http://thrallweb.fr:8080')



        await sio.wait()


    def callBack(self):
        @sio.event
        async def connect():
            await sio.emit('source', )
            print('connection established')

        @sio.on('pause')
        async def pause():
            self.executor.exe(6)

