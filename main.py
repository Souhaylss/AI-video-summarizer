import re;


def getIdFromUrl(videoUrl)  : 
    VIDEO_ID_REGEX =  '(?:v=|/)([0-9A-Za-z_-]{11}).*'
    matchObj = re.search(VIDEO_ID_REGEX,videoUrl)
    videoId = matchObj.group(1) if matchObj else None
    return videoId


videoUrl = "https://youtu.be/jJdIU3GaoQU"
print(getIdFromUrl(videoUrl))




