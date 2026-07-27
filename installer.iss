; Version is supplied by the build (CI + build.bat pass it from the VERSION
; file):  ISCC /DAppVer=1.2.3 installer.iss  — falls back to the default below.
#ifndef AppVer
  #define AppVer "1.3.0"
#endif

[Setup]
AppName=SE Audio Converter
AppVersion={#AppVer}
AppPublisher=Godimas
AppPublisherURL=https://patreon.com/Godimas101
AppSupportURL=https://github.com/Godimas101/universal-audio-converter
DefaultDirName={localappdata}\SEAudioConverter
DefaultGroupName=SE Audio Converter
DisableProgramGroupPage=yes
OutputDir=installer
OutputBaseFilename=SEAudioConverterSetup-v{#AppVer}
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\SE Audio Converter.exe
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
; Onedir build: package the whole PyInstaller output folder (exe + _internal).
Source: "dist\SE Audio Converter\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\SE Audio Converter"; Filename: "{app}\SE Audio Converter.exe"
Name: "{group}\Uninstall SE Audio Converter"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\SE Audio Converter.exe"; Description: "Launch SE Audio Converter now"; Flags: nowait postinstall skipifsilent
