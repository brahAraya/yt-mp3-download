# YouTube Audio Downloader

This is a **linux-only** YouTube audio downloader that uses [tkinter](https://docs.python.org/3/library/tkinter.html) to handle the user interface.

## Windows compatibility

To run this program on windows, you must clone this repo in a [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) environment and run it from the terminal. You can also create a batch file to directly run the Python script with a simple double clic of a file:

### example-with-venv.bat
`@echo off`
`wsl --exec bash -c "source /home/user/.../yt-download/venv/bin/activate && python3 /home/brah/dev/yt-download/script.py"`

### example-without-venv.bat
`@echo off`
`wsl --exec bash -c "python3 /home/user/.../yt-download/script.py"`
