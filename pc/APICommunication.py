import asyncio
import socketio
import requests
from Executors import Executor

sio = socketio.AsyncClient()


class HttpsRequest:

    def __init__(self):
        self.address = "http://thrallweb.fr:8080/"

    def register(self, email, password):
        pload = {"email": email, "username": "johndoe", "password": password}
        r = requests.post(self.address + "register", data=pload)
        dico = r.json()
        if dico['success']:
            print(dico['message'])
            return [True, dico['token']]
        else:
            print(dico['message'])
            return [False, dico['message']]

    def login(self, email, password):
        pload = {"email": email, "password": password}
        r = requests.post(self.address + "login", data=pload)
        dico = r.json()
        if dico['success']:
            print(dico['message'])
            return [True, dico['token']]
        else:
            print(dico['message'])
            return [False, dico['message']]



class SocketCommunication:

    def __init__(self, localUserData, shmSock):
        self.localUserData = localUserData
        self.executor = Executor()
        self.shmSock = shmSock

    async def task(self):
        await asyncio.gather(self.launchCom())

    async def launchCom(self):

        self.callBack()

        await sio.connect('http://thrallweb.fr:8080')

        await sio.wait()

    def callBack(self):
        @sio.event
        async def connect():
            pload = {"token": self.localUserData.getToken()}
            await sio.emit('source', pload)
            print('Connection established')

        @sio.on('volumeMute')
        async def mute():
            self.executor.execute(4)

        @sio.on('volumePlay')
        async def play():
            self.executor.execute(5)

        @sio.on('volumeUp')
        async def vUp():
            self.executor.execute(2)

        @sio.on('volumeDown')
        async def vDown():
            self.executor.execute(3)

        async def background_task():
            while True:
                if self.shmSock[0] == 1:
                    print("Disconnected")
                    await sio.disconnect()
                    return
                await sio.sleep(1)

        sio.start_background_task(background_task)
