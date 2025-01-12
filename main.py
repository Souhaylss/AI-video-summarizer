from summary import summarizeVideo


if(__name__ == "__main__"):
    summary = summarizeVideo()
    with open('summary.html','w',encoding='utf-8') as file:
        file.write(summary)