import asyncio
import threading
from APICommunication import HttpsRequest
from APICommunication import SocketCommunication
from LocalUserData import LocalUserData
from LoginWindow import Login
from SetupWindow import Setup


class Launcher:
    def __init__(self):
        self.userData = LocalUserData()
        self.com = ""
        self.result = ""

        self.httpConnect()

        self.threadSocket = threading.Thread(target=self.socketConnect)
        self.threadSocket.start()

        self.threadSetupWindow = threading.Thread(target=self.setupWindow)
        self.threadSetupWindow.start()

        self.threadSetupWindow.join()
        self.threadSocket.join()


        if self.result == 1:
            print("hello")
            self.com.disconnect()

    # Try to auto-connect to server
    def httpConnect(self):
        rqt = HttpsRequest()
        res = rqt.login(self.userData.getUserID(), self.userData.getUserPassword())
        if not res[0]:
            # Manually connect to server
            Login(self.userData, res[1])


    def socketConnect(self):
        self.com = SocketCommunication(self.userData)
        asyncio.run(self.com.task())

    def setupWindow(self):
        Setup(self.userData, self.result)




