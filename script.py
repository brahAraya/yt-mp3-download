import os
import tkinter as tk
from tkinter import ttk, filedialog
from typing import Dict, Any
import yt_dlp

PLAYLIST_URL_PARAM = '&list'

def download_mp3(url: str, audio_format: str, audio_quality: str) -> None:
    sanitized_url = remove_playlist_param(url)
    download_path = ask_for_download_path()
    if not download_path:
        print('No download folder selected. Aborting download.')
        return
    if not os.path.exists(download_path):
        print('Download path does not exist. Aborting download.')
        return
    options: Dict[str, Any] = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': audio_format,
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': audio_format,
                'preferredquality': audio_quality,
            }
        ],
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            print(f'Downloading audio file from video: {sanitized_url}')
            ydl.download([sanitized_url])
            print('Download completed.')
        except yt_dlp.utils.DownloadError as e:
            print(f'Error downloading audio file: {e}')
        except Exception as e:
            print(f'Unexpected error: {e}')

def remove_playlist_param(url: str) -> str:
    return url.split(PLAYLIST_URL_PARAM)[0] if PLAYLIST_URL_PARAM in url else url

def draw_main_window() -> None:
    root = tk.Tk()
    root.title('Youtube Audio Downloader')
    root.geometry('400x250+100+100')
    label = tk.Label(root, text='Paste the video URL:', font=('Arial', 11))
    label.pack(pady=10)
    url_entry = tk.Entry(root, width=40)
    url_entry.pack(pady=5)
    label_format = tk.Label(root, text='Select Audio Format:', font=('Arial', 10))
    label_format.pack(pady=5)
    formats = ['mp3', 'wav', 'aac']
    format_var = tk.StringVar(value=formats[0])
    format_menu = ttk.Combobox(root, textvariable=format_var, values=formats)
    format_menu.pack(pady=5)
    label_quality = tk.Label(root, text='Select Audio Quality:', font=('Arial', 10))
    label_quality.pack(pady=5)
    qualities = ['128', '192', '320']
    quality_var = tk.StringVar(value=qualities[2])
    quality_menu = ttk.Combobox(root, textvariable=quality_var, values=qualities)
    quality_menu.pack(pady=5)
    def submit_url():
        url = url_entry.get()
        audio_format = format_var.get()
        audio_quality = quality_var.get()
        download_mp3(url, audio_format, audio_quality)
    submit_button = tk.Button(root, text='Download', command=submit_url)
    submit_button.pack(pady=10)
    root.mainloop()

def ask_for_download_path() -> str:
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title='Select Download Path')
    return folder_selected

if __name__ == '__main__':
    draw_main_window()
