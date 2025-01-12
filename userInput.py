import re
import requests

def getUserInput(): 
    while True:
        videoUrl : str = input("Enter a youtube video URL : ")
        videoId = checkUrlFormat(videoUrl)
        isValidFormat = videoId
        if(isValidFormat):
            isExistantVideo = checkVideoExist(videoUrl)
            if(isExistantVideo):
                return videoId
            else:
                print("This video does not exist !")
        else:
            print("Invalid URL format !")
        print("Please enter a valid youtube video URL",end='\n\n')
                

def checkUrlFormat(videoUrl : str):
    YOUTUBE_LINK_FORMAT = 'https:\/\/(?:(?:www\.)?youtube\.com/\watch\?v=|youtu\.be\/)([\w-]{11}).*'
    matchObj = re.fullmatch(YOUTUBE_LINK_FORMAT,videoUrl)
    try :
        videoId = matchObj.group(1)
        return videoId
    except:
        return None

def checkVideoExist(videoUrl : str): 
    statusCode = requests.get(videoUrl).status_code
    VALID_STATUS_CODE = 200
    return statusCode == VALID_STATUS_CODE

def getVideoId() -> str:
    videoId = getUserInput()
    return videoId
