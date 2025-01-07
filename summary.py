import google.generativeai as genai
from dotenv import load_dotenv
from os import getenv
from transcript import getTextTranscript

load_dotenv() # load env variables located in .env file
API_KEY = getenv("API_KEY_GEM") # api key stored in .env file

genai.configure(api_key=API_KEY) 
model = genai.GenerativeModel("gemini-1.5-flash")
videoUrl = "https://www.youtube.com/watch?v=J8hzJxb0rpc&pp=ygUOd29ybGQgd2lkZSB3ZWI%3D"
videoTranscript = getTextTranscript(videoUrl)
prompt = f"Make a detailed an structured summary of the following youtube video transcript :\n {videoTranscript}"
response = model.generate_content(prompt)

with open('video_summary.txt','w',encoding='utf-8') as file:
    file.write(response.text)