from uuid import uuid4
import os


class TookenGenerator:

    def __init__(self):
        # Check if there is a tooken already created
        if os.path.isfile("tooken.txt"):
            print("There is already a tooken")
            # Take the tooken
            self.file = open("tooken.txt", "r")
            self.tooken = self.file.read()
            self.file.close()
            print(self.tooken)
        else:
            # Create and save the tooken
            print("Creating tooken")
            # Generate the tooken
            self.tooken = uuid4().hex
            # Create file and save the tooken
            self.file = open("tooken.txt", "w")
            self.file.write(self.tooken)
            self.file.close()
            print(self.tooken)


