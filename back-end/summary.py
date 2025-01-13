import google.generativeai as genai
from dotenv import load_dotenv
from os import getenv
from transcript import getTextTranscript
from markdown_it import MarkdownIt

def config() : 
    load_dotenv() # load env variables located in .env file
    API_KEY = getenv("API_KEY_GEM") # api key stored in .env file
    genai.configure(api_key=API_KEY) 

def getMarkDown(videoId : str, language : str): # video summary in mark down format
    model = genai.GenerativeModel("gemini-1.5-flash")
    videoTranscript = getTextTranscript(videoId, language)
    prompt = f"Use plain text format with bullet points. Make a detailed an structured summary of the following youtube video transcript :\n {videoTranscript}"
    return model.generate_content(prompt).text

def getHtml(text : str): # convert mark down summary to displayable format (HTML)
    md = MarkdownIt()
    return md.render(text)

def summarizeVideo(videoId : str ,language='en'):
    config()
    mdText = getMarkDown(videoId,language)
    return getHtml(mdText) # html version of the markdown summary
