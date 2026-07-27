# -*- mode: python ; coding: utf-8 -*-
#
# PyInstaller spec for SE Audio Converter — ONEDIR build.
#
# Onedir (not onefile): the DLLs live in the install folder instead of being
# unpacked to %TEMP% on every launch. A onefile exe is a single self-extracting
# blob that trips Windows Defender's packer heuristic (false-positive "virus")
# and races Defender on the temp extraction; onedir avoids both. The Inno
# installer packages the whole dist\SE Audio Converter\ folder.
#
# Build:  pyinstaller SE_Audio_Converter.spec   (or run build.bat)

from PyInstaller.utils.hooks import collect_all

# Bundle numpy (Audio Editor DSP) and sounddevice (playback + its portaudio DLL)
np_datas, np_binaries, np_hiddenimports = collect_all("numpy")
sd_datas, sd_binaries, sd_hiddenimports = collect_all("sounddevice")

a = Analysis(
    ["se_audio_launcher.py"],
    pathex=[],
    binaries=np_binaries + sd_binaries,
    datas=np_datas + sd_datas + [("VERSION", ".")],
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
    exclude_binaries=True,        # onedir: binaries go into the COLLECT folder
    name="SE Audio Converter",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,      # no console window — GUI only
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="icon.ico",
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="SE Audio Converter",
)
