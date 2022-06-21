import speech_recognition as sr
import pyttsx3
import os
import ctypes
import subprocess
import sys
import winshell
import webbrowser
import wikipedia
import wolframalpha
import colorama
import datetime
import time
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from time import sleep
from gtts import gTTS
from speech_engine import casper_speak
from PC_functions import windows_tasks
from web_functions import search_web
from open_program import open_program
from close_program import close_program
from launch import launching
from colorama import Fore, Back
colorama.init(autoreset=True)


date = datetime.datetime.now().strftime("%h:%H:%M:%S")
log_name = str(date).replace(":", "-") + "-Log.txt"
folder = "Casper Log"
save_path = os.path.join(folder, log_name)

log_file = open(save_path, "a")
date = datetime.datetime.now()
h = "\n" + str(date) + " \n<<< CASPER ACTIVITY LOG >>> \nBEGIN LOG >>>\n \n"
log_file.write(h)
log_file.close()


def casper_log(write):
    print_save = sys.stdout
    f = open(save_path, 'a', encoding="utf-8")
    sys.stdout = f
    y = write
    y = write
    y = write

    print(y)

    sys.stdout = print_save
    f.close()

# █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

def casper_listen():
    r = sr.Recognizer()
    audio = ""
    with sr.Microphone() as source:
        # print("")
        #print(Fore.YELLOW + "Listening...".center(100))
        audio = r.listen(source, phrase_time_limit=15)
    #print(Fore.BLUE + "Processing...".center(100))
    try:
        u_said = r.recognize_google(audio, language='en-US')
        print(Fore.BLUE + "Processing...".center(100))
        print(f"(●) {u_said}".center(100))

        casper_log(Fore.BLUE + "Processing...".center(100))
        casper_log(f"(●) {u_said}".center(100))
        return u_said
    except:
        #print(Fore.LIGHTBLACK_EX + "Awaiting command.".center(100))
        return 0

# █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

def makeNote(take_note):
    date = datetime.datetime.now().strftime("%h:%H:%M:%S")
    note_name = str(date).replace(":", "-") + "-note.txt"
    with open(note_name, "w") as noteFile:
        noteFile.write(take_note)
    subprocess.Popen(["notepad.exe", note_name])

# █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

def say_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(Fore.GREEN + f"The time is {time} sir.".center(100))
    casper_speak(speak=f"The time is {time} sir.", voice=voice_engine)

    casper_log(Fore.GREEN + f"The time is {time} sir.".center(100))

# █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

def knowledge(question):
    # wolframalpha api ID
    app_id = "Q3RGAU-UWQT2U8W2J"

    client = wolframalpha.Client(app_id)
    result = client.query(question)
    wolfram_answer = next(result.results).text

    print()
    print(Fore.GREEN + wolfram_answer + "".center(100))
    casper_speak(speak=wolfram_answer, voice=voice_engine)

    casper_log("")
    casper_log(Fore.GREEN + wolfram_answer + "".center(100))

# █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

def play_music():
    print(Fore.GREEN + "Playing music from music directory".center(100))
    casper_speak(speak="Playing music from music directory", voice=voice_engine)
    music_dir = "C:/Users/ashfa/Music"
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[1]))

    casper_log(Fore.GREEN + "Playing music from music directory".center(100))
    return

# █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████


def command_engine(command):
    try:
# Internet stuff
        if "search" in command or "where is" in command or "YouTube" in command or "wikipedia" in command.lower():
            search_web(command, voice_var=voice_engine)
            return

        elif "new tab" in command or "chrome tab" in command or "incognito" in command.lower():
            search_web(command, voice_var=voice_engine)
            return

        elif "account" in command:
            search_web(command, voice_var=voice_engine)
            return

        elif "stack overflow" in command:
            search_web(command, voice_var=voice_engine)
            return

        elif "source code" in command:
            search_web(command, voice_var=voice_engine)
            return

        elif "stackoverflow" in command.lower():
            search_web(command, voice_var=voice_engine)
            return

        elif "password" in command.lower():
            subprocess.call("password_manager.py", shell=True)
            return

# WolframAlpha knowledge engine API
        elif "knowledge" in command:
            print(Fore.YELLOW + "what do you want to know about?".center(100))
            casper_speak(speak="what do you want to know about?", voice=voice_engine)
            get_query = casper_listen()
            knowledge(get_query)

            casper_log(Fore.YELLOW + "what do you want to know about?".center(100))
            return

# windows stuff
        elif "play music" in command.lower():
            play_music()
            return

        elif "write" in command or "not" in command.lower():
            print(Fore.YELLOW + "What would you like me to write down sir? ".center(100))
            casper_speak(speak="What would you like me to write down sir? ", voice=voice_engine)
            write_note = casper_listen()
            makeNote(write_note)
            print(Fore.GREEN + "I've made a note of that.".center(100))
            casper_speak(speak="I've made a note of that.", voice=voice_engine)

            casper_log(Fore.YELLOW + "What would you like me to write down sir? ".center(100))
            casper_log(Fore.GREEN + "I've made a note of that.".center(100))
            return

        elif "change background" in command.lower():
            windows_tasks(command, voice_var=voice_engine)
            return

        elif "clear" in command or "recycle" in command.lower():
            windows_tasks(command, voice_var=voice_engine)
            return

        elif "shutdown" in command.lower():
            windows_tasks(command, voice_var=voice_engine)
            return

        elif "sign out" in command or "log off" in command.lower():
            windows_tasks(command, voice_var=voice_engine)
            return

# opening applications,closing
        elif "open" in command.lower():
            open_program(command.lower(), voice_var=voice_engine)
            return

        elif "close" in command.lower():
            close_program(command.lower(), voice_var=voice_engine)
            return

        elif "activate VPN" in command:
            open_program(command, voice_var=voice_engine)
            return

        elif "task manager" in command.lower():
            open_program(command.lower(), voice_var=voice_engine)
            return

# telling the time
        elif "time" in command.lower():
            say_time()
            return

# changing the voice of Casper
        elif "voice" in command:
            print(Fore.GREEN + "Voice engine changed.".center(100))
            casper_speak(speak="Voice engine changed.", voice=voice_engine)

            casper_log(Fore.GREEN + "Voice engine changed.".center(100))

# Casper responses (hardcoded)
        elif "introduce" in command:
            casperIntro1 = "I'm Casper, version 2 point 5, your personal desktop assistant."
            print(Fore.CYAN + casperIntro1.center(100))
            casper_speak(speak=casperIntro1, voice=voice_engine)

            casper_log(Fore.CYAN + casperIntro1.center(100))

        elif "what's my name" in command or "what is my name" in command.lower():
            print(Fore.GREEN + "Your name is Ashfaaq Rifath.".center(100))
            casper_speak(speak="Your name is Ashfaaq Rifath.", voice=voice_engine)

            casper_log(Fore.GREEN + "Your name is Ashfaaq Rifath.".center(100))

        elif "who made you" in command:
            print(Fore.GREEN + "I was developed by Ashfaaq Rifath.".center(100))
            casper_speak(speak="i was developed by Ashfaaq Rifath.", voice=voice_engine)

            casper_log(Fore.GREEN + "I was developed by Ashfaaq Rifath.".center(100))

        elif "what's up" in command or "how are you" in command.lower():
            print(Fore.CYAN + "I'm fine sir, thank you for asking.".center(100))
            casper_speak(speak="i'm fine sir, thank you for asking.", voice=voice_engine)

            casper_log(Fore.CYAN + "I'm fine sir, thank you for asking.".center(100))

        elif "hi" in command or "hello" in command.lower():
            print(Fore.CYAN + "Hello sir, How can i help.".center(100))
            casper_speak(speak="Hello sir, How can i help.", voice=voice_engine)

            casper_log(Fore.CYAN + "Hello sir, How can i help.".center(100))

        elif "thank you" in command:
            print(Fore.CYAN + "You're welcome sir, I'm happy to help.".center(100))
            casper_speak(speak="You're welcome sir, i'm happy to help.", voice=voice_engine)

            casper_log(Fore.CYAN + "Hello sir, How can i help.".center(100))

        elif "useless" in command:
            print(Fore.RED + "Whatever, you're a disgrace to the human race sir.".center(100))
            casper_speak(speak="Whatever, you're a disgrace to the human race sir", voice=voice_engine)

            casper_log(Fore.RED + "Whatever, you're a disgrace to the human race sir.".center(100))

        elif "named after" in command:
            casperIntro2 = "I was named after the cat of my developer."
            print(Fore.CYAN + casperIntro2.center(100))
            casper_speak(speak=casperIntro2, voice=voice_engine)

            casper_log(Fore.CYAN + casperIntro2.center(100))

        else:
            print(Fore.RED + "Sorry sir, I didn't quite get that, please try again!".center(100))
            casper_speak(speak="Sorry sir, I didn't quite get that, please try again!", voice=voice_engine)

            casper_log(Fore.RED + "Sorry sir, I didn't quite get that, please try again!".center(100))

    except:
        print(Fore.RED + "Sorry sir, I didn't quite get that, please try again!".center(100))
        casper_speak(speak="Sorry sir, I didn't quite get that, please try again!", voice=voice_engine)

        casper_log(Fore.RED + "Sorry sir, I didn't quite get that, please try again!".center(100))

# █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████


if __name__ == "__main__":
    launching()
    voice_engine = 2

    print("")
    print('''
                                 █▀▀█  █▀▀█  █▀▀▀█  █▀▀█  █▀▀▀  █▀▀█ 
                                 █     █▄▄█  ▀▀▀▄▄  █▄▄█  █▀▀▀  █▄▄▀ 
                                 █▄▄█  █  █  █▄▄▄█  █     █▄▄▄  █  █ v2.5.0
                                 ''')

    nowTime = int(datetime.datetime.now().hour)
    if nowTime >= 0 and nowTime < 12:
        greet = "Good Morning sir, what can i do for you?"
        print(Fore.CYAN + greet.center(100))
        casper_log(Fore.CYAN + greet.center(100))

    elif nowTime >= 12 and nowTime < 18:
        greet = "Good Afternoon sir, what can i do for you?"
        print(Fore.CYAN + greet.center(100))
        casper_log(Fore.CYAN + greet.center(100))

    else:
        greet = "Good Evening sir, what can i do for you?"
        print(Fore.CYAN + greet.center(100))
        casper_log(Fore.CYAN + greet.center(100))

    casper_speak(speak=greet, voice=voice_engine)
    print("")
    print(Fore.YELLOW + "Listening...".center(100))

    casper_log(Fore.YELLOW + "Listening...".center(100))

    while(1):
        recognize = casper_listen()
        if recognize == 0:
            continue

        if "voice" in str(recognize):
            if "change" in str(recognize):
                voice_engine = 1
            if "default" in str(recognize):
                voice_engine = 2

        elif "stand by" in str(recognize):
            print(Fore.LIGHTRED_EX + "Initiated Standby Mode.".center(100))
            casper_speak(speak="initiated Standby mode.", voice=voice_engine)
            print(Fore.LIGHTBLACK_EX + "Awaiting wake command.".center(100))

            casper_log(Fore.LIGHTRED_EX + "Initiated Standby Mode.".center(100))
            casper_log(Fore.LIGHTBLACK_EX + "Awaiting wake command.".center(100))

            def standBy():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    wake = r.listen(source)
                    wake_command = ""
                try:
                    wake_command = r.recognize_google(wake)
                    print(f"(●) {wake_command}".center(100))
                    casper_log(f"(●) {wake_command}".center(100))
                except Exception as e:
                    pass
                return wake_command.lower()

            WAKE = "hello"
            while True:
                keyword = standBy()
                if keyword.count(WAKE) > 0:
                    print(Fore.LIGHTBLACK_EX + "Hello sir, how can i help".center(100))
                    casper_speak(speak="Hello sir, how can i help", voice=voice_engine)
                    print("")
                    print(Fore.YELLOW + "Listening...".center(100))
                    recognize = casper_listen()

                    casper_log(Fore.LIGHTBLACK_EX + "Hello sir, how can i help".center(100))
                    casper_log("")
                    casper_log(Fore.YELLOW + "Listening...".center(100))
                    break

        if "sleep" in str(recognize):
            print(Fore.MAGENTA + "System power down, see you later sir.".center(100))
            casper_speak(speak="System power down, see you later sir.", voice=voice_engine)

            casper_log(Fore.MAGENTA + "System power down, see you later sir.".center(100))
            casper_log("")
            casper_log("END LOG >>>")
            exit()

        command_engine(recognize)
        print("")
        print(Fore.YELLOW + "Listening...".center(100))

        casper_log("")
        casper_log(Fore.YELLOW + "Listening...".center(100))