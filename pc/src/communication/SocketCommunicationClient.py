import asyncio
import sys

import socketio
import json

from pc.src.communication.HttpsRequest import HttpsRequest
from pc.src.osExecutors.Executor import Executor

sio = socketio.Client()


class SocketCommunication:

    def __init__(self, localUserData, shmSock):
        self.localUserData = localUserData
        self.executor = Executor()
        self.shmSock = shmSock

    async def task(self):
        await asyncio.gather(self.launchCom())

    def launchCom(self):

        self.callBack()

        sio.connect("http://thrallweb.fr:8080/")


        sio.wait()


    def callBack(self):
        @sio.event
        def connect():
            pload = json.dumps({"token": self.localUserData.getToken(), "user": self.localUserData.getJwtToken()})
            sio.emit('source', pload)
            print('Connection established')

        @sio.on('volumeMute')
        def mute():
            self.executor.execute(4)

        @sio.on('volumePlay')
        def play():
            self.executor.execute(5)

        @sio.on('volumeUp')
        def vUp():
            self.executor.execute(2)

        @sio.on('volumeDown')
        def vDown():
            self.executor.execute(3)

        @sio.on('error')
        def error(msg):
            rqt = HttpsRequest()
            print(msg)
            print("Error : " + msg['message'])
            if msg['message'] == 'Unauthorized! Access Token was expired!':
                res = rqt.refreshToken(self.localUserData.getServerToken())
                if res[0]:
                    self.localUserData.setServerToken(res[1])
                else:
                    res = rqt.login(self.localUserData.getUserID(), self.localUserData.getUserPassword())
                    if res[0]:
                        # Save tokens
                        self.localUserData.setJwtToken(res[1])
                        self.localUserData.setServerToken(res[2]['token'])
                    else:
                        sio.disconnect()
                        print('Error : ' + res[1])
            if msg['message'] == "User has no devices" or "Device not found":
                print("Adding device...")
                res = rqt.addDevice(self.localUserData)
                if res:
                    pload = json.dumps({"token": self.localUserData.getToken(), "user": self.localUserData.getJwtToken()})
                    sio.emit('source', pload)
                else:
                    print('Error : Can\'t add device')
                    sio.disconnect()
                    return

        # In background of socket communication check
        # on shared memory if connection need to be ended
        def backgroundTask():
            while True:
                if self.shmSock[0] == 1:
                    print("Disconnected")
                    sio.disconnect()
                    return
                sio.sleep(1)

        # Launch background task
        sio.start_background_task(backgroundTask)
