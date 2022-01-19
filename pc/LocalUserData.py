from uuid import uuid4
import os.path
import json


class LocalUserData:

    def __init__(self):
        # Init attributes
        self.username = ''
        self.password = ''
        self.token = ''
        self.server_token = ''

        # check if file exist
        if not os.path.exists("userData.json"):
            # Create file
            print("Create and format user data file")
            file = open("userData.json", "w")
            file.write('{"username":"", "password":"", "token":"", "server_token" : ""}')
            file.close()
        else:
            print("User data file exist")
            # Check if file exist but is empty
            file = open("userData.json", "r")
            data = file.read()
            file.close()
            if data == "":
                print("Reformat user data file")
                # Reformat file
                file = open("userData.json", "w")
                file.write('{"username":"", "password":"", "token":"", "server_token" : ""}')
                file.close()

        # Get data of data user file
        file = open("userData.json", "r")
        data = file.read()
        file.close()

        # Parse file
        data = json.loads(data)

        self.username = data["username"]
        self.password = data["password"]
        self.token = data["token"]
        self.server_token = data["server_token"]

        if self.token == "":
            file = open("userData.json", "w")
            # Create and save the token
            print("Creating token")
            # Generate the token
            self.token = uuid4().hex
            userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
                self.token) + '","server_token":"' + str(self.server_token)+'"}'
            file.write(userData)
            file.close()

        print("User data:")
        print(data)

    def getUserID(self):
        return self.username

    def setUserID(self, ID):
        self.username = ID
        file = open("userData.json", "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","server_token":"' + str(self.server_token) + '"}'
        file.write(userData)
        file.close()
        return 0

    def getUserPassword(self):
        return self.password

    def setUserPassword(self, password):
        self.password = password
        file = open("userData.json", "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","server_token":"' + str(self.server_token) + '"}'
        file.write(userData)
        file.close()
        return 0

    # Reset user username and password
    def delUser(self):
        self.username = ""
        self.password = ""
        file = open("userData.json", "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","server_token":"' + str(self.server_token) + '"}'
        file.write(userData)
        file.close()
        return 0

    def getToken(self):
        return self.token

    def delToken(self):
        self.token = ""
        file = open("userData.json", "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","server_token":"' + str(self.server_token) + '"}'
        file.write(userData)
        file.close()
        return 0

    # Generate new token and save it
    def refreshToken(self):
        self.token = uuid4().hex
        file = open("userData.json", "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","server_token":"' + str(self.server_token) + '"}'
        file.write(userData)
        file.close()
        return 0

    def getServerToken(self):
        return self.server_token

    def setServerToken(self, newServerToken):
        self.server_token = newServerToken
        file = open("userData.json", "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","server_token":"' + str(self.server_token) + '"}'
        file.write(userData)
        file.close()
        return 0
