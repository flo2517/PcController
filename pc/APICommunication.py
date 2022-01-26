import asyncio
import socketio
import requests
import json
from Executors import Executor

sio = socketio.AsyncClient()

serverAddress = "http://thrallweb.fr:8080/"


class HttpsRequest:

    def __init__(self):
        self.address = serverAddress

    # Send register request to server
    def register(self, email, password):
        pload = {"email": email, "username": "johndoe", "password": password}
        r = requests.post(self.address + "register", data=pload)
        requestResult = r.json()
        if requestResult['success']:
            print(requestResult['message'])
            return [True, requestResult['token']]
        else:
            print(requestResult['message'])
            return [False, requestResult['message']]

    # Send login request to server
    def login(self, email, password):
        pload = {"email": email, "password": password}
        r = requests.post(self.address + "login", data=pload)
        requestResult = r.json()
        if requestResult['success']:
            print(requestResult['message'])
            return [True, requestResult['token'], requestResult['refreshToken']]
        else:
            print(requestResult['message'])
            return [False, requestResult['message']]

    # Send refresh token request to server
    def refreshToken(self, serverToken):
        pload = {"refreshToken": serverToken}
        r = requests.post(self.address + "refreshToken", data=pload)
        requestResult = r.json()
        if requestResult['success']:
            print("Token refreshed successfully")
            return [True, requestResult['refreshToken']['token']]
        else:
            print("Error : Token refresh failed cause of \"" + requestResult['message'] + "\"")
            return [False, requestResult["message"]]

    # Send change password request to server
    def changePassword(self, oldPassword, newPassword):
        pload = {"oldPassword": oldPassword, "newPassword": newPassword}
        r = requests.post(self.address + "user/changePassword", data=pload)
        requestResult = r.json()
        if requestResult['message'] == "Password changed successfully":
            print(requestResult["message"])
            return True
        else:
            print("Error : Password changed failed cause of \"" + requestResult['message'] + "\"")
            return False

    # Send del user account request to server
    def delAccount(self, password):
        pload = {"password": password}
        r = requests.post(self.address + "user/deleteAccount", data=pload)
        requestResult = r.json()
        if requestResult['message'] == "Account deleted successfully":
            print(requestResult["message"])
            return True
        else:
            print("Error : Account deleted failed cause of \"" + requestResult['message'] + "\"")
            return False


class SocketCommunication:

    def __init__(self, localUserData, shmSock):
        self.localUserData = localUserData
        self.executor = Executor()
        self.shmSock = shmSock

    async def task(self):
        await asyncio.gather(self.launchCom())

    async def launchCom(self):

        self.callBack()

        await sio.connect(serverAddress)

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
        async def background_task():
            while True:
                if self.shmSock[0] == 1:
                    print("Disconnected")
                    await sio.disconnect()
                    return
                await sio.sleep(1)

        # Launch background task
        sio.start_background_task(background_task)
