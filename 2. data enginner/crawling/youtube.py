from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter, TextFormatter

def get_video_id(video_url):
    video_id = video_url.split('v=')[1][:11]
    return video_id

video_url = 'https://www.youtube.com/watch?v=CyEsljuyEW8'
video_id = get_video_id(video_url)