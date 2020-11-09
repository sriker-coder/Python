import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import requests , json
import os
import smtplib
from twilio.rest import Client
import wolframalpha
from googlesearch import search

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
        speak("Good Morning Guys!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Guys!")   

    else:
        speak("Good Evening Guys!")  

    speak("This is Dummy. Let me assist you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        queryy = r.recognize_google(audio, language='en-in')
        print(f"User said: {queryy}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return queryy

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Yeah sure...")
        speak("Yeah sure...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return command


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kusukuntla123@gmail.com', 'saisriker*123')
    server.sendmail('kusukuntla123@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
   
        queryy = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in queryy:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in queryy:
            webbrowser.open("youtube.com")
           

        elif 'google' in queryy:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in queryy:
            webbrowser.open("stackoverflow.com")   
        
        elif 'call' in queryy:
            speak('Calling you now')
            
            account_sid = "AC55bb150e7dd00669a80c61444dc009e5"
            auth_token = "af5fe7449f116476ac8c2d26f1fd83fd"
            client = Client(account_sid, auth_token)
            call = client.calls.create(
                 to="+918555860592",
                 from_="+12058579317",
                url="http://demo.twilio.com/docs/classic.mp3"
             )
            print(call.sid)

        elif 'who are you' in queryy:
            speak("I am dummy. I am a Personal Assistant developed by Serrikker.")

        elif 'play music' in queryy:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in queryy:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in queryy:
            codePath = "C:\\Users\\VASU\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'something' in queryy:
            while True:

                command= takecommand().lower()
                app_id='T7VPXR-U9R8WQ2XGA'
                client = wolframalpha.Client(app_id)
                res=client.query(command)
                answer= next(res.results).text
                print(answer)
                speak(answer)

        elif 'show me the map of' in queryy:
            api_key= 'AlzaSyA3ZNdkMwigujzDYANCY8XAUrtSz6l3eB4'
            url= "https://maps.googleapis.com/maps/api/staticmap?"
            data=takecommand().lower()
            r = requests.get(url+'data='+data+'&key='+api_key)
            x=r.json
            y=x['Results']
            for i in range(len(y)):
                speak(y[i]['name'])
                print(y[i]['name'])

        elif 'search' in queryy:
            data = takecommand().lower()
            for j in search(data, tld="co.in", num=10, stop=10, pause=2):
                print(j)
                
        elif 'send mail' in queryy:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "saisri@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, cannot send the email")    