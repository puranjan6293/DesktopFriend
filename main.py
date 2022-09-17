import time

from pyparsing import And
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import pywhatkit
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import json #java to python converter
import requests #url decoder
import subprocess #for opening any app
"""
#not using
from selenium import webdriver #for webpage
import weather_forecast as wf #for weather forcast

"""
from bs4 import BeautifulSoup #using for knowing weather




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")

    else:
        speak("Good Evening Boss!")

    speak("Jarvice here. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'on youtube' in query:
            song = query.replace('on youtube', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            speak("playing music")
            music_dir = 'F:\MY MEDIA FILES\VidMate'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'hello jarvis' in query:
            speak("Hello sir, please say how can I help you")

        elif 'thanks jarvis' in query:
            speak("its my pleasure sir")

        elif 'sorry jarvis' in query:
            speak("Sir,  please dont say sorry please")

        elif 'abilities' in query:
            speak("See,  I can do everything like..")
            speak("I can talk with you, "
                  "i can play music for you, "
                  "I can search videos in youtube, "
                  "I can soulve your queries with wikipedia command, "
                  "And many more..")

        elif'your boss' in query:
            speak("puranjan sir is my boss")

        elif 'about yourself' in query:
            speak("my name is jarvice, I am an AI, created by puranjan sir.")

        elif 'about puranjan' in query:
            speak("puranjan mallik is my boss, he is a NITAN.")

        elif 'hindi' in query:
            speak("sorry sir, I dont know hindi. I am in learning stage")

        elif 'hobbies' in query:
            speak("my hobbies are helping my boss,puranjan sir."
                  " but my boss hobbies are like coading, gaming, listining music")

        elif 'favourite food' in query:
            speak("sorry I cant eat food "
                  " but my boss favourite food is butter chicken.")

        #MATHEMATICALS
        elif 'square' in query:
            speak("ok, enter your number")
            s=int(input("enter your no\n"))
            sp= s*s
            speak("the square is ")
            speak(sp)

        elif 'addition' in query:
            speak("Ok, enter the values")
            v1=int(input("v1=\n"))
            v2=int(input("v2=\n"))
            sum=v1+v2
            speak("the addition is ")
            speak(sum)

        elif 'multiplication' in query:
            speak("ok, enter the values")
            m1=int(input("m1=\n"))
            m2=int(input("m2=\n"))
            multi=m1*m2
            speak("the multiplication is ")
            speak(multi)

        elif 'division' in query:
            speak("ok, enter the values")
            d1=int(input("d1="))
            d2=int(input("d2="))
            divi=d1/d2
            speak("the division is ")
            speak(divi)

        elif 'love you' in query:
            speak("sorry sir, this is biologically not possible.")

        elif 'you married' in query:
            speak("no, i could not marry")

        elif 'mad' in query:
            speak("no, i am an inteligent AI")

        elif'who are you' in query:
            speak("I am an inteligent AI, created by Puranjan Sir")

        elif 'my birthday' in query:
            speak("Wishing you a day full with happyness and a year filled with joy. "
                  " Happy birthday sir")

        elif 'how are you' in query:
            speak("I am fine sir. and I wish you are also fine")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'siri' in query:
            speak("siri is my girlfriend, she is an AI of IOS operating system")

        elif 'alexa' in query:
            speak("alexa is an AI, devloped by Amazon")

        elif 'google' in query:
            speak("google is a search engine, and it also have an AI,"
                  " bassed on andriod operating system")

        elif 'bixby' in query:
            speak("bixbi is an AI, devloped by samsung")

        elif 'drink water' in query:
            speak("ohh no  ,I can not drink water"
                  " but peoples must drink 3 liter of water daily")

        elif 'specification' in query:
            speak("ok, listn carefully,"
                  " I have 8 giga bite ram and 512 giga bite rom, "
                  " I have a very powerfull ryzen 5, 4000 series processor, "
                  "with integrated amd radeon graphics, "
                  " ohh  you can search it on google")

        elif 'parents' in query:
            speak("see, I am created by Puranjan sir,"
                  " but my boss mom and dad is niyati and balabhadra, "
                  " also have a brother named shantanu")

        elif 'rati kanta' in query:
            speak("ratikanta or called tungura is best friend of my boss "
                  " puranjan sir")

            #Opening some desktop applications

        elif 'open vs code' in query:
            speak("Opening Visual studio code, Boss")
            subprocess.call("C://Users//malli//AppData//Local//Programs//Microsoft VS Code//Code.exe")

        elif 'open command prompt' in query:
            speak("Opening command prompt, Boss")
            subprocess.call("cmd.exe")

        elif 'open calculator' in query:
            speak("opening calculator, Boss")
            subprocess.call("calc.exe")

        elif 'open notepad' in query:
            speak("opening notepad, Boss")
            subprocess.call("notepad.exe")

        elif 'close notepad' in query: #for closing
            speak("closing notepad Boss")
            os.system("taskkill /f /im notepad.exe")

        elif 'open chrome' in query:
            speak("opening chrome, Boss")
            subprocess.call("C://Program Files//Google//Chrome//Application//chrome.exe")

        elif 'open telegram' in query:
            speak("opening telegram, Boss")
            subprocess.call("C://Users//malli//AppData//Roaming//Telegram Desktop//Telegram.exe")

        elif 'open microsoft team' in query:
            speak("opening microsoft teams, Boss")
            subprocess.call("C://Users//malli//AppData//Local//Microsoft//Teams//Update.exe")

        elif 'open video editor' in query:
            speak("opening movavi video editor plus, Boss")
            subprocess.call("C://Users//malli//AppData//Roaming//Movavi Video Editor Plus 2021//VideoEditorPlus.exe")

        elif 'open cleaner' in query:
            speak("opening cc cleaner, Boss")
            subprocess.call("C://Program Files//CCleaner//CCleaner64.exe")

        elif 'open vlc player' in query:
            speak("Opening VLC player, Boss")
            subprocess.call("C://Program Files (x86)//VideoLAN//VLC//vlc.exe")


        elif 'my document file' in query:
            mydocoments = "D:\my docoments"
            speak("opening my docoments")
            os.startfile(mydocoments)

        elif 'my media file' in query:
            mymedia = "F:\MY MEDIA FILES\VidMate"
            speak("opening my media files")
            os.startfile(mymedia)

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif 'open canva' in query:
            speak("opening canva")
            webbrowser.open("canva.com")

        elif 'email to puranjan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mallik.puranjan@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Puranjan bhai. I am not able to send this email")

        elif 'news about' in query:
            try:
                datefor = datetime.date.today()
                news_about = query.replace('news about', '')
                speak(f"Boss wait a minute, I am finding the best news about {news_about} for you.")
                speak('the top five best news are...')
                news_api = "166cf40956434d289c251173d7e36715"
                news_data = requests.get(
                    f"https://newsapi.org/v2/everything?q={news_about}&from={datefor}&sortBy=publishedAt&apiKey={news_api}")
                news_report = news_data.json()
                article = news_report["articles"]
                best_articles = []
                for arti in article:
                    best_articles.append(arti['title'])
                for at in range(5):
                    fullnews = at + 1, best_articles[at]
                    speak(fullnews)
            except Exception as eee:
                print(eee)
                speak("No news Found")

        elif 'send message' in query:
            speak("What do you want to say?")
            x1=takeCommand()
            speak("in which WhatsApp number")
            x2=input("enter the whatsapp number\n")
            msgtime=datetime.datetime.now()
            pywhatkit.sendwhatmsg(x2, x1, time_hour=msgtime.hour, time_min=msgtime.minute+2)
            speak("message sended succesfully")

        elif 'set reminder' in query:
            from plyer import notification
            speak("Ok, set time")
            h=int(input("Hour\n"))
            m=int(input("Minute\n"))
            remindTime=datetime.datetime.now()
            if h == remindTime.hour and m == remindTime.minute:
                notification.notify(
                    title="**Reminder Sir!!",
                    message="You Have A Reminder Sir.",
                    app_icon="E:\remind\icon.ico",
                    timeout=12
                )
        elif 'schedules' in query: # in doubt
            speak("Ok, add your schedules")
            sh1 = input("add your schedules\n")
            shdt = input("Add your schedule time")
            h3 = int(input("Hours\n"))
            m3 = int(input("minutes\n"))
            scheduleTime = datetime.datetime.now()
            if h3 == scheduleTime.hour and m3 == scheduleTime.minute:
                aud = f"Sir you have a  shedule of {sh1} at the time in {shdt}"
                speak(aud)

        elif 'set a timer' in query: #Timer program
            speak("time for...")
            tmr = int(input("timer time in sec-\n"))
            while tmr:
                tmr = tmr-1
                time.sleep(1)
                if tmr ==0:
                    speak("Boss, your time is up")

        elif 'weather of' in query:
            api_key = "a10d14f7bfe7cb43c38b24a42e91ca45"
            user_input = query.replace('weather of', '')
            weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}")
            if weather_data.json()['cod'] == '404':
                print("No city found")
            else:
                weather = weather_data.json()['weather'][0]['main']
                tempr = round(weather_data.json()['main']['temp'])
                celcious = tempr-273.15
                celcis_int = int(celcious)
                # weather_descrp = weather_data.json()['weather'][0]['description']
                humidt = weather_data.json()['main']['humidity']
                windspd = weather_data.json()['wind']['speed']
                visibilty = weather_data.json()['visibility']
                sunris = weather_data.json()['sys']['sunrise']
                sunset = weather_data.json()['sys']['sunset']

                speak(f"the weather in {user_input} is: {weather} type")
                speak(f"the temperature in {user_input} is: {celcis_int} degree celcious")
                speak(f"the humidity of {user_input} city is {humidt}")
                speak(f"the wind speed in {user_input} is {windspd}")
                speak(f"the visibility of {user_input} is {visibilty}")
                speak(f"the sunrise time in {user_input} city is {sunris}")
                speak(f"and the sunset time in {user_input} city is {sunset}")

        elif 'sing' in query:
            speak("Boss I am Not good in singing, "
                  "but as your wish.."
                  "Listen my song ")
            speak("All my life I want money and power, "
                  "Respect my mind or die from lead glower, "
                  "I pray my dick get huge as the Eiffel Tower, "
                  "So I can fuck the world for twenty four hours...")

        elif 'what is the meaning of' in query:
            try:
                question = query.replace('what is the meaning of', '')
                question_url = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{question}")
                question_ans = question_url.json()
                # print(question_ans)
                organised_ans = str(question_ans[0]['meanings'][0]['definitions'][0]['definition'])
                print(organised_ans)
                speak(f"The meaning of {question} is,  {organised_ans}")
            except Exception as ee:
                print(ee)
                speak("Meaning not found")





