import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source , duration=1)
        audio=r.listen(source)

    try:
        print("Wait for few moments...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}/n")
    except Exception as e:
        print(e)
        speak("Please tell me again")
        query="none"

    return query

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        print('Good morning sir... I am jarvis. how are you sir')
        speak('Good morning sir... I am jarvis. how are you sir?')
    elif hour>=12 and hour<17:
        print('Good Afternoon')
        speak('Good Afternoon')
    elif hour >=17 and hour<21:
        print('Good morning')
        speak('Good morning')
    else:
        print('Good morning')
        speak('Good morning')


if __name__ == "__main__":
    wishings()
    while True:
        query = commands().lower()
        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, The Time is: " + strTime)
            print(strTime)
        elif 'open google' or 'open google chrome' in query:
            speak("Opening Google")
            # Path
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'wikipedia' in query:
            speak("Searching in wikipedia")
            try:
                query=query.replace("wikipedia", '')
                results = wikipedia.summary(query, sentences=1)
                speak("According to google...")
                print(results)
                speak(results)
            except:
                print("No results found...")
                speak("No results found...")

        elif 'play' in query:
            playQuery=query.replace('play', '')
            speak("Playing" + playQuery)
            pywhatkit.playonyt(playQuery)
        elif 'type' in query:
            speak("Please tell me what should i write")
            while True:
                typeQuery = commands()
                if typeQuery == "exit typing":
                    speak("Okay")
                    break
                else:
                    pyautogui.write(typeQuery)
        elif 'joke' in query:
            jarvis_Joke = pyjokes.get_joke()
            print(jarvis_Joke)
            speak(jarvis_Joke)
        