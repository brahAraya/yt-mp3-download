import yt_dlp

def download_mp3(url):
    options = {
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
            print(f"Downloading audio file from video: {url}")
            ydl.download([url])
            print("Download completed.")
        except Exception as e:
            print(f"Error downloading audio file: {e}")


url_video = input("Paste the video URL: ")

download_mp3(url_video)
