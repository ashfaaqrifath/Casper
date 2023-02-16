import os
import subprocess
import sys
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
from numpy import void
from speech_engine import casper_speak
from system_functions import system_task
from web_functions import surf_web
from program_functions import open_program, close_program
from newsAPI import news_BBC, news_category
from chronicle_engine import chronicle_audio, chronicle_log, clean_slate
from GPT3_model import GPT3
from message_functions import casper_alert, telegram_text, whatsapp_text
from datetime import date
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
log_file.close()

stealth = 0
input_source = 0

chronicle_log(write="CASPER - DESKTOP ASSISTANT v2.7.3\n" +
           str(date) + " \n<<< ACTIVITY LOG >>> \nBEGIN LOG >>>\n \n", var=stealth)

##################################################################################################

def casper_input():
    if input_source == 1:
        print()
        text = input(Fore.CYAN + "                                    Enter prompt: ")
        
        try:
            u_said = text
            print(Fore.LIGHTBLACK_EX + "Processing...".center(100))
            print()
            chronicle_log(f"[text] {u_said}".center(100), var=stealth)
            chronicle_log(Fore.LIGHTBLACK_EX + "Processing...".center(100), var=stealth)
            return u_said
        except:
            return 0

    else:
        r = sr.Recognizer()
        audio = ""
        with sr.Microphone() as source:
            audio = r.listen(source, phrase_time_limit=15)
        try:
            u_said = r.recognize_google(audio, language='en-US')
            print(f"(●) {u_said}".center(100))
            print(Fore.LIGHTBLACK_EX + "Processing...".center(100))
            print()

            chronicle_log(f"(●) {u_said}".center(100), var=stealth)
            chronicle_log(Fore.LIGHTBLACK_EX + "Processing...".center(100), var=stealth)
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
        print(Fore.RED + "Directory doesn't exist")

##################################################################################################

def say_time():
    time = datetime.datetime.now().strftime("%H:%M")

    if nowTime >= 0 and nowTime < 12:
        print(Fore.GREEN + f"The time is {time} AM sir".center(100))
        casper_speak(speak=f"The time is {time} AM sir", voice=voice_engine)
        chronicle_log(Fore.GREEN + f"The time is {time} AM sir".center(100), var=stealth)

    elif nowTime >= 12 and nowTime < 18:
        print(Fore.GREEN + f"The time is {time} PM sir".center(100))
        casper_speak(speak=f"The time is {time} PM sir", voice=voice_engine)
        chronicle_log(Fore.GREEN + f"The time is {time} PM sir".center(100), var=stealth)

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
    chronicle_log(Fore.GREEN + f"Today is {x} sir".center(100), var=stealth)

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

def wolfram_API(question):
    api_key = "YOUR API KEY"
    client = wolframalpha.Client(api_key)
    result = client.query(question)
    wolfram_answer = str(next(result.results).text)
    print()
    print(Fore.GREEN + wolfram_answer.center(100))
    casper_speak(speak=wolfram_answer, voice=voice_engine)
    chronicle_log("", var=stealth)
    chronicle_log(Fore.GREEN + wolfram_answer.center(100), var=stealth)

##################################################################################################

def play_music():
    print(Fore.GREEN + "Playing music from music directory".center(100))
    casper_speak(speak="Playing music from music directory", voice=voice_engine)
    music_dir = "C:/Users/ashfa/Music"
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[1]))
    chronicle_log(Fore.GREEN + "Playing music from music directory".center(100), var=stealth)
    return

##################################################################################################

def command_engine(command): #The heart of Casper
    global stealth
    global input_source

    try:
        # Internet tasks
        if "search" in command or "YouTube" in command or "google news" in command.lower():
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

        elif "gmail" in command.lower():
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

        elif "Wikipedia" in command:
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

        elif "locate" in command.lower():
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

        elif "new tab" in command or "chrome tab" in command or "incognito" in command.lower():
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

        elif "account" in command.lower():
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

        elif "facebook" in command.lower():
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

        elif "instagram" in command.lower():
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

        elif "twitter" in command.lower():
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

        elif "stack overflow" in command.lower():
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

        elif "google news" in command.lower():
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

        elif "source code" in command.lower():
            surf_web(command, voice_var=voice_engine, log=stealth)
            return

    # NewsAPI
        elif "headlines" in command.lower():
            news_BBC(voice_var=voice_engine, log=stealth)
            return

        elif "news category" in command.lower():
            news_category(voice_var=voice_engine, log=stealth)
            return

    # GPT3 language model API
        elif "test" in command.lower():
            print(Fore.GREEN + "<<< ACTIVATED GPT3 MODEL >>>".center(100))
            casper_speak(speak="ACTIVATED GPT3 MODEL", voice=voice_engine)
            casper_alert("ACTIVATED GPT3 MODEL")
            print()
            print(Fore.LIGHTBLACK_EX + "<< GPT-3 artificial intelligence language model desgned by OpenAI >>".center(100))
            print(Fore.YELLOW + "Hello I'm GPT3 language model how may i be of service?".center(100))
            casper_speak(speak="Hello, I'm GPT3 language model, how may i be of service?", voice=voice_engine)
            get_prompt = casper_input()
            GPT3(usr_prompt=get_prompt, voice_var=voice_engine, log=stealth)

    # WolframAlpha knowledge engine API
        elif "knowledge" in command:
            print(Fore.YELLOW + "What would you like to know about?".center(100))
            casper_speak(speak="What would you like to know about?", voice=voice_engine)
            get_query = casper_input()
            wolfram_API(get_query)
            chronicle_log(Fore.YELLOW + "What would you like to know about?".center(100), var=stealth)
            return

    # windows tasks
        elif "play music" in command.lower():
            play_music()
            return

        elif "write" in command.lower():
            print(Fore.YELLOW + "What would you like me to write down sir? ".center(100))
            casper_speak(speak="What would you like me to write down sir? ", voice=voice_engine)
            write_note = casper_input()
            make_note(write_note)
            print(Fore.GREEN + "I've made a note of that".center(100))
            casper_speak(speak="I've made a note of that", voice=voice_engine)

            chronicle_log(Fore.YELLOW + "What would you like me to write down sir? ".center(100), var=stealth)
            chronicle_log(Fore.GREEN + "I've made a note of that".center(100), var=stealth)
            return

        elif "change background" in command.lower():
            system_task(command, voice_var=voice_engine, log=stealth)
            return

        elif "clear" in command or "recycle" in command.lower():
            system_task(command, voice_var=voice_engine, log=stealth)
            return

        elif "shutdown" in command.lower():
            system_task(command, voice_var=voice_engine, log=stealth)
            return

        elif "sign out" in command or "log out" in command.lower():
            system_task(command, voice_var=voice_engine, log=stealth)
            return

    # opening, closing programs
        elif "open" in command.lower():
            open_program(command.lower(), voice_var=voice_engine, log=stealth)
            return

        elif "close" in command.lower():
            close_program(command.lower(), voice_var=voice_engine, log=stealth)
            return

        elif "activate VPN" in command:
            open_program(command, voice_var=voice_engine, log=stealth)
            return

        elif "task manager" in command.lower():
            open_program(command.lower(), voice_var=voice_engine, log=stealth)
            return

    # Casper tasks
        elif "voice" in command or "change voice" in command:
            print(Fore.GREEN + "Voice engine changed".center(100))
            casper_speak(speak="Voice engine changed", voice=voice_engine)
            chronicle_log(Fore.GREEN + "Voice engine changed".center(100), var=stealth)
            casper_alert("VOICE ENGINE CHANGED")

        elif "enable stealth" in command:
            print(Fore.RED + "<<< INITIATED STEALTH MODE >>>".center(100))
            casper_speak(speak="INITIATED STEALTH MODE", voice=voice_engine)
            chronicle_log("<<< INITIATED STEALTH MODE >>>".center(100), var=stealth)
            chronicle_log("Activity logging disabled".center(100), var=stealth)
            casper_alert("INITIATED STEALTH MODE")
            chronicle_log("END LOG >>>", var=stealth)
            stealth += 1

        elif "text" in command:
            print(Fore.GREEN + "<<< INITIATED TEXT INPUT MODE >>>".center(100))
            casper_speak(speak="INITIATED TEXT INPUT MODE", voice=voice_engine)
            chronicle_log("<<< INITIATED TEXT INPUT MODE >>>".center(100), var=stealth)
            casper_alert("INITIATED TEXT INPUT MODE")
            input_source += 1

        elif "disable stealth" in command:
            print(Fore.RED + "<<< DISABLED STEALTH MODE >>>".center(100))
            casper_speak(speak="DISABLED STEALTH MODE", voice=voice_engine)
            chronicle_log("<<< DISABLED STEALTH MODE >>>".center(100), var=stealth)
            chronicle_log("Activity logging disabled".center(100), var=stealth)
            casper_alert("DISABLED STEALTH MODE")
            chronicle_log("START LOG >>>", var=stealth)
            stealth = 0

        elif "delete log" in command or "clean slate" in command:
            clean_slate(voice_var=voice_engine)

        elif "timer" in command.lower():
            print(Fore.YELLOW + "For how long sir ?".center(100))
            casper_speak(speak="For how long sir ?", voice=voice_engine)
            chronicle_log(Fore.YELLOW + "For how long sir ?".center(100), var=stealth)
            t = casper_input()
            if "minutes" in t:
                t = t.replace("minutes", "")
                m = int(t) * 60
                set_timer(int(m))

            if "seconds" in t:
                t = t.replace("seconds", "")
                set_timer(int(t))
            return

        elif "record" in command or "chronicle audio" in command:
            chronicle_audio(voice_var=voice_engine, log=stealth)

        elif "date" in command.lower():
            say_date()
            return

        elif "time" in command.lower():
            say_time()
            return

        elif "telegram" in command.lower():
            print(Fore.YELLOW + "What would you like me to send sir ?".center(100))
            casper_speak(speak="What would you like me to send sir ?", voice=voice_engine)
            send_message = casper_input()
            telegram_text(send_message)
            print(Fore.GREEN + "Message sent".center(100))
            casper_speak(speak="Message sent", voice=voice_engine)

            chronicle_log(Fore.YELLOW + "What would you like me to send sir ?".center(100), var=stealth)
            chronicle_log(Fore.GREEN + "Message sent".center(100), var=stealth)

        elif "whatsapp" in command.lower():
            print(Fore.YELLOW + "What would you like me to send sir ?".center(100))
            casper_speak(speak="What would you like me to send sir ?", voice=voice_engine)
            send_message = casper_input()
            whatsapp_text(send_message)
            print(Fore.GREEN + "Message sent".center(100))
            casper_speak(speak="Message sent", voice=voice_engine)

            chronicle_log(Fore.YELLOW + "What would you like me to send sir ?".center(100), var=stealth)
            chronicle_log(Fore.GREEN + "Message sent".center(100), var=stealth)

        elif "developer" in command.lower():
            print(Fore.GREEN + "<<< ACTIVATED DEVELOPER MODE >>>".center(100))
            casper_speak(speak="Activated developer mode", voice=voice_engine)

    # Casper responses (hardcoded)
        elif "introduce" in command:
            print(Fore.GREEN + "I'm Casper, version 2 point 7, your personal desktop assistant.".center(100))
            casper_speak(speak="I'm Casper, version 2 point 7, your personal desktop assistant.", voice=voice_engine)
            chronicle_log(Fore.GREEN + "I'm Casper, version 2 point 7, your personal desktop assistant.".center(100), var=stealth)

        elif "what's my name" in command or "what is my name" in command.lower():
            print(Fore.GREEN + "Your name is Ashfaaq Rifath.".center(100))
            casper_speak(speak="Your name is Ashfaaq Rifath.", voice=voice_engine)
            chronicle_log(Fore.GREEN + "Your name is Ashfaaq Rifath.".center(100), var=stealth)

        elif "who made you" in command:
            print(Fore.GREEN + "I was developed by Ashfaaq Rifath as a flagship project.".center(100))
            casper_speak(speak="i was developed by Ashfaaq Rifath as a flagship project.", voice=voice_engine)
            chronicle_log(Fore.GREEN + "I was developed by Ashfaaq Rifath as a flagship project.".center(100), var=stealth)

        elif "what's up" in command or "how are you" in command.lower():
            print(Fore.GREEN + "I'm fine sir, thank you for asking".center(100))
            casper_speak(speak="i'm fine sir, thank you for asking", voice=voice_engine)
            chronicle_log(Fore.GREEN + "I'm fine sir, thank you for asking".center(100), var=stealth)

        elif "hi" in command or "hello" in command.lower():
            print(Fore.GREEN + "Hello sir, How can i help".center(100))
            casper_speak(speak="Hello sir, How can i help", voice=voice_engine)
            chronicle_log(Fore.GREEN + "Hello sir, How can i help".center(100), var=stealth)

        elif "thank you" in command:
            print(Fore.GREEN + "You're welcome sir, I'm happy to help".center(100))
            casper_speak(speak="You're welcome sir, i'm happy to help", voice=voice_engine)
            chronicle_log(Fore.GREEN + "You're welcome sir, i'm happy to help".center(100), var=stealth)

        else:
            print(Fore.RED + "Sorry sir, I didn't quite get that".center(100))
            casper_speak(speak="Sorry sir, I didn't quite get that", voice=voice_engine)
            chronicle_log(Fore.RED + "Sorry sir, I didn't quite get that".center(100), var=stealth)

    except RecursionError:
        print(Fore.GREEN + "Countdown completed".center(5))
        casper_speak(speak="Countdown completed", voice=voice_engine)
    except:
        print(Fore.RED + "Sorry sir, I didn't quite get that".center(100))
        casper_speak(speak="Sorry sir, I didn't quite get that", voice=voice_engine)

        chronicle_log(Fore.RED + "Sorry sir, I didn't quite get that".center(100), var=stealth)

###################################################################################################################

if __name__ == "__main__":
    os.system('cmd /c "CasperIntro.gif"')
    time.sleep(4.5)
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("cls")
    casper_alert("« ASSISTANT ACTIVATED »")

    voice_engine = 2

    print("")
    print('''
                                 █▀▀█  █▀▀█  █▀▀▀█  █▀▀█  █▀▀▀  █▀▀█ 
                                 █     █▄▄█  ▀▀▀▄▄  █▄▄█  █▀▀▀  █▄▄▀ 
                                 █▄▄█  █  █  █▄▄▄█  █     █▄▄▄  █  █ v2.7.3
                                 ''')

    nowTime = int(datetime.datetime.now().hour)
    if nowTime >= 0 and nowTime < 12:
        greet = "Good Morning sir, how may i help you ?"
        print(Fore.CYAN + greet.center(100))
        chronicle_log(Fore.CYAN + greet.center(100), var=stealth)

    elif nowTime >= 12 and nowTime < 18:
        greet = "Good Afternoon sir, how may i help you ?"
        print(Fore.CYAN + greet.center(100))
        chronicle_log(Fore.CYAN + greet.center(100), var=stealth)

    else:
        greet = "Good Evening sir, how may i help you ?"
        print(Fore.CYAN + greet.center(100))
        chronicle_log(Fore.CYAN + greet.center(100), var=stealth)

    casper_speak(speak=greet, voice=voice_engine)
    print("")
    print(Fore.YELLOW + "Listening...".center(100))

    chronicle_log(Fore.YELLOW + "Listening...".center(100), var=stealth)

    while (1):
        recognize = casper_input()
        if recognize == 0:
            continue

        if "voice" in str(recognize):
            if "voice" in str(recognize):
                voice_engine = 1
            if "default" in str(recognize):
                voice_engine = 2

        elif "sentry mode" in str(recognize):
            print(Fore.RED + "<<< INITIATED SENTRY MODE >>>".center(100))
            casper_speak(speak="initiated sentry mode", voice=voice_engine)
            print(Fore.LIGHTBLACK_EX + "Awaiting password".center(100))
            casper_alert("INITIATED SENTRY MODE")

            chronicle_log(Fore.RED + "<<< INITIATED SENTRY MODE >>>".center(100), var=stealth)
            chronicle_log(Fore.LIGHTBLACK_EX + "Awaiting password".center(100), var=stealth)

            def sentry_mode():
                if input_source == 1:
                    print()
                    text = input(Fore.CYAN + "                                    Enter password: ")
                    
                    try:
                        u_said = text
                        print(Fore.LIGHTBLACK_EX + "Processing...".center(100))
                        print()
                        chronicle_log(f"[text] {u_said}".center(100), var=stealth)
                        chronicle_log(Fore.LIGHTBLACK_EX + "Processing...".center(100), var=stealth)
                        return u_said
                    except:
                        return 0

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    sentry = r.listen(source)
                    sentry_key = ""
                try:
                    sentry_key = r.recognize_google(sentry) 
                    print(Fore.LIGHTBLACK_EX + f"(●) {sentry_key}".center(100))
                    chronicle_log(f"(●) {sentry_key}".center(100), var=stealth)
                except Exception as e:
                    pass
                return sentry_key.lower()

            password = "chronicle 16"
            while True:
                keyword = sentry_mode()
                if keyword.count(password) > 0:
                    casper_alert("SENRTY MODE ACCESS GRANTED")
                    print(Fore.GREEN + "Welcome back sir, how can i help ?".center(100))
                    casper_speak(speak="Welcome back sir, how can i help ?", voice=voice_engine)
                    print("")
                    print(Fore.YELLOW + "Listening...".center(100))
                    recognize = casper_input()

                    chronicle_log(Fore.GREEN + "Welcome back sir, how can i help ?".center(100), var=stealth)
                    chronicle_log(Fore.YELLOW + "Listening...".center(100), var=stealth)
                    break
                elif keyword == "":
                    pass
                else:
                    print(Fore.RED + "<<< WRONG PASSWORD >>>".center(100))
                    casper_speak(speak="WRONG PASSWORD", voice=voice_engine)
                    casper_alert("SENRTY MODE ALERT. WRONG PASSWORD")

        elif "stand by" in str(recognize):
            print(Fore.RED + "<<< INITIATED STANDBY MODE >>>".center(100))
            casper_speak(speak="initiated STANDBY mode", voice=voice_engine)
            winsound.Beep(420, 200)
            casper_alert("INITIATED STANDBY MODE")
            print(Fore.LIGHTBLACK_EX + "Awaiting wake command".center(100))

            chronicle_log(Fore.RED + "<<< INITIATED STANDBY MODE >>>".center(100), var=stealth)
            chronicle_log(Fore.LIGHTBLACK_EX + "Awaiting wake command".center(100), var=stealth)

            def standby_mode():
                if input_source == 1:
                    print()
                    text = input(Fore.CYAN + "                                    Enter wake command: ")
                    
                    try:
                        u_said = text
                        print(Fore.LIGHTBLACK_EX + "Processing...".center(100))
                        print()
                        chronicle_log(f"[text] {u_said}".center(100), var=stealth)
                        chronicle_log(Fore.LIGHTBLACK_EX + "Processing...".center(100), var=stealth)
                        return u_said
                    except:
                        return 0

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    wake = r.listen(source)
                    wake_command = ""
                try:
                    wake_command = r.recognize_google(wake)
                    print(Fore.LIGHTBLACK_EX + f"(●) {wake_command}".center(100))
                    chronicle_log(f"(●) {wake_command}".center(100), var=stealth)
                except Exception as e:
                    pass
                return wake_command.lower()

            WAKE = "wake up"
            while True:
                keyword = standby_mode()
                if keyword.count(WAKE) > 0:
                    winsound.Beep(1000, 500)
                    print("Welcome back sir, how can i help ?".center(100))
                    casper_speak(speak="Welcome back sir, how can i help ?", voice=voice_engine)
                    print("")
                    print(Fore.YELLOW + "Listening...".center(100))
                    recognize = casper_input()

                    chronicle_log("Welcome back sir, how can i help ?".center(100), var=stealth)
                    chronicle_log("", var=stealth)
                    chronicle_log(Fore.YELLOW + "Listening...".center(100), var=stealth)
                    break

        if "sleep" in str(recognize):
            print(Fore.MAGENTA + "Assistant shutdown, have a good day sir".center(100))
            casper_speak(speak="Assistant shutdown, have a good day sir", voice=voice_engine)
            chronicle_log(Fore.MAGENTA + "Assistant shutdown, have a good day sir".center(100), var=stealth)
            chronicle_log("", var=stealth)
            chronicle_log("END LOG >>>", var=stealth)
            casper_alert("« ASSISTANT SHUTDOWN »")
            exit()

        command_engine(recognize)
        print("")
        print(Fore.YELLOW + "Listening...".center(100))

        chronicle_log("", var=stealth)
        chronicle_log(Fore.YELLOW + "Listening...".center(100), var=stealth)










# MIT License
# Copyright (c) 2023 Ashfaaq Rifath - Casper v2.7.3
