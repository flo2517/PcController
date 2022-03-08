from src.dataUserManager.Encryption import Encryption
from uuid import uuid4
import os.path
import json

class LocalUserData:

    def __init__(self):
        # Init attributes
        self.dataFile = "userData.json"
        self.username = ''
        self.password = ''
        self.token = ''
        self.serverToken = ''
        self.e = Encryption(b"I'm-not-a-key")

        # check if file exist
        if not os.path.exists(self.dataFile):
            # Create file
            print("Create and format user data file")
            file = open(self.dataFile, "w")
            file.write('{"username":"", "password":"", "token":"", "jwt_token" : "", "server_token":""}')
            file.close()
        else:
            print("User data file exist")
            # Check if file exist but is empty
            file = open(self.dataFile, "r")
            data = file.read()
            file.close()
            if data == "":
                print("Reformat user data file")
                # Reformat file
                file = open(self.dataFile, "w")
                file.write('{"username":"", "password":"", "token":"", "jwt_token" : "", "server_token":""}')
                file.close()

        # Get data of data user file
        file = open(self.dataFile, "r")
        data = file.read()
        file.close()

        # Parse file
        data = json.loads(data)

        if len(data['username']) >= 16:
            self.username = self.e.decrypt(data["username"])
        if len(data['password']) >= 16:
            self.password = self.e.decrypt(data["password"])
        self.token = data["token"]
        self.jwtToken = data["jwt_token"]
        self.serverToken = data["server_token"]

        if self.token == "":
            # Create and save the token
            file = open(self.dataFile, "w")
            print("Creating token")
            # Generate the token
            self.token = uuid4().hex
            userData = '{"username":"' + data["username"] + '","password":"' + data["password"] + '","token":"' + str(self.token) + '","jwt_token":"' + data["jwt_token"] + '","server_token":"' + data["server_token"] + '"}'
            file.write(userData)
            file.close()
        print("User data:")
        print(data)

    def getUserID(self):
        if type(self.username) is bytes:
            return self.username.decode('latin-1')
        return self.username

    def setUserID(self, ID):
        self.username = ID
        file = open(self.dataFile, "w")
        userData = '{"username":"' + self.e.encrypt(str(self.username)) + '","password":"' + self.e.encrypt(str(self.password)) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    def getUserPassword(self):
        if type(self.password) is bytes:
            return self.password.decode('latin-1')
        return self.password

    def setUserPassword(self, password):
        self.password = password
        file = open(self.dataFile, "w")
        userData = '{"username":"' + self.e.encrypt(str(self.username)) + '","password":"' + self.e.encrypt(str(self.password)) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    # Reset user username and password
    def delUser(self):
        self.username = ""
        self.password = ""
        file = open(self.dataFile, "w")
        userData = '{"username":"' + self.e.encrypt(str(self.username)) + '","password":"' + self.e.encrypt(str(self.password)) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    def getToken(self):
        return self.token

    def delToken(self):
        self.token = ""
        file = open(self.dataFile, "w")
        userData = '{"username":"' + self.e.encrypt(str(self.username)) + '","password":"' + self.e.encrypt(str(self.password)) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    # Generate new token and save it
    def refreshToken(self):
        self.token = uuid4().hex
        file = open(self.dataFile, "w")
        userData = '{"username":"' + self.e.encrypt(str(self.username)) + '","password":"' + self.e.encrypt(str(self.password)) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    def getServerToken(self):
        return self.serverToken

    def setServerToken(self, newServerToken):
        self.serverToken = newServerToken
        file = open(self.dataFile, "w")
        userData = '{"username":"' + self.e.encrypt(str(self.username)) + '","password":"' + self.e.encrypt(str(self.password)) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    def setJwtToken(self, newJwtToken):
        self.jwtToken = newJwtToken
        file = open(self.dataFile, "w")
        userData = '{"username":"' + self.e.encrypt(str(self.username)) + '","password":"' + self.e.encrypt(str(self.password)) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    def getJwtToken(self):
        return self.jwtToken
