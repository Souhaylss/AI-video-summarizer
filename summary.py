import google.generativeai as genai
from dotenv import load_dotenv
from os import getenv
from transcript import *
from markdown_it import MarkdownIt

def config() : 
    load_dotenv() # load env variables located in .env file
    API_KEY = getenv("API_KEY_GEM") # api key stored in .env file
    genai.configure(api_key=API_KEY) 

def getMarkDownSummary(videoUrl : str, language : str): # video summary in mark down format
    model = genai.GenerativeModel("gemini-1.5-flash")
    videoTranscript = getTextTranscript(videoUrl, language)
    prompt = f"Use plain text format with bullet points. Make a detailed an structured summary of the following youtube video transcript :\n {videoTranscript}"
    return model.generate_content(prompt).text

def getHtmlSummary(text : str): # convert mark down summary to displayable format (HTML)
    md = MarkdownIt()
    return md.render(text)

#TODO check if user's input is a valid youtube LINK !
def checkInput(): 
    pass


DEFAULT_VIDEO_URL = "https://www.youtube.com/watch?v=Tugbu6Kw0vE"

#TODO add input verification
def getUserInput(): 
    videoUrlInput : str = input("Enter the youtube video URL : ")
    return videoUrlInput if videoUrlInput else DEFAULT_VIDEO_URL

def summarizeVideo(language='en'):
    videoUrl = getUserInput()
    mdText = getMarkDownSummary(videoUrl,language)
    return getHtmlSummary(mdText)

config()

summary = summarizeVideo('fr')

with open('example-summary.html','w',encoding='utf-8') as file:
    file.write(summary)