import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import wikipedia
import pywhatkit as wk
import pyjokes

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello, I am your Nexus AI. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "Say that again please..."
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "Hello Nexus " in query:
            speak("Hello, I am your Nexus AI. How may I help you?")
        elif "how are you" in query:
            speak("I am fine, thank you for asking. How may I help you?")
        elif "who are you" in query:
            speak("I am your Nexus AI. How may I help you?")
        elif "what can you do" in query:
            speak("I can do a lot of things. For example, I can tell you the time, date, search anything on the internet, open any website, play music, etc. How may I help you?")
        elif "who created you" in query:
            speak("I am developed by Abhinav Singh in Python")
        elif 'what is' in query:
            query = query.replace("what is", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'who is' in query:
            query = query.replace("who is", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif "just open google" in query:
            webbrowser.open("google.com")
        elif "open google" in query:
            speak("what should I search on google?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)
        elif "just open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open youtube" in query:
            speak("what should I search on youtube?")
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}")
        elif "search on youtube" in query:
            query= query.replace("search on youtube", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif "close browser" in query:
            os.system("taskkill /f /im chrome.exe")

        elif "exit" in query:
            speak("Thank you for using me. Have a good day!")
            break
        speak(query)
