from concurrent.futures import thread
from json import load
from tracemalloc import start
import pyttsx3      # pip install pyttsx3
import datetime     
import speech_recognition as sr     #pip install SpeechRecognition
import wikipedia        #pip install wikipedia
import webbrowser       #pip install webbrowser
import os
import pyautogui        #pip install pyautogui
import pyjokes          #pip install pyjokes
import pywhatkit as kit

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer,QTime,QDate
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from hudpro import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from time import *
import threading 
from playsound import playsound
import winsound
import pygame



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


        



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.TaskExecution()


    def wishings(self):
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print("Jarvis: Good Morning BOSS")
            speak("Good Morning BOSS")
        elif hour>=12 and hour<17:
            print("Jarvis: Good Afternoon BOSS")
            speak("Good Afternoon BOSS")
        elif hour>=17 and hour<21:
            print("Jarvis: Good Evening BOSS")
            speak("Good Evening BOSS")
        else:
            print("Jarvis: Good Night BOSS")
            speak("Good Night BOSS")
        

    def commands(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            # r.pause_threshold=1
            r.adjust_for_ambient_noise(source, duration=1)
            audio=r.listen(source)

        try:
            print("Wait for few Moments..")
            query=r.recognize_google(audio,language='en-in')
            print(f"You just said: {query}\n")

        except Exception as e:
            print(e)
            speak("Please tell me again")
            query="none"
        return query

    def wakeUpCommands(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Jarvis is Sleeping...")
            r.pause_threshold=1
            r.adjust_for_ambient_noise(source,duration=1)
            audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            query="none"
        return query


    def TaskExecution(self):     
        
        while True:
            self.query=self.wakeUpCommands().lower()
            if "wake up" in self.query:
                self.wishings()
                speak("Yes BOSS What can I do for you!")
                while True:
                    
                    self.query=self.commands().lower()
                    if "wikipedia" in self.query:
                        speak("Searching in Wikipedia")
                        try:
                            self.query=self.query.replace("wikipedia","")
                            results=wikipedia.summary(self.query,sentences=1)
                            speak("According to Wikipedia,")
                            print(results)
                            speak(results)
                        except:
                            speak("No Results found Sir...")
                            print("No results Found")
                    
                    elif "open youtube" in self.query:
                        speak("opening Youtube")
                        webbrowser.open("youtube.com")

                    elif 'time' in self.query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                        speak(f"Sir, the time is {strTime}")

                    elif "mute" in self.query:
                        speak("I'm Muting Sir...")
                        break
                    elif 'exit program' in self.query or 'exit the program' in self.query:
                        speak("I'm Leaving Sir, Byeee...")
                        quit()
                    
                    elif "open google" in self.query:
                        speak("Opening Google Chrome Sir")
                        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")        # Use the path of your file here
                        while True:
                            chromeQuery=self.commands().lower()
                            if "search" in chromeQuery:
                                youtubeQuery=chromeQuery
                                youtubeQuery=youtubeQuery.replace("search","")
                                pyautogui.write(youtubeQuery)
                                pyautogui.press('enter')
                                speak('Searching...')
                                
                            elif "close chrome" in chromeQuery or "exit chrome" in chromeQuery or "exit google" in chromeQuery or "close window" in chromeQuery or "close this window" in chromeQuery:
                                pyautogui.hotkey('ctrl','w')
                                speak("Closing Google Chrome Sir...")
                                break
                    elif "what can you do for me" in self.query:
                        print('Yes sir, Nice Question')
                        print('As per my Program, I\'m a bot which can perform tasks through your voice commands')
                        speak('Yes sir, Nice Question')
                        speak('As per my Program, I\'m a bot which can perform tasks through your voice commands')
                    elif "cool" in self.query or "nice" in self.query or "awsome" in self.query or "thank you" in self.query:
                        speak("Yes sir, That's my Pleasure!")
                    elif "minimize" in self.query or 'minimise' in self.query:
                        speak('Minimizing Sir')
                        pyautogui.hotkey('win', 'down','down')
                    elif "maximize" in self.query or 'maximise' in self.query:
                        speak('Maximizing Sir')
                        pyautogui.hotkey('win', 'up','up')
                    elif "close the window" in self.query or 'close the application' in self.query:
                        speak('Closing Sir')
                        pyautogui.hotkey('ctrl','w')
                    elif "screenshot" in self.query:
                        speak("Taking Screenshot sir...")
                        pyautogui.press('prtsc')
                    elif "open paint" in self.query:
                        speak("Opening Paint Application Sir...")           
                        os.startfile('C:\\Windows\\System32\\mspaint.exe')      # Use the path of your file here
                        while True:
                            paintQuery=self.commands().lower()
                            if "close" in paintQuery:
                                speak("Closing The Application sir")
                                pyautogui.leftClick(x=1344, y=11)
                                break
                            elif "paste" in paintQuery:
                                pyautogui.hotkey('ctrl', 'v')
                                speak("Done Sir!")
                            elif "save" in paintQuery:
                                pyautogui.hotkey('ctrl','s')
                                speak("saving sir!")
                            elif "minimize" in paintQuery:
                                speak('Minimizing Sir')
                                pyautogui.hotkey('win', 'down','down')
                                break
                            elif "maximize" in paintQuery:
                                speak('Maximizing Sir')
                                pyautogui.hotkey('win', 'up','up')
                            elif "minimise" in paintQuery:
                                speak('Minimizing Sir')
                                pyautogui.hotkey('win', 'down','down')
                            elif "maximise" in paintQuery:
                                speak('Maximizing Sir')
                                pyautogui.hotkey('win', 'up','up')
                    elif "open notepad" in self.query:
                        speak("Opening Notepad Application sir...")
                        os.startfile('C:\\Windows\\System32\\notepad.exe')          # Use the path of your file here
                        while True:
                            notepadQuery=self.commands().lower()
                            if "paste" in notepadQuery:
                                pyautogui.hotkey('ctrl','v')
                                speak("Done Sir!")
                            elif "save this file" in notepadQuery:
                                pyautogui.hotkey('ctrl','s')
                                speak("Sir, Please Specify a name for this file")
                                notepadSavingQuery=self.commands()
                                pyautogui.write(notepadSavingQuery)
                                pyautogui.press('enter')
                            elif 'type' in notepadQuery:
                                speak("Please Tell me what should I Write...")
                                while True:
                                    writeInNotepad=self.commands()
                                    if writeInNotepad == 'exit typing':
                                        speak("Done Sir.")
                                        break
                                    else:
                                        pyautogui.write(writeInNotepad)
                                    
                            elif "exit notepad" in notepadQuery or 'close notepad' in notepadQuery:
                                speak('quiting Notepad Sir...')
                                pyautogui.hotkey('ctrl', 'w')
                                break
                    elif 'play song' in self.query or 'sing a song' in self.query or 'play a song' in self.query or 'play music' in self.query or 'play a music' in self.query:
                        speak("Yes Sir Please Wait a moment")
                        songs=os.listdir('D:\Musics')       # Use the path of your file here
                        os.startfile(os.path.join('D:\Musics',songs[0]))        # Use the path of your file here
                    elif 'pause' in self.query or 'pass' in self.query:
                        pyautogui.press('space')
                        speak('Done Sir')
                    elif 'joke' in self.query:
                        jarvisJoke = pyjokes.get_joke()
                        print(jarvisJoke)
                        speak(jarvisJoke)
                #  TODO:
                    elif 'message' in self.query:
                        print('Whom do u want to send?')
                        speak('Whom do u want to send?')
                        contact = input('Contact name: ')
                        print("Message")
                        speak("Message")
                        message = input("Message: ")
                        speak("When to send?")
                        hour__ = int(input("Hour: "))
                        minute__ = int(input("Minutes: "))
                        kit.sendwhatmsg(contact, message, hour__, minute__)
                        

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        n = 500
        self.ui.progressBar.setRange(0, n)
        
        # Hiding elements
        self.ui.arcreacter.hide()
        self.ui.startpushButton.hide()
        self.ui.quitpushButton_2.hide()
        self.ui.globe.hide()
        
        self.ui.button.clicked.connect(lambda status,n_size=n: self.run(n_size))
        
        
    
    def run(self, n):
        
        # Add Intro Music
        pygame.mixer.init()
        pygame.mixer.music.load("F:\\Tech fest project\\jarvisintro.mp3")
        pygame.mixer.music.play()
        for i in range(n):
            sleep(0.01)
            self.ui.progressBar.setValue(i+1)
            
        
            
        
        
        
        
        
        self.ui.button.hide()
        self.ui.progressBar.hide()
        self.ui.startpushButton.show()
        self.ui.startpushButton.clicked.connect(self.startTask)
        
        self.ui.quitpushButton_2.clicked.connect(self.close)
        
    def startTask(self):
                
        
        def countdown():
            global my_timer
    
            my_timer = 5
    
            for x in range(5):
                my_timer = my_timer - 1
                sleep(1)
                
            # print("Hello")

        countdown_thread = threading.Thread(target = countdown)

        countdown_thread.start()

        while my_timer > 0:
            sleep(1)
    
        # After Timer Task
        self.ui.arcreacter.show()
        self.ui.globe.show()
        self.ui.quitpushButton_2.show()
        
        
        # Jarvis Gui
        
        self.ui.movie = QtGui.QMovie("F:\\Tech fest project\\reacter.gif")
        self.ui.arcreacter.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        
        # playsound('F:\\Tech fest project\\jarvisintro.mp3', block=False)
        
        # self.ui.movie = QtGui.QMovie("F:\\Tech fest project\\reacter.gif")
        # self.ui.arcreacter.setMovie(self.ui.movie)
        # self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("F:\\Tech fest project\\globe.gif")
        self.ui.globe.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()
        


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())


# Timer For Splash Screen