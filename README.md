> **I created this for fun and personal use, not for mass distribution, so it might not be ideal for your use case.**

# YouTube Audio Downloader
This is a **Linux-only** YouTube audio downloader that uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [tkinter](https://docs.python.org/3/library/tkinter.html) for its user interface.

### Requirements
- tkinter *(This command is for Debian-based distros only; check your distro’s installation process for others)*
```shell
sudo apt-get install python3-tk
```

### How to Run
Just like running any other Python file:
```shell
python3 script.py
```

## Windows Compatibility
To run this on Windows, you must clone this repo in a [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) environment and execute it from the terminal. You can also create a batch file to directly run the Python script with a simple double-click:

### example-without-venv.bat
```batch
@echo off
wsl --exec bash -c "python3 /home/user/.../yt-mp3-download/script.py"
```

### example-with-venv.bat
```batch
@echo off
wsl --exec bash -c "source /home/user/.../yt-mp3-download/venv/bin/activate && python3 /home/user/.../yt-mp3-download/script.py"
```
