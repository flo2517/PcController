from cx_Freeze import setup, Executable
import sys

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

include_files = {'include_files': 'pictures'}
setup(
    name="Pandapp",
    version="1.0",
    description="Pc remote controller software",
    options={'build_exe': include_files},
    executables=[Executable("linux/Pandapp.py", base=base, icon="/home/pandapp/Documents/DEV/Pandapp/pc/pictures/pandapp.ico")],
)
