import re

def getVideoIdFromUrl(videoUrl : str) :
    VIDEO_ID_PATTERN = '(?:watch\?v=|be\/)([\w-]{11})'
    videoId = re.search(VIDEO_ID_PATTERN,videoUrl).group(1)
    return videoId
