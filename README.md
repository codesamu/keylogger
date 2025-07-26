# Keylogger

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

A simple Python keylogger that records keystrokes to a file using the `pynput` library.

## Features

- Logs all keystrokes (including special keys) to `chars.txt`
- Prints each key press to the console
- Cross-platform (Linux, Windows, macOS)

## Requirements

- Python 3.6+
- `pynput` library

Install dependencies:
```bash
pip install pynput
```

## Usage

```bash
python keylogger.py
```

- All keystrokes will be appended to `chars.txt` in the current directory.
- To stop the keylogger, interrupt the process (Ctrl+C).

## Disclaimer

This tool is for educational purposes only. Do **not** use it on systems without explicit permission.
