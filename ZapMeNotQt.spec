# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/ZapMeNotQt/ZapMeNotQt.py'],
    pathex=['src/ZapMeNotQt'],
    binaries=[],
    datas=[
            ('src/ZapMeNotQt/ui/ActivitiesDialog.ui', 'ui'),
            ('src/ZapMeNotQt/ui/DetectorLocationDialog.ui', 'ui'),
            ('src/ZapMeNotQt/ui/GenericShieldDialog.ui', 'ui'),
            ('src/ZapMeNotQt/ui/IsotopeSelector.ui', 'ui'),
            ('src/ZapMeNotQt/ui/MainWindow.ui', 'ui'),
            ('src/ZapMeNotQt/ui/OptionsBuildupDialog.ui', 'ui'),
            ('src/ZapMeNotQt/ui/OptionsFillerDialog.ui', 'ui'),
            ('src/ZapMeNotQt/ui/OptionsGroupsDialog.ui', 'ui'),
            ('src/ZapMeNotQt/ui/OptionsProgenyDialog.ui', 'ui'),
            ('src/ZapMeNotQt/ui/OptionsQuadratureDialog.ui', 'ui'),
            ('src/ZapMeNotQt/ui/PhotonsDialog.ui', 'ui'),
            ('src/ZapMeNotQt/ui/RemoveShieldDialog.ui', 'ui'),
            ('src/ZapMeNotQt/ui/script_display.ui', 'ui') ],
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
