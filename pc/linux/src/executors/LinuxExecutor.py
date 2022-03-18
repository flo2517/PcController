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
            os.system("shutdown -h now")
            return 0
        elif commandID == 2:
            test = os.system("amixer -D pulse sset Master 10%+")
            print(test)
            return 0
        elif commandID == 3:
            os.system("amixer -D pulse sset Master 10%-")
            return 0
        elif commandID == 4:
            os.system("amixer -D pulse sset Master 0%")
            return 0
        elif commandID == 5:
            os.system("playerctl play-pause")
            return 0
        elif commandID == 6:
            os.system("playerctl pause")
            return 0
        elif commandID == 7:
            os.system("xdotool key super+l")
            return 0
        elif commandID == 8:
            os.system("playerctl next")
            return 0
        elif commandID == 9:
            os.system("playerctl previous")
            return 0
        elif commandID == 10:
            os.system("xdotool key Left")
            return 0
        elif commandID == 11:
            os.system("xdotool key Right")
            return 0
        elif commandID == 12:
            os.system("xdotool key Up")
            return 0
        elif commandID == 13:
            os.system("xdotool key Down")
            return 0
        else:
            print("Command not found")
        return 1

