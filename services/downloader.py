import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

import warnings 
warnings.filterwarnings("ignore")

def transcribeVideoOrchestrator(youtube_url: str, output_directory = "videos"):

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    video = downloadYoutubeVideo(youtube_url, output_directory)
    if video and os.path.exists(video['path']):
        print("Download Complete")
        return "Download Complete"
    else:
        return "Failed to download video or video file does not exist."

def downloadYoutubeVideo(youtube_url: str, directory: str) -> dict:
    try:
        print(f"Processing: {youtube_url}")
        yt = YouTube(youtube_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if stream:
            file_path = stream.download(output_path=directory)
            print(f"Download complete: {file_path}")
            return {"name": yt.title, "thumbnail": yt.thumbnail_url, "path": file_path}
        else:
            print("No suitable stream found.")
            return None
    except VideoUnavailable:
        print("Video is unavailable.")
        return None
    except Exception as e:
        print(f"An error occurred during video download: {str(e)}")
        return None
