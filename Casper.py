import os
import subprocess
import sys
from numpy import void
import winsound
import wolframalpha
import colorama
import datetime
import time
import sounddevice as sd
import speech_recognition as sr
import ctypes
import shutil
import webbrowser
import pyaudio
from pathlib import Path
from speech_engine import casper_speak
from system_functions import system_task
from web_functions import surf_web
from app_functions import open_program, close_program
from newsAPI import news_BBC, news_category
from activity_log import casper_log
from YTdownlaoder import yt_downldr
from datetime import date
from scipy.io.wavfile import write
from gtts import gTTS
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from colorama import Fore, Back
colorama.init(autoreset=True)


date = datetime.datetime.now().strftime("%h:%H:%M:%S")
act_log = str(date).replace(":", "-") + "-Log.txt"
audio_log = str(date).replace(":", "-") + "-Audio.wav"

folder = "Casper Log"
save_path = os.path.join(folder, act_log)
folderB = "Casper Log"
save_pathB = os.path.join(folder, audio_log)

log_file = open(save_path, "a")
date = datetime.datetime.now()

blanket = 0

casper_log(write="CASPER - DESKTOP ASSISTANT v3.0.0\n" +
str(date) + " \n<<< ACTIVITY LOG >>> \nBEGIN LOG >>>\n \n", var=blanket)

##################################################################################################

def casper_listen():
    r = sr.Recognizer()
    audio = ""
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=15)
    try:
        u_said = r.recognize_google(audio, language='en-US')
        print(f"(●) {u_said}".center(100))
        print(Fore.GREEN + "Processing...".center(100))
        print()

        casper_log(f"(●) {u_said}".center(100), var=blanket)
        casper_log(Fore.BLUE + "Processing...".center(100), var=blanket)
        return u_said
    except:
        return 0

##################################################################################################

def make_note(take_note):
    date = datetime.datetime.now().strftime("%h:%H:%M:%S")
    note_name = str(date).replace(":", "-") + "-note.txt"
    save_path = Path('Notes')

    if save_path.is_dir():
        with open(save_path.joinpath(note_name), 'w') as f:
            f.write(take_note)
    else:
        print("Directory doesn't exist")

##################################################################################################

def say_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(Fore.GREEN + f"The time is {time} sir".center(100))
    casper_speak(speak=f"The time is {time} sir", voice=voice_engine)
    casper_log(Fore.GREEN + f"The time is {time} sir".center(100), var=blanket)

##################################################################################################

def say_date():
    day = datetime.datetime.now()
    d1 = day.strftime("%A")

    date = datetime.datetime.now()
    d = date.strftime("%d")

    month = datetime.datetime.now()
    m = month.strftime("%B")

    year = datetime.datetime.now()
    y = year.strftime("%Y")

    full = d1, d, m, y
    x = str(full)
    char = ",()'"

    for c in char:
        x = x.replace(c, "")
    print(Fore.GREEN + f"Today is {x} sir".center(100))
    casper_speak(speak=f"Today is {x} sir", voice=voice_engine)

##################################################################################################

def set_timer(countdown):
    while countdown:
        mins, secs = divmod(countdown, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r".center(100))
        time.sleep(1)
        countdown = countdown - 1
    set_timer(countdown)

##################################################################################################

def knowledge_engine(question):
    api_key = "Q3RGAU-UWQT2U8W2J"

    client = wolframalpha.Client(api_key)
    result = client.query(question)
    wolfram_answer = str(next(result.results).text)
    print()
    print(Fore.GREEN + wolfram_answer.center(100))
    casper_speak(speak=wolfram_answer, voice=voice_engine)
    casper_log("", var=blanket)
    casper_log(Fore.GREEN + wolfram_answer.center(100), var=blanket)

##################################################################################################

def play_music():
    print(Fore.GREEN + "Playing music from music directory".center(100))
    casper_speak(speak="Playing music from music directory", voice=voice_engine)
    music_dir = "C:/Users/ashfa/Music"
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[1]))
    casper_log(Fore.GREEN + "Playing music from music directory".center(100), var=blanket)
    return

##################################################################################################

def command_engine(command):
    global blanket

    try:
        # Internet tasks
        if "search" in command or "locate" in command or "YouTube" in command or "Wikipedia" in command.lower():
            surf_web(command, voice_var=voice_engine, log=blanket)
            return

        elif "new tab" in command or "chrome tab" in command or "incognito" in command.lower():
            surf_web(command, voice_var=voice_engine, log=blanket)
            return

        elif "account" in command:
            surf_web(command, voice_var=voice_engine, log=blanket)
            return

        elif "stack overflow" in command:
            surf_web(command, voice_var=voice_engine, log=blanket)
            return

        elif "google news" in command.lower():
            surf_web(command, voice_var=voice_engine, log=blanket)
            return

        elif "source code" in command:
            surf_web(command, voice_var=voice_engine, log=blanket)
            return

        elif "stackoverflow" in command.lower():
            surf_web(command, voice_var=voice_engine, log=blanket)
            return

# NewsAPI
        elif "headlines" in command.lower():
            news_BBC(voice_var=voice_engine, log=blanket)
            return

        elif "news category" in command.lower():
            news_category(voice_var=voice_engine, log=blanket)
            return

# WolframAlpha knowledge engine API
        elif "knowledge" in command:
            print(Fore.YELLOW + "what do you want to know about?".center(100))
            casper_speak(speak="what do you want to know about?", voice=voice_engine)
            get_query = casper_listen()
            knowledge_engine(get_query)
            casper_log(Fore.YELLOW + "what do you want to know about?".center(100), var=blanket)
            return

# windows tasks
        elif "play music" in command.lower():
            play_music()
            return

        elif "write" in command or "not" in command.lower():
            print(Fore.YELLOW + "What would you like me to write down sir? ".center(100))
            casper_speak(speak="What would you like me to write down sir? ", voice=voice_engine)
            write_note = casper_listen()
            write_note(make_note)
            print(Fore.GREEN + "I've made a note of that".center(100))
            casper_speak(speak="I've made a note of that", voice=voice_engine)

            casper_log(Fore.YELLOW + "What would you like me to write down sir? ".center(100), var=blanket)
            casper_log(Fore.GREEN + "I've made a note of that".center(100), var=blanket)
            return

        elif "change background" in command.lower():
            system_task(command, voice_var=voice_engine, log=blanket)
            return

        elif "clear" in command or "recycle" in command.lower():
            system_task(command, voice_var=voice_engine, log=blanket)
            return

        elif "shutdown" in command.lower():
            system_task(command, voice_var=voice_engine, log=blanket)
            return

        elif "sign out" in command or "log out" in command.lower():
            system_task(command, voice_var=voice_engine, log=blanket)
            return

# opening, closing programs
        elif "open" in command.lower():
            open_program(command.lower(), voice_var=voice_engine, log=blanket)
            return

        elif "close" in command.lower():
            close_program(command.lower(), voice_var=voice_engine, log=blanket)
            return

        elif "activate VPN" in command:
            open_program(command, voice_var=voice_engine, log=blanket)
            return

        elif "task manager" in command.lower():
            open_program(command.lower(), voice_var=voice_engine, log=blanket)
            return

        elif "download" in command.lower():
            yt_downldr()
            return

# Casper tasks
        elif "voice" in command or "change voice" in command:
            print(Fore.GREEN + "Voice engine changed".center(100))
            casper_speak(speak="Voice engine changed", voice=voice_engine)
            casper_log(Fore.GREEN + "Voice engine changed".center(100), var=blanket)

        elif "blanket" in command:
            print(Fore.RED + "<<< INITIATED BLANKET MODE >>>".center(100))
            casper_speak(speak="INITIATED BLANKET MODE", voice=voice_engine)
            casper_log("<<< INITIATED BLANKET MODE >>>".center(100), var=blanket)
            casper_log("Activity logging disabled".center(100), var=blanket)
            casper_log("END LOG >>>", var=blanket)
            blanket += 1

        elif "delete" in command or "log files" in command:
            print(Fore.RED + "<<< INITIATING DELETION PROTOCOL >>>".center(100))
            casper_speak(speak="INITIATING DELETION PROTOCOL", voice=voice_engine)

            mydir = "Casper Log"
            filelist = [f for f in os.listdir(mydir) if f.endswith(".txt")]
            for f in filelist:
                os.remove(os.path.join(mydir, f))
            time.sleep(1)
            print(Fore.GREEN + "All activity log files has been deleted".center(100))
            casper_speak(speak="All activity log files has been deleted", voice=voice_engine)

        elif "timer" in command.lower():
            print(Fore.YELLOW + "For how long sir ?".center(100))
            casper_speak(speak="For how long sir ?", voice=voice_engine)
            t = casper_listen()
            if "minutes" in t:
                t = t.replace("minutes", "")
                m = int(t) * 60
                set_timer(int(m))

            if "seconds" in t:
                t = t.replace("seconds", "")
                set_timer(int(t))
            return

        elif "record" in command or "record mode" in command:
            print(Fore.RED + "<<< INITIATED RECORDING MODE >>>".center(100))
            casper_speak(speak="INITIATED RECORDING MODE", voice=voice_engine)
            casper_log(Fore.RED + "<<< INITIATED RECORDING MODE >>>".center(100), var=blanket)

            frequency = 44100
            duration = 300
            record_audio = sd.rec(int(duration * frequency), samplerate=frequency, channels=2)
            sd.wait()
            write(save_pathB, frequency, record_audio)
            print(Fore.GREEN + "Recoding audio completed".center(100))
            casper_log(Fore.GREEN + "Recording audio completed".center(100), var=blanket)
            casper_speak(speak="Recording audio completed", voice=voice_engine)

        elif "date" in command.lower():
            say_date()
            return

        elif "beep" in command.lower():
            for b in range(3):
                winsound.Beep(2500, 500)

        elif "time" in command.lower():
            say_time()
            return

# Casper responses (hardcoded)
        elif "introduce" in command:
            print(Fore.CYAN + "I'm Casper, version 2 point 6, your personal desktop assistant.".center(100))
            casper_speak(speak="I'm Casper, version 2 point 6, your personal desktop assistant.", voice=voice_engine)
            casper_log(Fore.CYAN + "I'm Casper, version 2 point 6, your personal desktop assistant.".center(100), var=blanket)

        elif "what's my name" in command or "what is my name" in command.lower():
            print(Fore.GREEN + "Your name is Ashfaaq Rifath.".center(100))
            casper_speak(speak="Your name is Ashfaaq Rifath.", voice=voice_engine)
            casper_log(Fore.GREEN + "Your name is Ashfaaq Rifath.".center(100), var=blanket)

        elif "who made you" in command:
            print(Fore.GREEN + "I was developed by Ashfaaq Rifath as a flagship project.".center(100))
            casper_speak(speak="i was developed by Ashfaaq Rifath as a flagship project.", voice=voice_engine)
            casper_log(Fore.GREEN + "I was developed by Ashfaaq Rifath as a flagship project.".center(100), var=blanket)

        elif "what's up" in command or "how are you" in command.lower():
            print(Fore.CYAN + "I'm fine sir, thank you for asking".center(100))
            casper_speak(speak="i'm fine sir, thank you for asking", voice=voice_engine)
            casper_log(Fore.CYAN + "I'm fine sir, thank you for asking".center(100), var=blanket)

        elif "hi" in command or "hello" in command.lower():
            print(Fore.CYAN + "Hello sir, How can i help".center(100))
            casper_speak(speak="Hello sir, How can i help", voice=voice_engine)
            casper_log(Fore.CYAN + "Hello sir, How can i help".center(100), var=blanket)

        elif "thank you" in command:
            print(Fore.CYAN + "You're welcome sir, I'm happy to help".center(100))
            casper_speak(speak="You're welcome sir, i'm happy to help", voice=voice_engine)
            casper_log(Fore.CYAN + "You're welcome sir, i'm happy to help".center(100), var=blanket)

        elif "useless" in command:
            print(Fore.RED + "Whatever, you're a disgrace to the human race sir".center(100))
            casper_speak(speak="Whatever, you're a disgrace to the human race sir", voice=voice_engine)
            casper_log(Fore.RED + "Whatever, you're a disgrace to the human race sir".center(100), var=blanket)

        elif "named after" in command:
            print(Fore.CYAN + "I was named after the cat of my developer.".center(100))
            casper_speak(speak="I was named after the cat of my developer.", voice=voice_engine)
            casper_log(Fore.CYAN + "I was named after the cat of my developer.".center(100), var=blanket)

        else:
            print(Fore.RED + "Sorry sir, I didn't quite get that, please try again".center(100))
            casper_speak(speak="Sorry sir, I didn't quite get that, please try again", voice=voice_engine)
            casper_log(Fore.RED + "Sorry sir, I didn't quite get that, please try again".center(100), var=blanket)

    except RecursionError:
        for b in range(3):
            winsound.Beep(2500, 500)
        print(Fore.GREEN + "Countdown completed".center(5))
        casper_speak(speak="Countdown completed", voice=voice_engine)
    except:
        print(Fore.RED + "Sorry sir, I didn't quite get that, please try again !".center(100))
        casper_speak(speak="Sorry sir, I didn't quite get that, please try again !", voice=voice_engine)

        casper_log(Fore.RED + "Sorry sir, I didn't quite get that, please try again !".center(100), var=blanket)

###################################################################################################################

if __name__ == "__main__":
    # os.system('cmd /c "CasperIntro.gif"')
    # time.sleep(4.5)
    # os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system('cls')

    voice_engine = 2

    print("")
    print('''
                                 █▀▀█  █▀▀█  █▀▀▀█  █▀▀█  █▀▀▀  █▀▀█ 
                                 █     █▄▄█  ▀▀▀▄▄  █▄▄█  █▀▀▀  █▄▄▀ 
                                 █▄▄█  █  █  █▄▄▄█  █     █▄▄▄  █  █ v2.6.0
                                 ''')

    nowTime = int(datetime.datetime.now().hour)
    if nowTime >= 0 and nowTime < 12:
        greet = "Good Morning sir, how may i help you ?"
        print(Fore.CYAN + greet.center(100))
        casper_log(Fore.CYAN + greet.center(100), var=blanket)

    elif nowTime >= 12 and nowTime < 18:
        greet = "Good Afternoon sir, how may i help you ?"
        print(Fore.CYAN + greet.center(100))
        casper_log(Fore.CYAN + greet.center(100), var=blanket)

    else:
        greet = "Good Evening sir, how may i help you ?"
        print(Fore.CYAN + greet.center(100))
        casper_log(Fore.CYAN + greet.center(100), var=blanket)

    casper_speak(speak=greet, voice=voice_engine)
    print("")
    print(Fore.YELLOW + "Listening...".center(100))

    casper_log(Fore.YELLOW + "Listening...".center(100), var=blanket)

    while(1):
        recognize = casper_listen()
        if recognize == 0:
            continue

        if "voice" in str(recognize):
            if "voice" in str(recognize):
                voice_engine = 1
            if "default" in str(recognize):
                voice_engine = 2

        elif "stand by" in str(recognize):
            print(Fore.RED + "<<< INITIATED STANDBY MODE >>>".center(100))
            casper_speak(speak="initiated standby mode", voice=voice_engine)
            print(Fore.LIGHTBLACK_EX + "Awaiting wake command".center(100))

            casper_log(
                Fore.RED + "<<< INITIATED STANDBY MODE >>>".center(100), var=blanket)
            casper_log(Fore.LIGHTBLACK_EX + "Awaiting wake command".center(100), var=blanket)

            def standby_mode():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    wake = r.listen(source)
                    wake_command = ""
                try:
                    wake_command = r.recognize_google(wake)
                    print(Fore.LIGHTBLACK_EX + f"(●) {wake_command}".center(100))
                    casper_log(f"(●) {wake_command}".center(100), var=blanket)
                except Exception as e:
                    pass
                return wake_command.lower()

            WAKE = "active"
            while True:
                keyword = standby_mode()
                if keyword.count(WAKE) > 0:
                    print("Welcome back sir, how can i help ?".center(100))
                    casper_speak(speak="Welcome back sir, how can i help ?", voice=voice_engine)
                    print("")
                    print(Fore.YELLOW + "Listening...".center(100))
                    recognize = casper_listen()

                    casper_log("Welcome back sir, how can i help ?".center(100), var=blanket)
                    casper_log("", var=blanket)
                    casper_log(Fore.YELLOW + "Listening...".center(100), var=blanket)
                    break

        if "sleep" in str(recognize):
            print(Fore.MAGENTA + "Assistant shutdown, see you later sir".center(100))
            casper_speak(speak="Assistant shutdown, see you later sir", voice=voice_engine)
            casper_log(Fore.MAGENTA + "Assistant shutdown, see you later sir".center(100), var=blanket)
            casper_log("", var=blanket)
            casper_log("END LOG >>>", var=blanket)
            exit()

        command_engine(recognize)
        print("")
        print(Fore.YELLOW + "Listening...".center(100))

        casper_log("", var=blanket)
        casper_log(Fore.YELLOW + "Listening...".center(100), var=blanket)






# <<< Copyright (c) 2022 Ashfaaq Rifath - Casper v2.6.0 >>>
