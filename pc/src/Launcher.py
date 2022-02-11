import os
import platform
import signal
import sys
import threading
from multiprocessing import shared_memory as sm
from pc.src.setupOption.Icon import Icon

from pc.src.communication.SocketCommunicationClient import SocketCommunication
from pc.src.communication.HttpsRequest import HttpsRequest
from pc.src.loginRegister.LoginWindow import Login
from pc.src.setupOption.SetupWindow import Setup
from pc.src.dataUserManager.LocalUserData import LocalUserData


class Launcher:
    def __init__(self):
        self.userData = LocalUserData()

        # Shared memory to communicate with setup window
        shmWin = sm.SharedMemory(create=True, size=128)
        self.shmSetupWin = shmWin.buf
        self.shmSetupWin[0] = 0  # 0 = do nothing

        # Shared memory to communicate with the socket program
        shmSocket = sm.SharedMemory(create=True, size=128)
        self.shmSock = shmSocket.buf
        self.shmSock[0] = 0  # 0 = do nothing

        # Shared memory to communicate with icon thread
        self.shmIconInit = sm.SharedMemory(create=True, size=128)
        self.shmIcon = self.shmIconInit.buf
        self.shmIcon[0] = 0  # 0 = do nothing

        # Say if app need to restart after closing or not
        self.restart = False

        # Valid login data with http request
        self.httpConnect()

        # Creat and open socket connection in other thread
        self.comSock = SocketCommunication(self.userData, self.shmSock)
        self.threadSocket = threading.Thread(target=self.socketConnect)
        self.threadSocket.start()

        # Creat and open setup window
        self.threadSetupWindow = threading.Thread(target=self.setupWindow)
        self.threadSetupWindow.start()

        # Start new thread with icon
        self.threadIcon = threading.Thread(target=self.launchIcon)
        self.threadIcon.start()

        # Wait end of setup window
        self.threadSetupWindow.join()

        # Close icon thread
        self.shmIcon[0] = 1

        # Wait end of icon thread
        self.threadIcon.join()

        # Destroy shared memory
        self.shmIconInit.close()
        self.shmIconInit.unlink()

        # Del user data and restart app
        if self.shmSetupWin[0] == 1:
            shmWin.close()
            shmWin.unlink()
            self.shmSock[0] = 1
            self.threadSocket.join()
            shmSocket.close()
            shmSocket.unlink()
            self.userData.delUser()
            self.restart = True
            return

        # End app
        if self.shmSetupWin[0] == 2:
            shmWin.close()
            shmWin.unlink()
            self.shmSock[0] = 1
            self.threadSocket.join()
            shmSocket.close()
            shmSocket.unlink()
            sys.exit(0)

        self.threadSocket.join()
        shmSocket.close()
        shmSocket.unlink()

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

    # Launch setup window
    def setupWindow(self):
        Setup(self.userData, self.shmSetupWin)

    # Launch Icon
    def launchIcon(self):
        Icon(self.shmSetupWin, self.shmIcon)

    # Get restart value
    def getRestartValue(self):
        return self.restart
