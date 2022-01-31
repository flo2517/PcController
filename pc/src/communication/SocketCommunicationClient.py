import asyncio
import socketio
import json

from pc.src.communication.HttpsRequest import HttpsRequest
from pc.src.osExecutors.Executor import Executor

sio = socketio.AsyncClient()


class SocketCommunication:

    def __init__(self, localUserData, shmSock):
        self.localUserData = localUserData
        self.executor = Executor()
        self.shmSock = shmSock

    async def task(self):
        await asyncio.gather(self.launchCom())

    async def launchCom(self):

        self.callBack()

        # await sio.connect("http://thrallweb.fr:8080/")
        await sio.connect("laurahost.fr:8080/")


        await sio.wait()

    def callBack(self):
        @sio.event
        async def connect():
            pload = json.dumps({"token": self.localUserData.getToken(), "user": self.localUserData.getJwtToken()})
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

        @sio.on('error')
        async def error(msg):
            print(msg)
            print("Error : " + msg['message'])
            if msg['message'] == 'Unauthorized! Access Token was expired!':
                rqt = HttpsRequest()
                res = rqt.refreshToken(self.localUserData.getServerToken())
                if res[0]:
                    self.localUserData.setServerToken(res[1])
                else:
                    res = rqt.login(self.localUserData.getUserID(), self.localUserData.getPassword())
                    if res[0]:
                        # Save tokens
                        self.localUserData.setJwtToken(res[1])
                        self.localUserData.setServerToken(res[2]['token'])
                    else:
                        await sio.disconnect()
                        print('Error : ' + res[1])

        # In background of socket communication check
        # on shared memory if connection need to be ended
        async def backgroundTask():
            while True:
                if self.shmSock[0] == 1:
                    print("Disconnected")
                    await sio.disconnect()
                    return
                await sio.sleep(1)

        # Launch background task
        sio.start_background_task(backgroundTask)
