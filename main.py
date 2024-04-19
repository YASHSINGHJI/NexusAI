import pyautogui
import requests
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import wikipedia
import pywhatkit as wk
import pyjokes
import time
import json

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
    speak("I am your Nexus AI. How may I help you Abhinav?")


def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9006914aee56454884fa88bf26bcccc2",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=9006914aee56454884fa88bf26bcccc2",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=9006914aee56454884fa88bf26bcccc2",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=9006914aee56454884fa88bf26bcccc2",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=9006914aee56454884fa88bf26bcccc2",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=9006914aee56454884fa88bf26bcccc2"
    }

    content = None
    url = None
    print("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , "
        "[science]")
    speak(
        "Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , "
        "[science]")
    field = takeCommand().lower()
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        speak("Do you want me to continue?")
        a = takeCommand().lower()
        if str(a) == "continue":
            pass
        elif str(a) == "stop":
            break

    speak("that's all")


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
    wishMe()
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
            print(result)
            speak("According to Wikipedia %s" % result)

        elif 'who is' in query:
            query = query.replace("who is", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak("According to Wikipedia %s" % result)

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
        elif "tell me the weather" in query:
            def get_weather_forecast(api_key, city):
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
                response = requests.get(url)
                data = response.json()
                if response.status_code == 200:
                    weather = {
                        "description": data["weather"][0]["description"],
                        "temperature": data["main"]["temp"],
                        "humidity": data["main"]["humidity"],
                        "wind_speed": data["wind"]["speed"]
                    }
                    return weather
                else:
                    return None


            def take_location_command():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening for location...")
                    speak("Please tell me the location")
                    audio = r.listen(source)

                try:
                    print("Recognizing location...")
                    location = r.recognize_google(audio, language="en-in")
                    print(f"User said: {location}")
                    return location
                except Exception as e:
                    print("Error recognizing location:", e)
                    return None


            if __name__ == "__main__":
                api_key = "f199eb32ea77257f988789bdfcebf188"
                location = take_location_command()
                if location:
                    weather_forecast = get_weather_forecast(api_key, location)
                    if weather_forecast:
                        speak(f"The weather forecast for {location} is as follows:")
                        speak(f"Description: {weather_forecast['description']}")
                        speak(f"Temperature: {weather_forecast['temperature']} degrees Celsius")
                        speak(f"Humidity: {weather_forecast['humidity']}%")
                        speak(f"Wind Speed: {weather_forecast['wind_speed']} meters per second")
                    else:
                        speak("Failed to fetch weather forecast. Please try again later.")
                else:
                    speak("Failed to recognize location. Please try again.")
        elif "latest news" in query:
            latestnews()


        elif "exit" in query:
            speak("Thank you for using Nexus. Have a good day Abhinav!")
            break
        else:
            speak("I am sorry, I didn't get that. Please say it again.")
            continue
