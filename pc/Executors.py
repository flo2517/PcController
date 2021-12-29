import os
import pyautogui

class WinExe:
    def __init__(self):
        print("Executing by WinExe")
        return

    def exe(self, commandID):
        # Execute command corresponding to id
        print("CommadID = ", commandID)
        if commandID == 0:
            return
        elif commandID == 1:
            os.system("shutdown -s -t 1")
        elif commandID == 2:
            pyautogui.press("volumeup")
        elif commandID == 3:
            pyautogui.press("volumedown")
        elif commandID == 4:
            pyautogui.press("volumemute")
        elif commandID == 5:
            pyautogui.press("playpause")
        elif commandID == 6:
            pyautogui.press("pause")
        elif commandID == 7:
            print("Command to lock PC is comming soon")
        else:
            print("Command not found")
        return


class LinuxExe:
    def __init__(self):
        print("Executing by LinuxExe")
        return

    def exe(self, commandID):
        # Execute command corresponding to id
        print(commandID)
        return


class MacExe:
    def __init__(self):
        print("Executing by MacExe")
        return

    def exe(self, commandID):
        # Execute command corresponding to id
        print(commandID)
        return
