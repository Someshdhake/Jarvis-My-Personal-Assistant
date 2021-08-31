from sys import path
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis sir. please tell me how may I help you")


def takecommend():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('someshdhake@gmail.com', 'Somesh202029')
    server.sendmail('vineypatil30@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommend().lower()

        # logic for executimg tasked based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            music_dir = 'F:\\DJ SONG\\00 DJ'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Python\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            notepadPath ="C:\\Windows\\notepad.exe"
            os.startfile(notepadPath)

        elif 'open command prompt' in query:
            os.system("start cmd")


        elif 'send email' in query:
            try:
                speak("what should I said")
                content = takecommend()
                to = "vineypatil30@gmail.com"
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:    
                print(e)
                speak("sorry my friend. I am not able to send this email")

        elif 'joke' in query:    
            speak(pyjokes.get_joke())

        elif 'are you single' in query:    
            speak("I am a relationship with wifi")


        elif 'goodbye' in query:
            speak("thanks for using me sir, have a good day.")
            exit()