import asyncio
import sys
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

        # Shared memory to communicate with setup window
        shmWin = sm.SharedMemory(create=True, size=128)
        self.result = shmWin.buf
        self.result[0] = 0  # 0 = do nothing

        # Shared memory to communicate with the socket program
        shmSocket = sm.SharedMemory(create=True, size=128)
        self.shmSock = shmSocket.buf
        self.shmSock[0] = 0  # 0 = do nothing

        # Say if app need to restart after closing or not
        self.restart = False

        # Valid login data with http request
        self.httpConnect()

        # Creat and open socket connection in other thread
        self.com = SocketCommunication(self.userData, self.shmSock)
        self.threadSocket = threading.Thread(target=self.socketConnect)
        self.threadSocket.start()

        # Creat and open setup window
        self.threadSetupWindow = threading.Thread(target=self.setupWindow)
        self.threadSetupWindow.start()

        # Wait end of setup window
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

        # End app
        if self.result[0] == 2:
            shmWin.close()
            shmWin.unlink()
            self.shmSock[0] = 1
            self.threadSocket.join()
            sys.exit(0)

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
