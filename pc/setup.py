from cx_Freeze import setup, Executable
import sys

packages = ["requests", "tk", "PIL", "json", "uuid", "socketio", "pystray", "threading", "multiprocessing", "pycryptodome"]
build_exe_options = {"packages": packages, "excludes": []}


# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    packages.append("PyAutoGui")
    base = "Win32GUI"


setup(
    name="Premote",
    version="1.0",
    description="Pc remote controller software",
    options={"build_exe": build_exe_options},
    executables=[Executable("Main.py", base=base)],
)
