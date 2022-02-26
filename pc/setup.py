from cx_Freeze import setup, Executable
import sys



setup(
    name="Premote",
    version="1.0",
    description="Pc remote controller software",
    executables=[Executable("Main.py", base=None)],
)

if sys.platform == "win32":
    packages = ["os", "requests", "tk", "pillow", "json", "uuid", "python-socketio", "pystray", "sys", "re",
                "threading", "multiprocessing", "pycryptodome", "PyAutoGui"]
    build_exe_options = {"packages": packages, "excludes": [""]}
    setup(
        name="Premote",
        version="1.0",
        description="Pc remote controller software",
        options={"build_exe": build_exe_options},
        executables=[Executable("Main.py", base="Win32GUI")],
    )


