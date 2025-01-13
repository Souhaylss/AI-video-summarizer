# Youtube Video Summarizer 

## Description : 

Web App that summarizes any youtube video with the Google Gemini API. 
Just enter the video URL and it does the work for you !

## How to use the tool on your local machine ? 

1. Navigate to the **back-end** directory
2. Navigate to **.env** file and enter your Gemini API key. If you don't have one yet, you can create one very easily right [HERE](https://ai.google.dev/gemini-api/docs/api-key) !
3. Enter the following command in the terminal to start the **back-end** server :
   ```
   python3 app.py
   ```
4. Navigate to the **front-end** directory
5. Enter the following command in the terminal to install dependecies and serve the website on a new window :
   ```
   npm ci
   ng serve -o
   ```
