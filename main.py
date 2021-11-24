import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import pyjokes
import pywhatkit
import random
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
listener=sr.Recognizer()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def run_alexa():
    command=take_command()
    print(command)
    if "play" in command:
        song=command.replace("play","")
        talk("playing"+song)
        print("playing"+song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime("%H:%M %p")
        talk("current time is"+time)
        print("current time is"+time)
    elif "Who is" in command:
        wiki_search=command.replace("Who is","")
        info=wikipedia.summary(wiki_search,1)
        print(info)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("This command is not recognized.Tell a another command")

def take_command():
    with sr.Microphone() as source:
        print("Listening....")
        listener.adjust_for_ambient_noise(source)
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if "alexa" in command:
            command=command.replace("alexa","")
            print(command)
        return command
while True:
    run_alexa()
