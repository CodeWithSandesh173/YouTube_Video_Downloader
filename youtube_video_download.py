import yt_dlp #pip install yt_dlp

# URL of the video you want to download
video_url = input("Enter video url")

# Options for downloading
ydl_opts = {
    'format': 'best',   # download best quality
    'outtmpl': '%(title)s.%(ext)s',  # save file with video title
}

# Download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
