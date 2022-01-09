import asyncio

from pc.APICommunication import Server_communication
from pc.LocalUserData import LocalUserData


class Launcher:
    def __init__(self):
        userData = LocalUserData()
        #Check if there is user data
        """"if userData.getUserID() == "[]" or userData.getUserPassword() == "[]":
            #Ask to user to give his ID and his password
        """

        self.com = Server_communication()
        asyncio.run(self.com.task())
