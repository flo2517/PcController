import platform

from pc.TookenGenerator import TookenGenerator
from pc.Executors import WinExe, MacExe, LinuxExe


class Launcher:
    def __init__(self):
        # Set tooken
        self.tooken = TookenGenerator()

        # Set command executor depending on the system
        if "Windows" == platform.system():
            self.osExecutor = WinExe()
        elif "Linux" == platform.system():
            self.osExecutor = LinuxExe()
        else:
            self.osExecutor = MacExe()

        # Init commandID to 0
        # commandID 0 -> no command
        self.commandID = 0

    def receiveCommand(self):
        self.commandID = 1

    def execute(self):
        # Launch command using executor
        self.osExecutor.exe(self.commandID)

    def executeManual(self, commandID):
        self.osExecutor.exe(commandID)
