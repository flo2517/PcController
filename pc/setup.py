from cx_Freeze import setup, Executable
import sys

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

include_files = {'include_files': 'pictures'}
setup(
    name="Premote",
    version="1.0",
    description="Pc remote controller software",
    options={'build_exe': include_files},
    executables=[Executable("Premote.py", base=base, icon="pictures/premote.ico")],
)
