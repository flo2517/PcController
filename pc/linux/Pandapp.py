from src.Launcher import Launcher
from multiprocessing import freeze_support

freeze_support()
restart = True
while restart:
    restart = False
    app = Launcher()
    restart = app.getRestartValue()
