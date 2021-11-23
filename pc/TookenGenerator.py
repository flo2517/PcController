from uuid import uuid4
import os


class TookenGenerator:

    def __init__(self):
        # Check if there is a tooken already created
        if os.path.isfile("tooken.txt"):
            print("There is already a tooken")
            # Take the tooken
            file = open("tooken.txt", "r")
            self.tooken = file.read()
            file.close()
            print(self.tooken)
        else:
            # Create and save the tooken
            print("Creating tooken")
            # Generate the tooken
            self.tooken = uuid4().hex
            # Create file and save the tooken
            file = open("tooken.txt", "w")
            file.write(self.tooken)
            file.close()
            print(self.tooken)

    def getTooken(self):
        file = open("tooken.txt", "r")
        tooken = file.read()
        file.close()
        return tooken

