import asyncio
import threading
from multiprocessing import shared_memory as sm
from APICommunication import HttpsRequest
from APICommunication import SocketCommunication
from LocalUserData import LocalUserData
from LoginWindow import Login
from SetupWindow import Setup


class Launcher:
    def __init__(self):
        self.userData = LocalUserData()
        shmWin = sm.SharedMemory(create=True, size=128)
        self.result = shmWin.buf
        self.result[0] = 0

        shmSocket = sm.SharedMemory(create=True, size=128)
        self.shmSock = shmSocket.buf
        self.shmSock[0] = 0

        self.restart = False

        self.httpConnect()

        self.com = SocketCommunication(self.userData, self.shmSock)

        self.threadSocket = threading.Thread(target=self.socketConnect)
        self.threadSocket.start()

        self.threadSetupWindow = threading.Thread(target=self.setupWindow)
        self.threadSetupWindow.start()

        self.threadSetupWindow.join()

        # Del user data and restart app
        if self.result[0] == 1:
            shmWin.close()
            shmWin.unlink()
            self.shmSock[0] = 1
            self.threadSocket.join()
            self.userData.delUser()
            self.restart = True
            return

        self.threadSocket.join()

    # Authentication with server
    def httpConnect(self):
        rqt = HttpsRequest()
        # Try to auto-connect to server
        res = rqt.login(self.userData.getUserID(), self.userData.getUserPassword())
        if not res[0]:
            # Manually connect to server
            Login(self.userData, res[1])

    # Launch socket connection
    def socketConnect(self):
        asyncio.run(self.com.task())

    # Launch setup window
    def setupWindow(self):
        Setup(self.userData, self.result)

    # Get restart value
    def getRestartValue(self):
        return self.restart
