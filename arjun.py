import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[0].id)
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning , Arjun ;\nhave nice day!")
    elif hour>=12 and hour<18:
        speak("Good after noon , arjun")
    else:
        speak("Good Evening!")

    speak("my name is arjun , how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogniging...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)
        print("say that again ...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    takeCommand()