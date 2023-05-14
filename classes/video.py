import os
from pytube import YouTube
from moviepy.editor import *
import openai
import nltk
nltk.download('punkt')

openai.organization = os.getenv("OPEN_AI_ORG")
openai.api_key = os.getenv("OPEN_AI_KEY")

class Video:
    def __init__(self):
        pass

    def video_to_speech(self,youtube_url=''):
        
        # Download the YouTube video using pytube
        yt = YouTube(youtube_url)
        video = yt.streams.filter(only_audio=True).first()
        video.download()

        # Extract audio from the downloaded video using moviepy
        clip = AudioFileClip(video.default_filename)
        clip.write_audiofile(f'{yt.title}.mp3')

        #save the audio file

        os.remove(video.default_filename)

        audio = open(f'{yt.title}.mp3', 'rb')

        transcript = openai.Audio.transcribe("whisper-1", file=audio)

        os.remove(f'{yt.title}.mp3')

        return transcript

        


