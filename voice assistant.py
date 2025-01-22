import speech_recognition as sr
import datetime

import pywhatkit
import pyttsx3
import webbrowser
import wikipedia
import pyjokes
import pyaudio
import geopy
from geopy.geocoders import Nominatim
from geopy import distance
#librabry for gui
from tkinter import * 
from tkinter.ttk import *
from PIL import Image,ImageTk,ImageSequence
import time





#voice assistant code


engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        talk('Good moring')
    elif hour >=12 and hour <18:
        talk('Good Afternoon')
    else:
        talk('Good evening')

def talk(text):
    play_gif  
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
         with sr.Microphone() as source:
            play_gif
            print('Clearing background noises..Please wait')
            recognizer.adjust_for_ambient_noise(source,duration=0.5)
            print('Ask me anything..')
            recordedaudio=recognizer.listen(source,None,3)
            command=recognizer.recognize_google(recordedaudio,language='en_US')
            command=command.lower()
            if 'sigma' in command:
                command=command.replace('sigma','')
                return command
    except:
        pass
            
    
   
def take_command1():
    try:
        with sr.Microphone() as source:
            play_gif
            
            recognizer.adjust_for_ambient_noise(source,duration=0)
            print('Waiting for your reply...')
            recordedaudio=recognizer.listen(source,None,3)
            command1=int(recognizer.recognize_google(recordedaudio,language='en_US'))
            return command1
    except:
        pass

def take_command2():
    try:
        with sr.Microphone() as source:
            play_gif
            
            recognizer.adjust_for_ambient_noise(source,duration=0)
            print('Waiting for your reply...')
            recordedaudio=recognizer.listen(source,None,3)
            command2=recognizer.recognize_google(recordedaudio,language='en_US')
            command2=command2.lower()
            return command2
    except:
        pass   

def run__sigma():
    play_gif
    command= take_command()
    
    
    if 'hello' in command:
        wishMe()
        talk('I am your voice assistant, Sigma. How can i help you?')
        play_gif
    elif 'how are you' in command:
        talk('i am great, hope you are doing well')
        play_gif
    elif 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)

        print('playing'+ song)
        pywhatkit.playonyt(song)
        play_gif


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)        
        talk('current time is'+time)
        play_gif

    elif 'youtube' in command:
        talk('opening youtube')
        webbrowser.open('www.youtube.com')
        play_gif

    elif 'date' in command:
        from datetime import date 
        today = date.today()
        talk(today)
        print(today)
        play_gif

    elif 'joke' in command:
        joke = pyjokes.get_joke(language='en' , category='all')
        print(joke)
        talk(joke)
        play_gif

    elif 'who is' in command:
        person=command.replace('who is', '')
        info= wikipedia.summary(person,1)
        print(info)
        talk(info)
        play_gif
        
        
    elif 'spotify' in command:
        talk('Opening Spotify..')
        webbrowser.open('open.spotify.com')
        play_gif

    elif "calculator" in command:
        talk("welcome to the calculator")
        print("/ X - + CALCULATOR + - X /")
        talk('What is the first number?')
        n1=take_command1()
        talk('what is the second number?')
        n2=take_command1()
        talk('What do you want to perform')
        n=take_command2()
        if n=='addition':
            a=int(n1)+int(n2)
            talk('the answer is')
            talk(a)                
            print(a)
            play_gif
        elif n=='subtraction':
            a=int(n1)-int(n2)
            talk('the answer is')
            talk(a)
            print(a)
            play_gif
        elif n=='multiplication':
            a=int(n1)*int(n2)
            talk('the answer is')
            talk(a)
            print(a)
            play_gif
        elif n=='division':
            a=int(n1)//int(n2)
            talk('the answer is')
            talk(a)
            print(a)
            play_gif
    elif 'distance' in command:
        talk('Please name the first location')
        n1=take_command2()
        talk('please name the second location')
        n2=take_command2()
        a=Nominatim(user_agent="sigma")
        c1=a.geocode(n1)
        c2=a.geocode(n2)
        lat1,long1=(c1.latitude),(c1.longitude)
        lat2,long2=(c2.latitude),(c2.longitude)
        p1=(lat1,long1)
        p2=(lat2,long2)
        dist=distance.distance(p1,p2)
        print(dist)
        j='the distance between'+n1+'and'+n2+'is'
        talk(j)
        talk(dist)
        play_gif

##gui code
# creating tkinter window
root = Tk()
root.configure(bg="white")

  

# Adding widgets to the root window
Label(root, text = '   TEAM SIGMA \nVOICE ASSISTANT\n PLEASE SPEAK!!!',background="white", font =('Verdana', 15)).pack(side = TOP, pady = 10)
vaguifile=(r"C:\Users\rajde\OneDrive\Desktop\vagui12\VA4.gif")
#gif file
def play_gif():
    global img
    img=Image.open(vaguifile)
    lbl=Label(root)
    lbl.place(x=8,y=119)
    for img in ImageSequence.Iterator(img):
        img=ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.03)
    root.after(0,play_gif)
# Creating a photoimage object to use image
photo = PhotoImage(file = r"C:\Users\rajde\OneDrive\Desktop\vagui12\VA4.gif")
photo2=PhotoImage(file=r"C:\Users\rajde\OneDrive\Desktop\vagui12\speakbutton (3).png")
photo3=PhotoImage(file=r"C:\Users\rajde\OneDrive\Desktop\vagui12\stop b2 (2).png")
# here, image option is used to
# set image on button
Button(root, text = 'Click Me !', image = photo,command=play_gif).pack(side = TOP)
Button(root, text='speak',image=photo2,command=run__sigma).pack(side=LEFT)
Button(root, text="stop",image=photo3,command=root.destroy).pack(side=LEFT)
mainloop()