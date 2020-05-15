import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male




def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    speak("Sir I am Jarvis How may I help You?")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...............")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("RECOGNISING..............")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print(e)
        print("Say That Again Please.....")
        return "NONE"
    return query
#email

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('enter your own email','enter password')
    server.sendmail('Your email',to,content)
    server.close()


if __name__ =="__main__":
    wishMe()
    
    while True:  
    #executing the task
        query=takeCommand().lower()

        #wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia............')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        #WEBSITE OPEN
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("web.whatsapp.com")
        # Playing music
        elif 'play music' in query:
            music_dir = 'F:\\music test'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        # Checking the time
        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        
        #Opening any file on computer
        elif 'open sublime' in query:
            speak("opening sublime")
            path="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(path)
        elif 'shutdown' in query:
            speak("Thank you for using me Hope I helped you out!!!")
            exit()


        elif 'email to' in query:
            try:
                speak("What should I say")
                content=takeCommand()
                to="the person who you want to send email"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry I am not able to send the email")
