from flask import Flask, request, Response
from flask_cors import CORS
from inputValidation import checkUrlFormat, checkVideoExist
from http import HTTPStatus
from utils import getVideoIdFromUrl
from summary import summarizeVideo

app = Flask(__name__)
CORS(app)

def validateUrl(videoUrl : str) -> dict: 
    isValidFormat = checkUrlFormat(videoUrl)
    if(isValidFormat):
        isExistantVideo = checkVideoExist(videoUrl)
        if(isExistantVideo):
            return {'validity' : True}
        else:
            return {'validity' : False , 'error' : "This video does not exist !" }
    else:
        return {'validity' : False , 'error' : "Invalid URL format !" }


    
@app.post('/')
def summarize():
    videoUrl = request.get_json().get('videoUrl')
    videoValidation = validateUrl(videoUrl)
    isValidUrl = videoValidation['validity']
    respContent : str
    statusCode : int
    if(isValidUrl):
        videoId = getVideoIdFromUrl(videoUrl)
        respContent = summarizeVideo(videoId)
        statusCode = HTTPStatus.CREATED.value
    else:
        errMessage =  videoValidation['error']
        respContent = errMessage
        if('exist' in errMessage ) :
            statusCode = HTTPStatus.NOT_FOUND.value
        elif('format' in errMessage):
            statusCode = HTTPStatus.BAD_REQUEST.value
    return Response(respContent,content_type='text/plain',status=statusCode)


if __name__ == "__main__":
    app.run(port=5000,debug=True)