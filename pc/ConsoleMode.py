import sys

from pc.Launcher import Launcher


class ConsoleMode:

    def __init__(self):
        self.launcher = Launcher()
        self.run = True
        while self.run:
            self.printMenu()




    def printMenu(self):
        print("Choose what you want to do")
        print("\t-1 Show tooken")
        print("\t-2 Execute command")
        print("\t-3 Exit")
        choice = input()
        while choice != '1' and choice != '2' and choice != '3':
            print("Input error, enter 1, 2 or 3")
            choice = input()
        if choice == '1':
            # Show tooken
            print(self.launcher.tooken.getTooken())
        elif choice == '2':
            # Execute command
            self.commandExecutor()
        else:
            self.run = False
            return


    def commandExecutor(self):
        print("\t\t-1 Enter command id")
        print("\t\t-2 Show command documentation")
        choice = input()
        while choice != '1' and choice != '2':
            print("Input error, enter 1 or 2")
            choice = input()
        if choice == '1':
            # enter command id and execute it
            print("\t\tPlease enter command id :")
            id = input()
            # Execute it
            self.launcher.executeManual(int(id))
        else:
            # Show command manual
            file = open("../Documentation/Command_id.txt", "r")
            print(file.read())
            file.close()
