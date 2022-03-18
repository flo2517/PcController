from datetime import datetime as date
from src.executors.LinuxExecutor import LinuxExe

class Executor:
    def __init__(self):
        self.commandID = 0
        self.osExecutor = LinuxExe()

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
