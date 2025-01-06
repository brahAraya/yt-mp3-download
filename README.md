# YouTube Audio Downloader

This is a **Linux-only** YouTube audio downloader that uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [tkinter](https://docs.python.org/3/library/tkinter.html) to handle its user interface.

### Requirements:

- tkinter *(This command is for debian-derived distros only, check your distro installation process)*
```shell
foo@bar:~$ sudo apt-get install python3-tk
```

## Windows compatibility

To run this program on windows, you must clone this repo in a [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) environment and run it from the terminal. You can also create a batch file to directly run the Python script with a simple double clic of a file:

### example-with-venv.bat
```batch
@echo off
wsl --exec bash -c "source /home/user/.../yt-download/venv/bin/activate && python3 /home/user/.../yt-download/script.py"
```

### example-without-venv.bat
```batch
@echo off
wsl --exec bash -c "python3 /home/user/.../yt-download/script.py"
```
