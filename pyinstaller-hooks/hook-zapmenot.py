# pyinstaller-hooks/hook-zapmenot.py
from PyInstaller.utils.hooks import collect_submodules, collect_data_files
hiddenimports = collect_submodules('zapmenot')
datas = collect_data_files('zapmenot')
