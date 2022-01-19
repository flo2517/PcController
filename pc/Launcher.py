import asyncio
from APICommunication import HttpsRequest
from APICommunication import SocketCommunication
from LocalUserData import LocalUserData
from LoginWindow import Login
from SetupWindow import Setup

class Launcher:
    def __init__(self):
        userData = LocalUserData()

        # Try to auto-connect to server
        rqt = HttpsRequest()
        res = rqt.login(userData.getUserID(), userData.getUserPassword())
        if not res[0]:
            # Manually connect to server
            Login(userData, res[1])

        self.com = SocketCommunication(userData)
        asyncio.run(self.com.task())
        Setup(userData)
