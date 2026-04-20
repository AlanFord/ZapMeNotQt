# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/ZapMeNotQt/ZapMeNotQt.py'],
    pathex=['src/ZapMeNotQt'],
    binaries=[],
    hiddenimports=[],
    hookspath=['./pyinstaller-hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['pyvista'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ZapMeNotQt',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ZapMeNotQt',
)
