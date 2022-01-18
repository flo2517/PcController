import asyncio
import socketio
import requests

from Executors import Executor

sio = socketio.AsyncClient()


class HttpsRequest:

    def __init__(self):
        self.address = "http://thrallweb:8080/"

    def register(self, email, password):
        pload = {"email": email, "username": "johndoe", "password": password}
        r = requests.post(self.address+"register", data=pload)
        print(r)

    def login(self, email, password):
        pload = {"email": email, "password": password}
        r = requests.post(self.address+"login", data=pload)
        print(r)


class SocketCommunication:

    def __init__(self, localUserData):
        self.localUserData = localUserData
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

