import sys
import threading
from multiprocessing import shared_memory as sm

from src.communication.SocketCommunicationClient import SocketCommunication
from src.communication.HttpsRequest import HttpsRequest
from src.loginRegister.LoginWindow import Login
from src.setupOption.SetupWindow import Setup
from src.dataUserManager.LocalUserData import LocalUserData


class Launcher:
    def __init__(self):
        self.userData = LocalUserData()

        # Shared memory to communicate with the socket program
        shmSocket = sm.SharedMemory(create=True, size=128)
        self.shmSock = shmSocket.buf
        self.shmSock[0] = 0  # 0 = do nothing

        # Say if app need to restart after closing or not
        self.restart = False

        # Valid login data with http request
        self.httpConnect()

        # Creat and open socket connection in other thread
        self.comSock = SocketCommunication(self.userData, self.shmSock)
        self.threadSocket = threading.Thread(target=self.socketConnect)
        self.threadSocket.start()

        # Creat and open setup window
        win = Setup(self.userData)

        # Del user data and restart app
        if win.getEndResult():
            self.shmSock[0] = 1
            self.threadSocket.join()
            shmSocket.close()
            shmSocket.unlink()
            self.userData.delUser()
            self.restart = True
            return

        # End app
        else:
            self.shmSock[0] = 1
            self.threadSocket.join()
            shmSocket.close()
            shmSocket.unlink()
            sys.exit(0)

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
        self.comSock.launchCom()

    # Get restart value
    def getRestartValue(self):
        return self.restart
