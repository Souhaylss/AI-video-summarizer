from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import Transcript
from youtube_transcript_api.formatters import TextFormatter


def getTranscript(videoId : str, language='en') -> Transcript :
    return YouTubeTranscriptApi.get_transcript( videoId  ,[language])

def getLanguageList(videoId : str) -> list  :
    transcriptList  = YouTubeTranscriptApi.list_transcripts(videoId)
    genLangList = list(transcriptList._generated_transcripts)
    manualLangList = list(transcriptList._manually_created_transcripts)
    return list(set(genLangList + manualLangList))

def getTextTranscript(videoId, language='en') -> str :
    transcript = getTranscript(videoId,language)
    formatter = TextFormatter()
    return formatter.format_transcript(transcript)

