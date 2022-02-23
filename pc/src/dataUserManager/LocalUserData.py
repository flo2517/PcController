from uuid import uuid4
import os.path
import json
import hashlib


class LocalUserData:

    def __init__(self):
        # Init attributes
        self.dataFile = "userData.json"
        self.username = ''
        self.password = ''
        self.token = ''
        self.serverToken = ''

        # check if file exist
        if not os.path.exists(self.dataFile):
            # Create file
            print("Create and format user data file")
            userData = '{"username":"", "password":"", "token":"", "jwt_token" : "", "server_token":""}'
            self.encode(userData)
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

        self.username = data["username"]
        self.password = data["password"]
        self.token = data["token"]
        self.jwtToken = data["jwt_token"]
        self.serverToken = data["server_token"]

        if self.token == "":
            # Create and save the token
            print("Creating token")
            # Generate the token
            self.token = uuid4().hex
            userData = '{"username":"' + str(self.username) + '","password":"' + str(
                self.password) + '","token":"' + str(
                self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(
                self.serverToken) + '"}'
            self.encode(userData)

        print("User data:")
        print(data)

    def encode(self, userData):
        file = open(self.dataFile, "w")
        file.write(hashlib.sha256(userData).hexdigest())
        file.close()

    def decode(self, userData):
        file = open(self.dataFile, "r")
        data = file.read()
        file.close()
        return hashlib.sha256(data).hexdigest().decode('ascii')

    def getUserID(self):
        return self.username

    def setUserID(self, ID):
        self.username = ID
        file = open(self.dataFile, "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    def getUserPassword(self):
        return self.password

    def setUserPassword(self, password):
        self.password = password
        file = open(self.dataFile, "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    # Reset user username and password
    def delUser(self):
        self.username = ""
        self.password = ""
        file = open(self.dataFile, "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    def getToken(self):
        return self.token

    def delToken(self):
        self.token = ""
        file = open(self.dataFile, "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    # Generate new token and save it
    def refreshToken(self):
        self.token = uuid4().hex
        file = open(self.dataFile, "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    def getServerToken(self):
        return self.serverToken

    def setServerToken(self, newServerToken):
        self.serverToken = newServerToken
        file = open(self.dataFile, "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    def setJwtToken(self, newJwtToken):
        self.jwtToken = newJwtToken
        file = open(self.dataFile, "w")
        userData = '{"username":"' + str(self.username) + '","password":"' + str(self.password) + '","token":"' + str(
            self.token) + '","jwt_token":"' + str(self.jwtToken) + '","server_token":"' + str(self.serverToken) + '"}'
        file.write(userData)
        file.close()
        return 0

    def getJwtToken(self):
        return self.jwtToken
