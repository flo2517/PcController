import asyncio

from APICommunication import Server_communication
from LocalUserData import LocalUserData
from LoginWindow import Login
from SetupWindow import Setup
from RegisterWindow import Register


class Launcher:
    def __init__(self):
        userData = LocalUserData()
        # Check if there is user data
        """
        if userData.getUserID() == "[]" or userData.getUserPassword() == "[]":
            # Ask to user to give his ID and his password
        """
        Login(userData, "")
        #self.com = Server_communication(userData)
        #asyncio.run(self.com.task())

        #Setup(userData)



    def executeManual(self, commandID):
        self.osExecutor.exe(commandID)
