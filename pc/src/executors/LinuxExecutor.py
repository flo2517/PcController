import os


class LinuxExe:
    def __init__(self):
        print("Executing by LinuxExe")
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
            os.system("playerctl volume 10%+")
            return 0
        elif commandID == 3:
            os.system("playerctl volume 10%+")
            return 0
        elif commandID == 4:
            os.system("playerctl volume 0%")
            return 0
        elif commandID == 5:
            os.system("playerctl play-pause")
            return 0
        elif commandID == 6:
            os.system("playerctl pause")
            return 0
        elif commandID == 7:
            os.system("gnome-screensaver-command -l")
            return 0
        elif commandID == 8:
            os.system("playerctl next")
            return 0
        elif commandID == 9:
            os.system("playerctl previous")
            return 0
        else:
            print("Command not found")
        return 1

