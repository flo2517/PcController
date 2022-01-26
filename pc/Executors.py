import os
import pyautogui
import platform
from datetime import datetime as date


class Executor:
    def __init__(self):
        self.osName = platform.system
        self.commandID = 0

        if "Windows" == platform.system():
            self.osExecutor = WinExe()
        elif "Linux" == platform.system():
            self.osExecutor = LinuxExe()
        else:
            self.osExecutor = MacExe()
        return

    def execute(self, commandID):
        res = self.osExecutor.exe(commandID)
        # Save in log file
        file = open("commandHistory.log", "a")
        now = date.now().strftime("%b-%d-%Y, %H:%M:%S | ")
        if res == 1:
            file.write(now+"Can't find command number "+str(commandID)+"\n")
        else:
            file.write(now+"Command number "+str(commandID)+" is executed\n")
        file.close()
        return


class WinExe:
    def __init__(self):
        print("Executing by WinExe")
        return

    @staticmethod
    def exe(commandID):
        # Execute command corresponding to id
        print("CommadID = ", commandID)
        if commandID == 0:
            return 0
        elif commandID == 1:
            os.system("shutdown -s -t 1")
            return 0
        elif commandID == 2:
            pyautogui.press("volumeup")
            return 0
        elif commandID == 3:
            pyautogui.press("volumedown")
            return 0
        elif commandID == 4:
            pyautogui.press("volumemute")
            return 0
        elif commandID == 5:
            pyautogui.press("playpause")
            return 0
        elif commandID == 6:
            pyautogui.press("pause")
            return 0
        elif commandID == 7:
            print("Command to lock PC is coming soon")
            return 0
        else:
            print("Command not found")
        return 1


class LinuxExe:
    def __init__(self):
        print("Executing by LinuxExe")
        return

    @staticmethod
    def exe(commandID):
        # Execute command corresponding to id
        print(commandID)
        return 1


class MacExe:
    def __init__(self):
        print("Executing by MacExe")
        return

    @staticmethod
    def exe(commandID):
        # Execute command corresponding to id
        print(commandID)
        return 1
