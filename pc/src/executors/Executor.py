import platform
from datetime import datetime as date
from pc.src.executors.LinuxExecutor import LinuxExe
from pc.src.executors.MacExecutor import MacExe
from pc.src.executors.WindowsExecutor import WinExe


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