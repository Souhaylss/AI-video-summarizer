import re
import requests

def checkUrlFormat(videoUrl : str):
    YOUTUBE_LINK_FORMAT = 'https:\/\/(?:(?:www\.)?youtube\.com/\watch\?v=|youtu\.be\/)([\w-]{11}).*'
    matchObj = re.fullmatch(YOUTUBE_LINK_FORMAT,videoUrl)
    return matchObj

def checkVideoExist(videoUrl : str): 
    statusCode = requests.get(videoUrl).status_code
    VALID_STATUS_CODE = 200
    return statusCode == VALID_STATUS_CODE

