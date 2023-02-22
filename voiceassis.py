import os
import speech_recognition as sr
import datetime
import pyttsx3
import webbrowser
import shutil
from urllib.request import urlopen

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Bonjour !")
    elif hour >= 12 and hour < 18 :
        speak("Bon après-midi")
    else:
        speak("Bonsoir")

    assname = ("PillPal")
    speak("Je suis ton assistant vocal")
    speak(assname)

def username():
    speak("Que dois-je vous appeler ?")
    uname = takeCommand()
    speak("Bienvenue ")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("######################".center(columns))
    print("Bienvenue ", uname.center(columns))

    speak("Comment puis-je vous aider ? ")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Recognizing")
        query = r.recognize_google(audio, language="fr-FR")
        print(f"User said: {query}\n")

    except Exception as ex:
        print(ex)
        print("Unable to recognize your voice")
        return None

    return query


if __name__== '__main__':
    clear = lambda: os.system('cls')
    clear()
    WishMe()
    username()
    assname = ("PillPal")

    while True:

        query = takeCommand().lower()
        if 'ouvre youtube' in query :
            speak("Voici le lien vers Youtube\n")
            webbrowser.open('youtube.com')
        elif 'ouvre google' in query:
            speak("Voici le lien vers Google\n")
            webbrowser.open('google.com')
        elif 'heure' in query:
            srTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"L'heure est {srTime}")
        elif 'Ça va ? ' in query:
            speak("Je vais bien, merci")
            speak("Et vous ? Vous allez bien ?")
        elif 'Bien' in query or "Oui" in query:
            speak("Parfait !")
        elif "Change mon prenom " in query :
            query = query.replace("Change mon prenom a", "")
            assname = query
        elif "change name" in query:
            speak("What whould you like to call me, Sir")
            assname = takeCommand()
            speak("Thank for naming me")
        elif "comment tu t'appelles ?" in query or "ton nom" in query:
            speak("On m'appelle ")
            speak("assname")
            print("On m'appelle", assname)
        elif 'exit' in query:
            speak("Merci pour votre temps, au revoir")
            exit()
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)
        elif 'who i am' in query:
            speak('If you talk then definitely human')



