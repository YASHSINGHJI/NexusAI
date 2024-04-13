import pyautogui
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import wikipedia
import pywhatkit as wk
import pyjokes
import time

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
        if "hello" in query:
            speak("Hello, I am your Nexus AI. How may I help you?")
        elif "how are you" in query:
            speak("I am fine, thank you for asking. How may I help you?")
        elif "who are you" in query:
            speak("I am your Nexus AI. How may I help you?")
        elif "what can you do" in query:
            speak(
                "I can do a lot of things. For example, I can tell you the time, date, search anything on the "
                "internet, open any website, play music, etc. How may I help you?")
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
            query = query.replace("search on youtube", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif "close browser" in query:
            os.system("taskkill /f /im chrome.exe")
        elif "open paint" in query:
            npath = "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(npath)
        elif "close paint" in query:
            os.system("taskkill /f /im mspaint.exe")
        elif "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")
        elif "play music" in query:
            music_dir = "C:\\Users\\ASUS\\My-Heart-Will-Go-On.mp3"
            os.startfile(music_dir)
        elif "can you tell me the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif "shut down" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "lock the system" in query:
            os.system("rundll32.exe user32.dll,LockWorkStation")
        elif "open camera" in query:
            os.system("start microsoft.windows.camera:")
        elif "take screenshot" in query:
            speak("Please tell me the name for the screenshot file")
            name = takeCommand().lower()
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot has been taken successfully")
        elif "calculate" in query:
            speak("What should I calculate?")
            calc = takeCommand().lower()
            result = eval(calc)
            speak(f"The result is {result}")
        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "type" in query:
            query = query.replace("type", "")
            pyautogui.typewrite(f"{query}")
        elif "youtube search" in query:
            query = query.replace("youtube search", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif "google search" in query:
            query = query.replace("google search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif "open new window" in query:
            pyautogui.hotkey("ctrl", "n")
        elif "open incognito window" in query:
            pyautogui.hotkey("ctrl", "shift", "n")
        elif "scroll up" in query:
            pyautogui.scroll(200)
        elif "scroll down" in query:
            pyautogui.scroll(-200)
        elif "minimise this window" in query:
            pyautogui.hotkey("win", "down")
        elif "open new tab" in query:
            pyautogui.hotkey("ctrl", "t")
        elif "close tab" in query:
            pyautogui.hotkey("ctrl", "w")
        elif "next tab" in query:
            pyautogui.hotkey("ctrl", "tab")
        elif "previous tab" in query:
            pyautogui.hotkey("ctrl", "shift", "tab")
        elif "open downloads" in query:
            os.system("start shell:Downloads")
        elif "open chrome" in query:
            os.system("start chrome")
        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")
        elif "open spotify and play" in query:
            query = query.replace("open spotify and play", "")
            os.system(f"start spotify:search:{query}")
        elif "exit" in query:
            speak("Thank you for using Nexus. Have a good day Abhinav!")
            break
        else:
            speak("I am sorry, I didn't get that. Please say it again.")
            continue
