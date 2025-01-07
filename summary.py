import google.generativeai as genai
from dotenv import load_dotenv
from os import getenv
from transcript import getTextTranscript

def config() : 
    load_dotenv() # load env variables located in .env file
    API_KEY = getenv("API_KEY_GEM") # api key stored in .env file
    genai.configure(api_key=API_KEY) 

def generateSummary(videoUrl : str):
    model = genai.GenerativeModel("gemini-1.5-flash")
    videoTranscript = getTextTranscript(videoUrl)
    prompt = f"Use plain text format with bullet points. Make a detailed an structured summary of the following youtube video transcript :\n {videoTranscript}"
    return model.generate_content(prompt).text

config()

DEFAULT_VIDEO_URL = "https://www.youtube.com/watch?v=J8hzJxb0rpc"
videoUrlInput : str = input("enter the youtube video URL : ")
videoUrl = videoUrlInput if videoUrlInput else DEFAULT_VIDEO_URL
summary : str = generateSummary(videoUrl).format()

with open('example-summary.txt','w',encoding='utf-8') as file:
    file.write(summary)