import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser as wb
import os 

# if sys.version_info[0] == 2:
#     import ConfigParser as configparser
# else:
#     import configparser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].name)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour <=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Desktop Assistant Madam. Please tell me how may I help you")  
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print(str(audio))

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    print(query)
    return query
       
    
if __name__ == "__main__":
    # speak("Hello Madam, I am python machine learning Robot")
    wishMe()
    query = takeCommand().lower()
   
    # Logic to open wikipedia
    if 'wikipedia' in query:
        speak('Searching wikipedia....')
        query = query.replace("wikipedia","")
        results =  wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        wb.open("youtube.com")
    elif 'open google' in query:
        wb.open("google.com")
    elif 'exit' in query:
        results = query.lower()
        print(results)
        speak("System Exit")
        os.system("shutdown /s /t 1")  
    else: 
        results = query.replace("website","")
        print(results)
        speak('Web site opening....')
        wb.get().open_new(results)
    else:
         speak('I am not getting')
         print("Try again")
