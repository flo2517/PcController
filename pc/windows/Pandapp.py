from src.Launcher import Launcher

def main():
    restart = True
    while restart:
        restart = False
        app = Launcher()
        restart = app.getRestartValue()

if __name__ == "__main__":
    main()
