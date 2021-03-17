import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mike' in command:
                command = command.replace('mike', '')
                print(command)
    except:
        pass
    return command

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
        talk("Good Evening!")  

    talk("Hello , my name is Alexa. Please tell me how may I help you")
    
def run_mike():
    command = take_command()
    print(command)
   
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you ok' in command:
        talk('sorry, I have a headache')
    elif 'you are good' in command:
        talk('Thanks, thats my pleasure')
    elif 'you are shit' in command:
        talk('sorry, what crime did I make') 
    elif 'are you busy' in command:
        talk('No , what happen,tell me, I will try to help you')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open code' in command:
        codePath = "C:\\Users\\VIJAY SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    elif 'open chrome' in command:
        codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(codePath)
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'open stack overflow' in command:
        webbrowser.open("stackoverflow.com")
    elif 'open white hat junior' in command:
        webbrowser.open("code.whitehatjr.com")
    elif 'open github' in command:
        webbrowser.open("github.com")
    elif 'hi alexa' in command:
        wishMe()
    
    else:
        talk('Please say the command again.')        


while True:
    run_mike()
