from cx_Freeze import setup, Executable

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI"

include_files = {'include_files': 'windows/pictures'}
setup(
    name="Pandapp",
    version="1.1",
    description="Pc remote controller software",
    options={'build_exe': include_files},
    executables=[Executable("windows/Pandapp.py", base=base, icon="windows/pictures/pandapp.ico")],
)
