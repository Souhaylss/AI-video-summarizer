import re;
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import Transcript
from youtube_transcript_api.formatters import TextFormatter


def getIdFromUrl(videoUrl : str) -> int : 
    VIDEO_ID_REGEX =  '(?:v=|/)([0-9A-Za-z_-]{11}).*'
    matchObj = re.search(VIDEO_ID_REGEX,videoUrl)
    videoId = matchObj.group(1) if matchObj else None
    return videoId

def getTranscript(videoUrl : str, language='en') -> Transcript :
    return YouTubeTranscriptApi.get_transcript(getIdFromUrl(videoUrl),[language])

def getLanguageList(videoUrl : str) -> list  :
    videoId = getIdFromUrl(videoUrl)
    transcriptList  = YouTubeTranscriptApi.list_transcripts(videoId)
    genLangList = list(transcriptList._generated_transcripts)
    manualLangList = list(transcriptList._manually_created_transcripts)
    return list(set(genLangList + manualLangList))

def getTextTranscript(videoUrl, language='en') -> str :
    transcript = getTranscript(videoUrl,language)
    formatter = TextFormatter()
    return formatter.format_transcript(transcript)

