# -*- mode: python ; coding: utf-8 -*-
#
# PyInstaller spec for SE Audio Converter
#
# Build with:
#   pyinstaller SE_Audio_Converter.spec
#
# Output: dist/SE Audio Converter.exe

from PyInstaller.utils.hooks import collect_all

# Bundle numpy (Audio Editor DSP) and sounddevice (playback + its portaudio DLL)
np_datas, np_binaries, np_hiddenimports = collect_all("numpy")
sd_datas, sd_binaries, sd_hiddenimports = collect_all("sounddevice")

a = Analysis(
    ["se_audio_launcher.py"],
    pathex=[],
    binaries=np_binaries + sd_binaries,
    datas=np_datas + sd_datas,
    hiddenimports=np_hiddenimports + sd_hiddenimports + [
        # Screen modules loaded lazily by string name
        "screen_audio_home",
        "screen_audio_setup",
        "screen_audio_converter",
        "screen_audio_editor",
        "screen_audio_sbc",
        # Theme and shared modules
        "se_audio_theme",
        # sounddevice's CFFI backend
        "_cffi_backend",
        # stdlib modules used at runtime
        "wave",
        "xml.etree.ElementTree",
        "tkinter",
        "tkinter.ttk",
        "tkinter.filedialog",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["pygame"],   # not used; a stale reference only
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="SE Audio Converter",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    icon="icon.ico",
    console=False,      # no console window — GUI only
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
