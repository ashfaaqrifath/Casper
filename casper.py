import speech_recognition as sr
import pyttsx3
import os
from gtts import gTTS
import subprocess
import webbrowser
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)
import datetime
import playsound
import time



def casper_speaks(speak):

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
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


def makeNote(the_note):
    date = datetime.datetime.now()
    note_name = str(date).replace(":", "-") + "-note.txt"
    with open(note_name, "w") as noteFile:
        noteFile.write(the_note)

    subprocess.Popen(["notepad.exe", note_name])


def open_application(input):
    if "chrome" in input:
        casper_speaks("Opening Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return

    elif "word" in input:
        casper_speaks("Opening Microsoft Word")
        os.startfile("C:/Users/ashfa/OneDrive/Desktop/Control_Panel.ink")
        return

    elif "connect" in input:
        casper_speaks("connecting wifi")
        subprocess.call([r'C:\Users\ashfa\OneDrive\Documents\Batch files\Wifi Shortcut.bat'])
        return


def commands(input):

    try:
        if "search" in input or "YouTube" in input or "wikipedia" in input.lower():
            search_web(input)
            return

        elif "what are you" in input:
            casperIntro1 = "I'm Casper, version 1 point 0, your virtual desktop assistant."
            casper_speaks(casperIntro1)
            return

        elif "who made you" in input:
            casper_speaks("i was developed and modified by Ashfaaq Rifath.")
            return

        elif "excel" in input or "spreadsheet" in input.lower():
            os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE")

        elif "write down" in input.lower():
            casper_speaks("What would you like me to write down? ")
            taking_note = casper_listen()
            makeNote(taking_note)
            casper_speaks("I've made a note of that.")
            return

        elif "open" in input:
            open_application(input.lower())
            return

        elif "connect" in input.lower():
            open_application(input.lower())
            return
            
        else:
            casper_speaks("I can search the web for you, Do you want to continue?")
            answer = casper_listen()
            if "yes" in str(answer) or "yeah" in str(answer):
                search_web(input)
            else:
                return

    except:
        casper_speaks("sorry, command not defined, please try again!")


def search_web(input):

    if "youtube" in input.lower():
        casper_speaks("what do you want to search?")
        yt_search = casper_listen()
        casper_speaks(f"searching youtube for {yt_search}")
        webbrowser.open(f"http://www.youtube.com/results?search_query={yt_search}")
        return

    elif "wikipedia" in input.lower():
        casper_speaks("what do you want to search?")
        wiki_search = casper_listen()
        casper_speaks(f"searching wikipedia for {wiki_search}")
        webbrowser.open(f"https://en.wikipedia.org/wiki/{wiki_search}")
        return

    elif "github" in input or "account" in input.lower():
        casper_speaks("opening your github account")
        webbrowser.open("https://github.com/ashfaaqrifath")
        return

    elif "search" in input.lower():
        indx = input.lower().split().index('search')
        query = input.split()[indx + 1:]
        casper_speaks(f"searching {query}")
        webbrowser.open(f"http://www.google.com/search?q={query}")
        return


        
if __name__ == "__main__":

    print(Fore.GREEN + '''
    ░█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀█ 
    ░█    ░█▄▄█  ▀▀▀▄▄ ░█▄▄█ ░█▀▀▀ ░█▄▄▀ 
    ░█▄▄█ ░█ ░█ ░█▄▄▄█ ░█    ░█▄▄▄ ░█ ░█ ver 1.0
            VIRTUAL ASSISTANT''')

    #casper_speaks("Hello, i'm Casper, your virtual assistant, how may i help you?")

    while(1):
        text = casper_listen()
        if text == 0:
            continue

        if "sleep" in str(text):
            casper_speaks("assistant power down, see you later.")
            break

        commands(text)


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