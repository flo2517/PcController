from src.Launcher import Launcher

restart = True
while restart:
    restart = False
    app = Launcher()
    restart = app.getRestartValue()
