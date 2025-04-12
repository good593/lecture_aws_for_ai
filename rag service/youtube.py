from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter, TextFormatter

import yt_dlp

channel_url = "https://www.youtube.com/@%ED%95%98%EC%A0%95%ED%9B%88%EC%9D%98%EC%82%90%EB%BD%80%EC%82%90%EB%BD%80119%EC%86%8C/videos"


def get_video_urls(channel_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'playlistend': 1000,  # Limit to first 1000 videos
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        
        if 'entries' in info:
            video_urls = [entry['url'] for entry in info['entries'] if 'url' in entry]
            return video_urls


def get_youtube_video_info(video_url):
    ydl_opts = {
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        return {
            "video_id": video_info['id'],
            "title": video_info['title'],
            "upload_date": video_info['upload_date'],
            "channel": video_info['channel'],
            "duration": video_info['duration_string'],
            "caption": get_youtube_video_transcript(video_info['id'])
        }
    
def get_youtube_video_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko'])
    return " ".join(line['text'] for line in transcript)

