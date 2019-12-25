import speech_recognition as sr
import webbrowser
import time
import os
import random
from time import ctime

r = sr.Recognizer()

speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
speaker.setPropert('voice', voices[1].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 173)

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alext_speak('Sorry, I did not get that')
        except sr.RequestError:
            alexis_speak('Sorry, my speech service is down')
        return voice_data


def responde(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is Alexis')
    if 'what time is it' in voice_data:
        alexis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what found for' + search)
    if 'find locaton' in voice_data:
        location = record_audio('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
alexis_speak('How can i help you?')
while True:
    voice_data = record_audio()
    responde(voice_data)

