from gtts import gTTS
import os

def generate_audio(summary, filename="output.mp3"):
    tts = gTTS(text=summary, lang="hi")
    tts.save(filename)
    return filename
