from tkinter import *
from PIL import Image, ImageTk
import pygame
import subprocess
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys


engine = pyttsx3.init()

client = wolframalpha.Client('V4UJ95-ERQ9WE5JAJ')

voices = engine.getProperty('voices')
folder ='C:\\Users\\Amrit\\Desktop\\Python\\Project\\'
b_music = ['m2']
pygame.mixer.init()
pygame.mixer.music.load(folder+random.choice(b_music)+ '.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

def speak(audio):
    print('Joy :', audio)
    engine.setProperty('voice',voices[len(voices)-1].id)
    engine.say(audio)
    engine.runAndWait()

def myCommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language='en-in')
        print('User :'+ query +'\n')

    except sr.UnknownValueError:
        speak('Try again')
        pass

    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH< 12:
        speak('Good Morning')

    if currentH >= 12 and currentH< 18:
        speak('Good AfterNoon')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

class Widget:
    def __init__(self):
        root = Tk()
        root.title('Joy(MK-1)')
        root.config(background='Red')
        root.geometry('350x600')
        root.resizable(0, 0)
        root.iconbitmap(r'C:\Users\Amrit\Desktop\Python\Project\images\Untitled-1.ico')
        img = ImageTk.PhotoImage(Image.open(r"C:\Users\Amrit\Desktop\Python\Project\images\speech-api-lead.png"))
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "no")

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click \'Start Listening\' to Give commands')

        userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
        userFrame.pack(fill="both", expand="yes")
         
        left2 = Message(userFrame, textvariable=self.userText, bg='lightyellow', fg='black')
        left2.config(font=("Comic Sans MS", 10, 'bold'))
        left2.pack(fill='both', expand='yes')

        compFrame = LabelFrame(root, text="Joy", font=('Black ops one', 10, 'bold'))
        compFrame.pack(fill="both", expand="yes")
         
        left1 = Message(compFrame, textvariable=self.compText, bg='lightyellow',fg='black')
        left1.config(font=("Comic Sans MS", 10, 'bold'))
        left1.pack(fill='both', expand='yes')
       
        btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepSkyBlue', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white', command=root.destroy).pack(fill='x', expand='no')

       
        speak('Hello, I am Joy! What should I do for You?')
        self.compText.set('Hello, I am Joy! What should I do for You?')

        root.bind("<Return>", self.clicked) 
        root.mainloop()
       
    def clicked(self):
        print('Working')
        query =myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        if 'open youtube' in query:
             speak('okay')
             webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.com')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'open facebook' in query:
            speak('okay')
            webbrowser.open('www.facebook.com')

        elif 'open flipkart' in query:
            speak('speak')
            webbrowser.open('www.flipkart.com')
            

        elif "what\'s" in query or 'how are you' in query:
            stMsgs=['just doing my things!','I am fine','nice!','I am nice and full of energy!']
            speak(random.choice(stMsgs))

        elif 'email' in query:
             speak('who is the recipient? ')
             recipient = myCommand()
             self.userText.set(recipient)
             recipient = recipient.lower()

             if 'me' in recipient:
                 try:
                     
                     speak('what should I say? ')
                     content = myCommand()
                     self.userText.set(content)

                     server=smtplib.SMTP('smtp.gmail.com',587)
                     server.ehlo()
                     server.starttls()
                     server.login("Your_Username",'Your_Password')
                     server.sendmail('Your_Username',"Recipient_Username", content)
                     server.close()
                     self.compText.set('Email sent!')
                     speak('Email sent!')

                 except:
                    self.compText.set('Email sent!')
                    speak('Sorry' + 'Sir' + '!, I am unable to sent your message at this moment!')
                 
                 
        elif 'nothing' in query or 'obort' in  query or 'stop' in query:
            self.compText.set('okay')
            speak('okay')
            self.compText.set('Bye Sir, have a good day.')
            speak('Bye Sir, have a good day.')
            root.destroy()
			

        elif 'hello' in query:
            self.compText.set('Hello Sir')
            speak('Hello Sir')

        elif 'bye' in query:
            self.compText.set('Bye ' + 'Sir' + ', have a good day.')
            speak('Bye ' + 'Sir' + ', have a good day.')

        elif 'play music' in query:
            music_folder = 'C:\\Users\\Amrit\\Desktop\\Python\\Project\\'
            music = ['music1','music2','music3','music4','music5']
            random_music = music_folder+random.choice(music)+'.mp3'
            os.system(random_music)
            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')

        else:
            try:
                try:
                    res = client.query(query)
                    results=next(res.results).text
                    self.compText.set(results)
                    speak(results)

                except:
                    results = wikipedia.summery(query,sentences=2)
                    self.compText.set(results)
                    speak(results)
            except:
                speak('I don\'t know Sir! Google is smarter than me!')
                self.compText.set('I don\'t know Sir! Google is smarter than me!')
                webbrowser.open('www.google.com')

if __name__ == '__main__':
    greetMe()
    widget = Widget()
