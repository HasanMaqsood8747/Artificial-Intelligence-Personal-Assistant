import pyttsx3
import datetime
import time
import speech_recognition as sr
import smtplib
from secrets import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb 
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import webbrowser

from tkinter import *
from PIL import ImageTk, Image

import getpass  # Import the getpass module
import os      # Import the os module

a=pyttsx3.init()

# This speak function is for taking audio as input FROM USER:
def speak(audio): 
    a.say(audio)
    a.runAndWait()
    
# This getvoices function is for selecting Male or female voice:
def getvoices(voice):
    voices = a.getProperty('voices')
    if voice == 1:
        a.setProperty('voice', voices[0].id)
        speak("hello this is jarvis")
    if voice == 2:
        a.setProperty('voice', voices[1].id)
        speak("hello this is Friday")

# voice = int(input("Press 1 for Male voice:\nPress 2 for Female voice:\n"))
# getvoices(voice) 

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("The current date is:")
    speak(date)
    speak(month)
    speak(year)


def show_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is:")
    speak(Time)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Afternoon sir!")
    else:
        speak("Good Night Sir!")

user_name = getpass.getuser()
def wishme():
    welcome_message = f"Welcome Back Hasan"
    speak(welcome_message)
    greeting()
    date()
    show_time()
    speak("How may I help you Sir!")
# wishme()
def takeCommandCMD():
    query = input("Please enter your input:")
    return query

import time

def takeCommandMic(timeout=5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Optional: adjust for ambient noise
        audio = None
        start_time = time.time()

        while time.time() - start_time < timeout:
            try:
                audio = r.listen(source)
                break
            except sr.WaitTimeoutError:
                pass

        if audio is None:
            print("Timeout reached. No speech detected.")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Please speak again...")
        return "None"

    return query


def sendEmail(receiver,subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    # server.sendmail(senderemail, to, content)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak('What should I search for?')
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)

def news():
    newsapi = NewsApiClient(api_key='a3647543ea8142c09034b046cd0d74b5')
    speak("What topic do you need the news about?")
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,language ='en',page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        description = f'{x}{y["description"]}'
        print(description)
        speak(description)
        
       

    speak("that's it for now I will update you in some time")


class Widget:
    def __init__(self):
        root = Tk()
        root.title('Jarvis')
        root.config(background='#286FA8')
        root.geometry('1120x550')
        root.resizable()
        img = ImageTk.PhotoImage(Image.open("man2.jpg"))
        panel = Label(root, image = img)
        panel.pack(side='right', fill='y',expand = "no") 

        userFrame = LabelFrame(root, bg='#286FA8', fg='white', font=('Poppins', 15), borderwidth=2, relief='flat')
        userFrame.pack(fill='both', expand='yes', side='top')

        self.time_label = Label(userFrame, text='', bg='#286FA8', fg='white', font=("Poppins", 45, 'bold'), height=1)
        self.time_label.pack(fill='both', expand='yes', side='top', pady= (20,0))

        label = Label(userFrame, text=f"Hasan Welcome to your AI Assistant.\n How May I help you?", bg='#286FA8', fg='white', font=('Poppins', 20, 'bold'), height=2)
        label.pack(fill='both', expand='yes', side='top', pady= (0,10))      

        # Create user and Jarvis messages
        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('CLick Run Jarvis and ask question.')

        labe2 = Label(userFrame, textvariable=self.userText , bg='#286FA8', fg='white', font=('Poppins', 15))
        labe2.pack(fill='both', expand='yes', side='top')  

        # Create buttons

        btn = Button(userFrame, text='Run Jarvis', font=('Poppins', 15, 'bold'), bg='#39AAD0', fg='white', command=self.clicked, borderwidth=2, relief='flat', pady=-10)
        btn.pack(fill='x', expand='yes', side='left', padx = (100, 10), pady= '10')

        btn1 = Button(userFrame, text='Close Jarvis', font=('Poppins', 15, 'bold'), bg='#ffffff', fg='#39AAD0', command=root.destroy, borderwidth=2, relief='flat', pady=-10)
        btn1.pack(fill='x', expand='yes', side='right', padx = (10, 100), pady= '10')


        # Load social media icons
        button_frame = Frame(root, bg='#286FA8')
        button_frame.pack(pady= 20, side='top')

        google_icon = ImageTk.PhotoImage(Image.open("google.png"))
        facebook_icon = ImageTk.PhotoImage(Image.open("whatsapp.png"))
        youtube_icon = ImageTk.PhotoImage(Image.open("yt.png"))

        # Create and display buttons with social media icons
        labe4 = Label(button_frame, text='Navigate Yourself!' , bg='#286FA8', fg='white', font=('Poppins', 12))
        labe4.pack(fill='both', expand='yes', side='top')  
        google_button = Button(button_frame, image=google_icon, bg='#286FA8', borderwidth=2, relief='flat', command=self.open_google)
        facebook_button = Button(button_frame, image=facebook_icon, bg='#286FA8', borderwidth=2, relief='flat', command=self.open_facebook)
        youtube_button = Button(button_frame, image=youtube_icon, bg='#286FA8', borderwidth=2, relief='flat', command=self.open_youtube)

        google_button.pack(pady=10, side='left', padx = '5')
        facebook_button.pack(pady=10, side='left', padx = '5')
        youtube_button.pack(pady=10, side='left', padx = '5')


        labe3 = Label(root, text="Thanks for using Jarvis. Hope You enjoyed it.", bg='#0d223d', fg='white', font=('Poppins', 11), pady=10)
        labe3.pack(fill='both', expand='yes', side='bottom', pady='0')  

        # Bind the Enter key event
        root.bind("<Return>", self.clicked)

        # Update the Jarvis frame with the current time
        self.update_time()

        root.mainloop()

    def clicked(self):
        print('Working')
        query = takeCommandMic()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        # while True:
        # query = takeCommandMic().lower()
        if 'time' in query:
           show_time()
        elif 'date' in query:
            date()
        elif 'email' in query:
            email_list = {
                'Hasan' : 'hasanmaqsood2001@gmail.com',
                
            }
            try:
                speak('To whom you want to send an email')
                name = takeCommandMic()
                receiver = email_list[name]
                speak('What is the Subject of the mail?')
                subject = takeCommandMic()
                speak('What Email do you want to send?')
                content = takeCommandMic()
                sendEmail(receiver, subject, content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak('Unable to send the email')
            
        elif 'message' in query:
            user_name = {
                    'Hasan':'+923125849765',
                    'Ali':'+923085849765',
                    'Hamza':'+923325755116'

                }
            try:
                speak('To whom you want to send a whatsapp message')
                name = takeCommandMic()
                phone_no = user_name[name]
                speak('What is the message?')
                message = takeCommandMic()
                sendwhatsmsg(phone_no,message)
                speak('message has been sent')
            except Exception as e:
                print(e)
                speak('Unable to send the message')

        elif 'wikipedia' in query:
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'google' in query:
            searchgoogle()
           
        elif 'youtube' in query:
            speak('What should I search on Youtube?')
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)

        elif 'weather' in query:
            url = 'https://api.openweathermap.org/data/2.5/weather?q=jhelum&units=imperial&appid=16a2a26237fbce169e27f6eb88672e34'
            
            res = requests.get(url)
            data = res.json()

            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp = data['weather'] [0] ['description']
            temp = round((temp - 32) * 5/9)
            print(weather)
            print(temp)
            print(desp)
            speak('Today Temperature is : {} degree celcius'.format(temp))
            speak('And weather is {}'.format(desp))

        elif 'news' in query:
            news()
        
        elif 'offline' in query:
            quit()

    def update_time(self):
        # Get the current time
        current_time = datetime.datetime.now().strftime("%I:%M %p")

        # Update the Jarvis frame text with the current time
        self.time_label.config(text=f'{current_time}')

    def open_google(self):
        webbrowser.open('https://www.google.com')

    def open_facebook(self):
        webbrowser.open('https://web.whatsapp.com')

    def open_youtube(self):
        webbrowser.open('https://www.youtube.com')

if __name__ == "__main__":
    getvoices(1)
    wishme()
    widget = Widget() 
