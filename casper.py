import speech_recognition as sr
import pyttsx3
import os
from gtts import gTTS
import subprocess
import webbrowser
import wolframalpha
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)
import datetime
import playsound
import time


def casper_speaks(speak):

    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)
    engine.say(speak)
    engine.runAndWait()


def casper_listen():

    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print(Fore.GREEN + "Listening...")
        audio = rObject.listen(source, phrase_time_limit = 15)
    print("Processing...")

    try:
        text = rObject.recognize_google(audio, language='en-US')
        print(f"You: {text}")
        return text
    except:

        #casper_speaks("sorry, I don't understand, Please try again!")
        print("Sorry, I couldn't understand, Please repeat ")
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


def makeNote(take_note):

    date = datetime.datetime.now()
    note_name = str(date).replace(":", "-") + "-note.txt"
    with open(note_name, "w") as noteFile:
        noteFile.write(take_note)

    subprocess.Popen(["notepad.exe", note_name])

def say_time():

    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    casper_speaks("The time is" + hour + "Hours and" + min + "Minutes")


def open_application(command):
    if "chrome" in command:
        print("Opening Chrome")
        casper_speaks("Opening Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return

    elif "word" in command:
        print("Opening Microsoft Word")
        casper_speaks("Opening Microsoft Word")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE")
        return

    elif "excel" in command or "worksheet" in command:
        print("Opening Microsoft Excel")
        casper_speaks("Opening Microsoft Excel")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE")
        return

    elif "access" in command or "database" in command:
        print("Opening Microsoft Access")
        casper_speaks("Opening Microsoft Access")
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/MSACCESS.EXE")
        return


def knowledge(question):

    #wolframalpha api ID
    app_id = 'Q3RGAU-UWQT2U8W2J'

    client = wolframalpha.Client(app_id)
    result = client.query(question)
    answer = next(result.results).text

    print(Fore.GREEN + answer)
    casper_speaks(answer)


def Commands(command):

    try:
        if "search" in command or "YouTube" in command or "wikipedia" in command.lower():
            search_web(command)
            return

        elif "what are you" in command:
            casperIntro1 = "I'm Casper, version 1 point 1, your virtual desktop assistant."
            print(casperIntro1)
            casper_speaks(casperIntro1)
            return

        elif "who made you" in command:
            print("i was developed and modified by Ashfaaq Rifath.")
            casper_speaks("i was developed and modified by Ashfaaq Rifath.")
            return

        elif "named after" in command:
            casperIntro2 = "i was named after the famous, Casper the friendly ghost cartoon show."
            print(casperIntro2)
            casper_speaks(casperIntro2)
            return

        elif "knowledge" in command:
            print("what do you want to know about?")
            casper_speaks("what do you want to know about?")
            get_query = casper_listen()
            knowledge(get_query)
            return

        elif "write down" in command.lower():
            print("What would you like me to write down? ")
            casper_speaks("What would you like me to write down? ")
            write_note = casper_listen()
            makeNote(write_note)
            print("I've made a note of that.")
            casper_speaks("I've made a note of that.")
            return

        elif "open" in command:
            open_application(command.lower())
            return

        elif "connect" in command.lower():
            open_application(command.lower())
            return
            
        else:
            print("I can search the web for you, Do you want to continue?")
            casper_speaks("I can search the web for you, Do you want to continue?")
            answer = casper_listen()
            if "yes" in str(answer) or "yeah" in str(answer):
                search_web(command)
            else:
                return

    except:
        print("sorry, command not defined, please try again!")
        casper_speaks("sorry, command not defined, please try again!")


def search_web(command):

    if "youtube" in command.lower():
        print("what do you want to search?")
        casper_speaks("what do you want to search?")
        yt_search = casper_listen()
        print(f"searching youtube for {yt_search}")
        casper_speaks(f"searching youtube for {yt_search}")
        webbrowser.open(f"http://www.youtube.com/results?search_query={yt_search}")
        return

    elif "github" in command or "account" in command.lower():
        print("opening your GitHub account")
        casper_speaks("opening your GitHub account")
        webbrowser.open("https://github.com/ashfaaqrifath")
        return

    elif "search" in command.lower():
        indx = command.lower().split().index('search')
        query = command.split()[indx + 1:]
        casper_speaks(f"searching {query}")
        webbrowser.open(f"http://www.google.com/search?q={query}")
        return


        
if __name__ == "__main__":

    print(Fore.YELLOW + '''
    ░█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀█ 
    ░█    ░█▄▄█  ▀▀▀▄▄ ░█▄▄█ ░█▀▀▀ ░█▄▄▀ 
    ░█▄▄█ ░█ ░█ ░█▄▄▄█ ░█    ░█▄▄▄ ░█ ░█ ver 1.1.0
            VIRTUAL ASSISTANT''')

    casper_speaks("Hello, i'm Casper, your virtual assistant, how may i help you?")

    while(1):
        text = casper_listen()
        if text == 0:
            continue

        if "sleep" in str(text):
            casper_speaks("assistant power down, see you later.")
            break

        Commands(text)


#if you want to activate Casper with wake keyword, enable this code section and disable the above.

# WAKE = "casper"
#     print("Start")

#     while True:
#         print("Listening...")
#         text = casper_command()

#         if text.count(WAKE) > 0:
#             casper_speaks("I am ready")
#             text = casper_command()

#             understand(text)
