import asyncio

from APICommunication import Server_communication
import LocalUserData


class Launcher:
    def __init__(self):
        userData = LocalUserData()
        #Check if there is user data
        """"if userData.getUserID() == "[]" or userData.getUserPassword() == "[]":
            #Ask to user to give his ID and his password
        """

        self.com = Server_communication()
        asyncio.run(self.com.task())



    def executeManual(self, commandID):
        self.osExecutor.exe(commandID)
