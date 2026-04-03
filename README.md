<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=170&color=0:1F2937,45:D97706,100:F59E0B&text=Universal%20Audio%20Converter&fontColor=ffffff&fontAlignY=35&fontSize=32&desc=Space%20Engineers%20audio%20conversion,%20editing,%20and%20SBC%20prep&descAlignY=57&descSize=18" />
</p>

> **"Because audio modding is already weird enough without fighting file formats, sample rates, and surprise stereo issues."**

A Windows toolset for the full Space Engineers audio workflow: convert sounds, clean them up, and generate the SBC files needed to actually use them in-game. It’s built for the very common journey from “random sound effect on disk” to “working mod asset that doesn’t explode on contact.”

If you just want the app, grab the latest build from the [GitHub Releases page](https://github.com/Godimas101/universal-audio-converter/releases).

## 🚀 Quick Start

1. Download `SE Audio Converter.exe` from Releases
2. Place `ffmpeg.exe` next to it
3. Add `xWMAEncode.exe` too if you want `.xwm` output
4. Use the built-in tools to convert, edit, and generate `Audio.sbc` / `SoundBlock.sbc`

![SE Audio Converter screenshot](audio_converter.png)

## ✨ Features

| Feature | What it does |
|--------|---------------|
| **Audio Converter** | Converts common formats to `WAV` or `XWM` |
| **Audio Editor** | Lets you trim, fade, normalize, and fix channels visually |
| **SBC Generator** | Builds `Audio.sbc` and `SoundBlock.sbc` output for SE mods |
| **Dependency checker** | Helps you find what’s missing before you start yelling at the toolchain |

## 🔧 Setup

### `ffmpeg`
Required for the **Audio Converter** and general format conversion.

1. Download a Windows build from [ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract it and find `ffmpeg.exe` inside the `bin/` folder
3. Place `ffmpeg.exe` next to `SE Audio Converter.exe` or add it to your system `PATH`

### `xWMAEncode`
Required **only** if you want `XWM` output.

The easiest source is the **Space Engineers Mod SDK**:

```text
[Steam library]\steamapps\common\SpaceEngineersModSDK\Tools\xWMAEncode.exe
```

Copy `xWMAEncode.exe` next to the app or add its folder to `PATH`.

> No Mod SDK installed? You can also get it from the **DirectX SDK (June 2010)** at [archive.org/details/dxsdk_2010](https://archive.org/details/dxsdk_2010) under `Utilities\bin\x86\`.

### Source dependencies
If you're running the Python version instead of the packaged exe:

```bash
pip install -r requirements.txt
```

---

## 🎚️ Audio Converter

### Quick workflow
1. Click **SELECT** and choose your audio files
2. Set **Output Format** to `WAV` or `XWM`
3. Optionally set a prefix, suffix, and output folder
4. Click **▶ CONVERT ▶**

### Supported input formats

| Format | Extension |
|--------|-----------|
| MP3 | `.mp3` |
| WAV | `.wav` |
| OGG | `.ogg` |
| FLAC | `.flac` |
| AAC | `.aac` |
| M4A | `.m4a` |
| WMA | `.wma` |
| AIFF | `.aiff`, `.aif` |
| Opus | `.opus` |
| XWM | `.xwm` |

### XWM output pipeline
When `XWM` is selected, the tool automatically:

1. uses `ffmpeg` to convert the source file to **16-bit PCM WAV at 44100 Hz**
2. feeds that WAV into `xWMAEncode` to produce the final `.xwm`

The intermediate WAV is created in a temp location and cleaned up automatically.

---

## ✂️ Audio Editor

### Quick workflow
1. Click **OPEN WAV**
2. Drag on the waveform to create a selection
3. Apply edits like trim, fades, normalize, channel changes, or speed adjustments
4. Save over the file or use **SAVE AS...**

### Selection controls

| Action | Result |
|--------|--------|
| Click + drag on empty space | Create a selection |
| Drag a handle | Resize the selection |
| Drag inside the selection | Move it |
| **SELECT ALL** | Select the whole file |

### Edit tools

| Tool | What it does |
|------|--------------|
| **TRIM** | Keeps only the selected audio |
| **SILENCE** | Replaces the selection with silence |
| **REVERSE** | Reverses the selected region |
| **NORMALIZE** | Brings the loudest peak up to 0 dBFS |
| **DC OFFSET** | Removes DC bias from recordings |
| **GAIN** | Applies a simple volume multiplier |
| **FADE IN / OUT** | Smoothly ramps the selection in or out |
| **STEREO→MONO** | Mixes stereo down to mono |
| **MONO→STEREO** | Duplicates mono to both channels |
| **SWAP / EXTRACT / SOLO** | Useful for channel cleanup and sanity restoration |

### Playback
When running from source with the playback dependencies installed, the editor can preview the whole file or just the selected range.

---

## 📄 SBC Generator

### Quick workflow
1. Click **ADD FILES**
2. Select your `.wav` or `.xwm` files
3. Set fields like `SubtypeId`, `Category`, `Wave Type`, and loop behavior
4. Click **▶▶ GENERATE SBC ▶▶**
5. Copy or save the generated `Audio.sbc` and `SoundBlock.sbc`

### Key settings

| Setting | Notes |
|---------|-------|
| `SubtypeId` | Unique ID for the sound definition |
| `Category` | `Sb` for Sound Blocks, `Music` for music, others for event use |
| `Wave Type` | `D2` for non-positional audio, `D3` for 3D positional audio |
| `Volume` | `1.0` keeps original volume |
| `Max Distance` | Mainly relevant for `D3` sounds |
| `Loop Type` | None / Simple Loop / Start + Loop + End |
| `Stream Sound` | Useful for longer tracks |
| `SB Category ID` | Groups sounds in Sound Blocks |

### Example mod structure

```text
MyMod/
  Data/
    Audio.sbc
    SoundBlock.sbc
  Audio/
    MySound.xwm
```

### Example `Audio.sbc`

```xml
<?xml version="1.0"?>
<Definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <Sounds>
    <Sound>
      <Id>
        <TypeId>MyObjectBuilder_AudioDefinition</TypeId>
        <SubtypeId>MyModSound</SubtypeId>
      </Id>
      <Category>Sb</Category>
      <MaxDistance>200</MaxDistance>
      <Volume>1.0</Volume>
      <Waves>
        <Wave Type="D2">
          <Loop>Audio\MySound.xwm</Loop>
        </Wave>
      </Waves>
      <StreamSound>false</StreamSound>
    </Sound>
  </Sounds>
</Definitions>
```

## 📁 Project Files

| File | Purpose |
|------|---------|
| `se_audio_launcher.py` | Main launcher for the Python version |
| `screen_audio_*.py` | UI screens for conversion, editing, setup, and SBC generation |
| `se_audio_theme.py` | Shared theme and UI styling |
| `build.bat` | Build helper for the packaged executable |
| `requirements.txt` | Source dependencies |

## 📝 Notes

- Sound Block audio in Space Engineers should generally be **mono**
- if you leave source audio stereo, the game will usually only play the left channel
- if `xWMAEncode.exe` isn’t available, the tool can still handle WAV work just fine

## 🐍 Running from Source

```bash
pip install -r requirements.txt
python se_audio_launcher.py
```

Requires **Python 3.8+**.

## 🏗️ Building the EXE

```bash
build.bat
```

Output:
```text
dist\SE Audio Converter.exe
```

## 🙌 Credits

Made with ♥ by **Godimas** and **Claude**.

Audio format details were cross-checked against Space Engineers files and the DirectX SDK tooling.

## 🧡 Support

This tool is free and always will be. If it saves you time on your next sound pass, consider supporting on Patreon — it helps keep the tools and mods coming.

[![Support on Patreon](https://raw.githubusercontent.com/Godimas101/personal-projects/main/patreon/images/buttons/patreon-medium.png)](https://patreon.com/Godimas101)

*Keep it mono, keep it clean, and try not to summon clipping demons.* 🎵
