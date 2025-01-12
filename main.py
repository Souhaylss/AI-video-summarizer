from summary import summarizeVideo


summary = summarizeVideo()

with open('summary.html','w',encoding='utf-8') as file:
    file.write(summary)