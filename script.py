from typing import Dict, Any
import yt_dlp

PLAYLIST_URL_PARAM = '&list'

def download_mp3(url: str) -> None:
    sanitized_url = remove_playlist_param(url)
    options: Dict[str, Any] = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }
        ],
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            print(f"Downloading audio file from video: {sanitized_url}")
            ydl.download([sanitized_url])
            print("Download completed.")
        except Exception as e:
            print(f"Error downloading audio file: {e}")

def remove_playlist_param(url: str) -> str:
    return url.split(PLAYLIST_URL_PARAM)[0] if PLAYLIST_URL_PARAM in url else url

if __name__ == "__main__":
    video_url: str = input("Paste the video URL: ")
    download_mp3(video_url)