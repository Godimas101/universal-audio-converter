# Changelog

All notable changes to SE Universal Audio Converter. Format follows [Keep a Changelog](https://keepachangelog.com/).

## [1.2.1] — 2026-07-25

### Fixed
- Audio Editor: **Space now reliably plays and pauses** from anywhere in the editor. A focused button (like OPEN) used to swallow the spacebar — so Space would re-open dialogs or only work after clicking Play. Space is now play/pause throughout, and pausing keeps your place so the next press resumes instead of restarting. The edit log shows where you paused and resumed from.

## [1.2.0] — 2026-07-25

A big look-and-feel and usability refresh. Same tools, same colours — cleaner type, real keyboard shortcuts, and clearer feedback.

### Changed
- Refreshed the whole interface to the modernised SE-tool style: a clean sans typeface for headings, labels and buttons, with monospace kept where it earns its place — logs, file lists, specs and the SBC XML output. The colour palette is unchanged.
- Convert / Generate now stays disabled until it can actually run, and shows a working state while it's busy.
- The "ⓘ" help button now sits in every screen's header, next to Back, and lists that screen's keyboard shortcuts.

### Added
- Keyboard shortcuts throughout — including **Space to play/pause** and **Ctrl+Z to undo** in the Audio Editor, Ctrl+O to add files, Enter to convert, digit keys (1–4) to jump between screens from the home page, Esc to go back, and F1 for help.
- A visible focus ring so keyboard navigation is easy to follow.
- A "Found a bug? Report it" link on the home screen.

### Fixed
- Conversions now time out instead of freezing the app if ffmpeg or xWMAEncode gets stuck, and report clearer errors.
- The audio preview button no longer trips over rapid play/stop clicks.

## [1.1] — 2026-04-03

- Earlier release (Audio Converter, Editor and SBC Generator).
