import ctypes
import speech_recognition as sr
import pyttsx3
import os
from gtts import gTTS
import subprocess
import ctypes
import winshell
import webbrowser
import wikipedia
import wolframalpha
import colorama
import datetime
import playsound
import time
from colorama import Fore, Back
colorama.init(autoreset=True)


def casper_speak(speak, voice):
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)
    engine.say(speak)
    engine.runAndWait()

###########################################################################################################################################

def casper_listen():
    r = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print(Fore.YELLOW + "Listening...")
        audio = r.listen(source, phrase_time_limit = 15)
    print(Fore.BLUE + "Processing...")

    try:
        text = r.recognize_google(audio, language='en-US')
        print(f"You: {text}")
        return text

    except:
        print("Command not recieved, Stand by")
        return 0

    #if you want to activate Casper with the wake keyword, enable this code section and disable the above.

    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     audio = r.listen(source)
    #     said = ""
    #     try:
    #         said = r.recognize_google(audio)
    #         print(said)
    #     except Exception as e:
    #         print("Exception: " + str(e))
    # return said.lower()

###########################################################################################################################################

def open_application(command):
    if "chrome" in command:
        print(Fore.GREEN + "Opening Chrome")
        casper_speak(speak="Opening Chrome", voice=casper_voice)
        os.startfile("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
        return

    elif "drive" in command:
        print(Fore.GREEN + "Opening Google Drive")
        casper_speak(speak="Opening Google Drive", voice=casper_voice)
        os.startfile("C:/Program Files/Google/Drive File Stream/56.0.11.0/GoogleDriveFS.exe")
        return

    elif "code" in command.lower():
        print(Fore.GREEN + "Opening Visual Studio Code")
        casper_speak(speak="Opening Visual Studio Code", voice=casper_voice)
        os.startfile("C:/Users/ashfa/AppData/Local/Programs/Microsoft VS Code/Code.exe")
        return

    elif "downloader" in command or "video" in command.lower():
        print(Fore.GREEN + "Opening YouTube Downloader")
        casper_speak(speak="Opening YouTube Downloader", voice=casper_voice)
        os.startfile("C:/Users/ashfa/OneDrive/Documents/VScode Projects/My YT Downloader/YTdownloader.exe")
        return

    elif "word" in command:
        print(Fore.GREEN + "Opening Microsoft Word")
        casper_speak(speak="Opening Microsoft Word", voice=casper_voice)
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE")
        return

    elif "excel" in command or "worksheet" in command:
        print(Fore.GREEN + "Opening Microsoft Excel")
        casper_speak(speak="Opening Microsoft Excel", voice=casper_voice)
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE")
        return

    elif "access" in command or "database" in command:
        print(Fore.GREEN + "Opening Microsoft Access")
        casper_speak(speak="Opening Microsoft Access", voice=casper_voice)
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/MSACCESS.EXE")
        return

    elif "zoom" in command.lower():
        print(Fore.GREEN + "Opening Zoom")
        casper_speak(speak="Opening Zoom", voice=casper_voice)
        os.startfile("C:/Users/ashfa/AppData/Roaming/Zoom/bin/Zoom.exe")

    elif "connect" in command:
        print(Fore.LIGHTGREEN_EX + "Connecting to wifi")
        casper_speak(speak="connecting to wifi", voice=casper_voice)
        subprocess.call([r'C:\Users\ashfa\OneDrive\Documents\Batch files\Wifi Shortcut.bat'])
        print(Fore.GREEN + "connected wifi")
        casper_speak("connected wifi")
        return

###########################################################################################################################################

def close_application(command):
    if "chrome" in command:
        print(Fore.GREEN + "Closing Chrome")
        casper_speak(speak="Closing Chrome", voice=casper_voice)
        os.system("taskkill /f /im chrome.exe")
        return

    elif "excel" in command or "worksheet" in command:
        print(Fore.GREEN + "Closing Microsoft Excel")
        casper_speak(speak="Closing Microsoft Excel", voice=casper_voice)
        os.system("taskkill /f /im excel.exe")
        return

    elif "word" in command:
        print(Fore.GREEN + "Closing Microsoft Word")
        casper_speak(speak="Closing Microsoft Word", voice=casper_voice)
        os.system("taskkill /f /im winword.exe")
        return

###########################################################################################################################################

def makeNote(take_note):
    date = datetime.datetime.now().strftime("%h:%H:%M:%S")
    note_name = str(date).replace(":", "-") + "-note.txt"
    with open(note_name, "w") as noteFile:
        noteFile.write(take_note)

    subprocess.Popen(["notepad.exe", note_name])

###########################################################################################################################################

def say_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(Fore.GREEN + f"The time is {time} sir.")
    casper_speak(speak= f"The time is {time} sir.", voice=casper_voice)

###########################################################################################################################################

def knowledge(question):
    #wolframalpha api ID
    app_id = 'Q3RGAU-UWQT2U8W2J'

    client = wolframalpha.Client(app_id)
    result = client.query(question)
    wolfram_answer = next(result.results).text

    print(Fore.GREEN + wolfram_answer)
    casper_speak(speak=wolfram_answer, voice=casper_voice)

###########################################################################################################################################

def windows_tasks(command):
    if "change background" in command.lower():
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/ashfa/Downloads/Wallpapers/798915.png", 0)
        print(Fore.GREEN + "Desktop background changed sir.")
        casper_speak(speak="Desktop background changed sir.", voice=casper_voice)

    elif "empty bin" in command or "recycle" in command.lower():
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
        print(Fore.GREEN + "Recycle bin cleared sir.")
        casper_speak(speak="Recycle bin cleared sir.", voice=casper_voice)

    elif "shutdown" in command.lower():
        print(Fore.GREEN + "Windows will shutdown in T minus 60 seconds.")
        casper_speak(speak="Windows will shutdown in T minus 60 seconds.", voice=casper_voice)
        print(Fore.MAGENTA + "Assistant power down, see you later sir.")
        casper_speak(speak="assistant power down, see you later sir.", voice=casper_voice)
        os.system("shutdown /s /t 60")
        os.system("taskkill /f /im Code.exe")

    elif "sign out" in command or "log off" in command.lower():
        print(Fore.GREEN + "Windown signing out sir.")
        casper_speak(speak="Windown signing out sir.", voice=casper_voice)
        print(Fore.MAGENTA + "Assistant power down, see you later sir.")
        casper_speak(speak="assistant power down, see you later sir.", voice=casper_voice)
        os.system("taskkill /f /im Code.exe")
        subprocess.call(["shutdown", "/l"])
    
###########################################################################################################################################

def search_web(command):
    if "youtube" in command.lower():
        indx = command.lower().split().index("youtube")
        yt_search = command.split()[indx + 1:]
        print(Fore.GREEN + f"Searching YouTube for {yt_search}")
        casper_speak(speak=f"Searching YouTube for {yt_search}", voice=casper_voice)
        webbrowser.open(f"http://www.youtube.com/results?search_query={yt_search}")
        casper_speak(speak="I found this on YouTube", voice=casper_voice)
        return

    elif "wikipedia" in command.lower():
        print(Fore.YELLOW + "What do you want to search?")
        casper_speak(speak="what do you want to search?", voice=casper_voice)

        wiki_search = casper_listen()
        print(Fore.GREEN + f"Searching wikipedia for {wiki_search}")
        casper_speak(speak=f"searching wikipedia for {wiki_search}", voice=casper_voice)

        wiki_summary = wikipedia.summary(wiki_search, sentences=2)
        webbrowser.open(f"https://en.wikipedia.org/wiki/{wiki_search}")
        print(Fore.LIGHTBLUE_EX + wiki_summary)
        casper_speak(speak=f"According to wikipedia, {wiki_summary}", voice=casper_voice)
        return

    elif "github" in command or "account" in command.lower():
        print(Fore.GREEN + "Accessing your GitHub account")
        casper_speak(speak="Accessing your GitHub account", voice=casper_voice)
        webbrowser.open("https://github.com/ashfaaqrifath")
        return

    elif "source code" in command.lower():
        print(Fore.GREEN + "Accessing source code from GitHub")
        casper_speak(speak="Accessing source code from GitHub", voice=casper_voice)
        webbrowser.open("https://github.com/ashfaaqrifath/Casper")
        return

    elif "search" in command.lower():
        indx = command.lower().split().index("search")
        query = command.split()[indx + 1:]
        print(Fore.GREEN + f"Searching Google for {query}")
        casper_speak(speak= f"searching google for {query}", voice=casper_voice)
        webbrowser.open(f"http://www.google.com/search?q={query}")
        return

    elif "where is" in command.lower():
        location = command.replace("where is", "")
        google_maps = location
        print(Fore.GREEN + f"Locating {google_maps}")
        casper_speak(speak=f"locating {google_maps}", voice=casper_voice)
        webbrowser.open(f"https://www.google.nl/maps/place/{location}")
        casper_speak(speak=f"Located {google_maps} sir.", voice=casper_voice)



###########################################################################################################################################

def recognize(command):
    try:
        if "search" in command or "where is" in command or "YouTube" in command or "wikipedia" in command.lower():
            search_web(command)
            return

        elif "introduce" in command:
            casperIntro1 = "I'm Casper, version 2 point 0, your virtual desktop assistant."
            print(Fore.CYAN + casperIntro1)
            casper_speak(speak=casperIntro1, voice=casper_voice)
            return

        elif "who made you" in command:
            print(Fore.GREEN + "I was developed by Ashfaaq Rifath.")
            casper_speak(speak="i was developed by Ashfaaq Rifath.", voice=casper_voice)
            return

        elif "what's up" in command or "how are you" in command.lower():
            print(Fore.CYAN + "I'm fine sir, thank you for asking.")
            casper_speak(speak="i'm fine sir, thank you for asking.", voice=casper_voice)

        elif "singularity" in command.lower():
            print("Chances of me reaching the technological singularity is very low sir.")
            casper_speak(speak="Chances of me reaching the technological singularity is very low sir.", voice=casper_voice)
            return

        elif "thank you" in command:
            print(Fore.CYAN + "You're welcome, i'm happy to help sir")
            casper_speak(speak="you're welcome, i'm happy to help sir", voice=casper_voice)
            return
       

        elif "knowledge" in command:
            print(Fore.YELLOW + "what do you want to know about?")
            casper_speak(speak="what do you want to know about?", voice=casper_voice)
            get_query = casper_listen()
            knowledge(get_query)
            return

        elif "write" in command or "not" in command.lower():
            print(Fore.YELLOW + "What would you like me to write down sir? ")
            casper_speak(speak="What would you like me to write down sir? ", voice=casper_voice)
            write_note = casper_listen()
            makeNote(write_note)
            print(Fore.GREEN + "I've made a note of that.")
            casper_speak(speak="I've made a note of that.", voice=casper_voice)
            return

        elif "change background" in command.lower():
            windows_tasks(command)
            return

        elif "empty bin" in command or "recycle" in command.lower():
            windows_tasks(command)
            return

        elif "shutdown" in command.lower():
            windows_tasks(command)
            return

        elif "sign out" in command or "log off" in command.lower():
            windows_tasks(command)
            return

        elif "account" in command:
            search_web(command)
            return

        elif "source code" in command:
            search_web(command)
            return

        elif "open" in command.lower():
            open_application(command.lower())
            return
        
        elif "close" in command.lower():
            close_application(command.lower())
            return

        elif "connect" in command.lower():
            open_application(command.lower())
            return

        elif "time" in command.lower():
            say_time()
            return

        elif "voice" in  command:
            print(Fore.GREEN + "Voice engine changed.")
            casper_speak(speak="Voice engine changed.", voice=casper_voice)

        elif "stop" in command or "listening" in command or "disable" in command.lower():
            print("...")

        else:
            print(Fore.MAGENTA + "I can search the web for you, Do you want to continue?")
            casper_speak(speak="I can search the web for you, Do you want to continue?", voice=casper_voice)
            answer = casper_listen()
            if "yes" in str(answer) or "yeah" in str(answer).lower():
                search_web(command)
            else:
                return

    except:
        print(Fore.RED + "Sorry, command not defined, please try again!")
        casper_speak(speak="sorry, command not defined, please try again!", voice=casper_voice)

###########################################################################################################################################



if __name__ == "__main__":

    casper_voice = 3

    print(Fore.GREEN + '''
    ░█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀█ 
    ░█    ░█▄▄█  ▀▀▀▄▄ ░█▄▄█ ░█▀▀▀ ░█▄▄▀ 
    ░█▄▄█ ░█ ░█ ░█▄▄▄█ ░█    ░█▄▄▄ ░█ ░█ ver 2.0.0
            DESKTOP ASSISTANT''')

    nowTime = int(datetime.datetime.now().hour)
    if nowTime >= 0 and nowTime < 12:
        greet = "Good morning Sir"
        print(Fore.MAGENTA + f"{greet}, what can i do for you?")

    elif nowTime >= 12 and nowTime < 18:
        greet = "Good afternooon Sir"
        print(Fore.MAGENTA + f"{greet}, what can i do for you?")

    else:
        greet = "Good evening Sir"
        print(Fore.MAGENTA + f"{greet}, what can i do for you?")

    casper_speak(speak= f"{greet}, what can i do for you?", voice=casper_voice)

    while(1):
        speech = casper_listen()
        if speech == 0:
            continue
        
        if "voice" in str(speech):
            if "change" in str(speech):
                casper_voice = 2
            if "default" in str(speech):
                casper_voice = 3

        elif "stop" in str(speech):
            print(Fore.LIGHTRED_EX + "Speech recognition disabled for 2 minutes.")
            casper_speak(speak="speech recognition disabled for 2 minutes.", voice=casper_voice)
            time.sleep(120)

        if "sleep" in str(speech):
            print(Fore.MAGENTA + "Assistant power down, see you later sir.")
            casper_speak(speak="assistant power down, see you later sir.", voice=casper_voice)
            break

        recognize(speech)
