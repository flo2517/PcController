from uuid import uuid4
import os.path

class LocalUserData:

    def __init__(self):
        # Init attributes
        self.ID = ''
        self.password = ''
        self.tooken = ''

        # check if file exist
        if not os.path.exists("userData.json"):
            # Create file
            file = open("userData.json", "w")
            file.write("[]\n[]\n[]")
            file.close()
        else:
            # Check if file exist but is empty
            file = open("userData.json", "r")
            data = file.read()
            file.close()
            if data == "":
                # Reformat file
                file = open("userData.json", "w")
                file.write("[]\n[]\n[]")
                file.close()


        # Get data of data user file
        file = open("userData.json", "r")
        line = file.readline()
        index = 0

        # Parse file
        while line:
            if index == 0:
                self.ID = line
                self.ID = self.ID.replace("\n", "")
            elif index == 1:
                self.password = line
                self.password = self.password.replace("\n", "")
            elif index == 2:
                self.tooken = line

            line = file.readline()
            index += 1

        file.close()
        print("Index = ", index)
        print("id = ", self.ID)
        print("password = ", self.password)
        print("tooken = ", self.tooken)

        if self.tooken == "[]":
            file = open("userData.json", "w")
            # Create and save the tooken
            print("Creating tooken")
            # Generate the tooken
            self.tooken = uuid4().hex
            userData = str(self.ID) + '\n' + str(self.password) + '\n' + str(self.tooken)
            file.write(userData)
            file.close()


    def getUserID(self):
        return self.ID

    def setUserID(self, ID):
        self.ID = ID
        file = open("userData.json", "w")
        userData = str(self.ID) + '\n' + str(self.password) + '\n' + str(self.tooken)
        file.write(userData)
        file.close()
        return 0

    def getUserPassword(self):
        return self.password

    def setUserPassword(self, password):
        self.password = password
        file = open("userData.json", "w")
        userData = str(self.ID) + '\n' + str(self.password) + '\n' + str(self.tooken)
        file.write(userData)
        file.close()
        return 0

    # Reset user ID and password
    def delUser(self):
        self.ID = "[]"
        self.password = "[]"
        file = open("userData.json", "w")
        userData = str(self.ID) + '\n' + str(self.password) + '\n' + str(self.tooken)
        file.write(userData)
        file.close()
        return 0

    def getTooken(self):
        return self.tooken

    def delTooken(self):
        self.tooken = "[]"
        file = open("userData.json", "w")
        userData = str(self.ID) + '\n' + str(self.password) + '\n' + str(self.tooken)
        file.write(userData)
        file.close()
        return 0

    # Generate new tooken and save it
    def refreshTooken(self):
        self.tooken = uuid4().hex
        file = open("userData.json", "w")
        userData = str(self.ID) + '\n' + str(self.password) + '\n' + str(self.tooken)
        file.write(userData)
        file.close()
        return 0



