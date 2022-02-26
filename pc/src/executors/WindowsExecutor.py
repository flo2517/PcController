import os


class WinExe:
    def __init__(self):
        print("Executing by WinExe")
        return

    @staticmethod
    def exe(commandID):
        import pyautogui
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
            os.system('rundll32.exe user32.dll,LockWorkStation')
            return 0
        elif commandID == 8:
            pyautogui.press("nexttrack")
            return 0
        elif commandID == 9:
            pyautogui.press("prevtrack")
            return 0
        else:
            print("Command not found")
        return 1
