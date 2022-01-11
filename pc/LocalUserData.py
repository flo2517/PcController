from uuid import uuid4


class LocalUserData:

    def __init__(self):
        # Get data of data user file
        file = open("userData.json", "r")
        data = file.read()
        index = 0
        for char in data:
            if index == 0:
                self.userID.append(char)
            elif index == 1:
                self.userPassword.append(char)
            elif index == 2:
                self.tooken.append(char)
            if char == ']':
                index += 1

        self.userID = ''.join(self.userID)
        self.userPassword = ''.join(self.userPassword)
        file.close()

        if index != 3:
            file = open("userData.json", "w")
            # Create and save the tooken
            print("Creating tooken")
            # Generate the tooken
            self.tooken = '[', uuid4().hex, ']'
            file.write(self.userID, '', self.userPassword, '', self.tooken)
            file.close()
        else:
            self.tooken = ''.join(self.tooken)

    def setUser(self, userID, userPassword):
        self.userID = userID
        self.userPassword = userPassword
        file = open("userData.json", "w")
        file.write(self.userID, '', self.userPassword, '', self.tooken)
        file.close()
        return 0

    def delUser(self):
        self.userID = "[]"
        self.userPassword = "[]"
        file = open("userData.json", "w")
        file.write(self.userID, '', self.userPassword, '', self.tooken)
        file.close()
        return 0

    def getTooken(self):
        return self.tooken

    def getUserID(self):
        return self.userID

    def refreshTooken(self):
        self.tooken = '[', uuid4().hex, ']'
        file = open("userData.json", "w")
        file.write(self.userID, '', self.userPassword, '', self.tooken)
        file.close()
        return 0

    def getUserPassword(self):
        return self.userPassword

