import os
import subprocess
import sys
import winsound
#import WolframAlpha
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
from system_functions import system_actions
from web_functions import internet_actions
from program_functions import open_program, close_program
# from newsAPI import news_BBC, news_category
from chronicle_engine import chronicle_audio, chronicle_log, clean_slate
from currency_converter import convert_currency
from pipwizard import pipwizard
from openai_gpt3 import GPT3
from message_functions import casper_alert, telegram_text, whatsapp_text
from datetime import date
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from colorama import Fore, Back
colorama.init(autoreset=True)


date = datetime.datetime.now().strftime(f"%h{'('}%d{')'}:%H:%M")
txt_file = str(date).replace(":", "-") + "-Log.txt"
audio_file = str(date).replace(":", "-") + "-Audio.wav"

folder = "Activity Logs"
save_txt_file = os.path.join(folder, txt_file)
save_wav_file = os.path.join(folder, audio_file)

log_file = open(save_txt_file, "a")
date = datetime.datetime.now()
log_file.close()

incognito = 0
input_source = 1

time_stamp = datetime.datetime.now().strftime("%D:%h:%H:%M:%S")
chronicle_log(write="CASPER - PC ASSISTANT v2.7.5\n" +
           str(time_stamp) + " \n<< ACTIVITY LOG >> \nBEGIN LOG >>\n \n", var=incognito)

##################################################################################################

def casper_input():
    if input_source == 1:
        print()
        text = input(Fore.CYAN + "                                    Enter prompt: ")
        try:
            u_said = text
            print()
            chronicle_log(f"[text] {u_said}".center(100), var=incognito)
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

            chronicle_log(f"(●) {u_said}".center(100), var=incognito)
            chronicle_log(Fore.LIGHTBLACK_EX + "Processing...".center(100), var=incognito)
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
        print(Fore.RED + "Directory does not exist")

##################################################################################################

def time_info():
    time = datetime.datetime.now().strftime("%H:%M")

    if nowTime >= 0 and nowTime < 12:
        print(Fore.GREEN + f"The time is {time} AM sir".center(100))
        casper_speak(speak=f"The time is {time} AM sir", voice=voice_engine)
        chronicle_log(Fore.GREEN + f"The time is {time} AM sir".center(100), var=incognito)

    elif nowTime >= 12 and nowTime < 18:
        print(Fore.GREEN + f"The time is {time} PM sir".center(100))
        casper_speak(speak=f"The time is {time} PM sir", voice=voice_engine)
        chronicle_log(Fore.GREEN + f"The time is {time} PM sir".center(100), var=incognito)

##################################################################################################

def date_info():
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
    chronicle_log(Fore.GREEN + f"Today is {x} sir".center(100), var=incognito)

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

# def wolfram_API(question):
#     api_key = "Q3RGAU-UWQT2U8W2J"
#     client = WolframAlpha.Client(api_key)
#     result = client.query(question)
#     wolfram_answer = str(next(result.results).text)
#     print()
#     print(Fore.GREEN + wolfram_answer.center(100))
#     casper_speak(speak=wolfram_answer, voice=voice_engine)
#     chronicle_log("", var=incognito)
#     chronicle_log(Fore.GREEN + wolfram_answer.center(100), var=incognito)

##################################################################################################

def play_music():
    print(Fore.GREEN + "Playing music from music directory".center(100))
    casper_speak(speak="Playing music from music directory", voice=voice_engine)
    music_dir = "C:/Users/ashfa/Music"
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[1]))
    chronicle_log(Fore.GREEN + "Playing music from music directory".center(100), var=incognito)
    return

##################################################################################################

def command_engine(command):
    global incognito
    global input_source

    try:
        # Internet tasks
        if "search" in command or "YouTube" in command or "youtube" in command or "google news" in command.lower():
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

        elif "gmail" in command.lower():
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

        elif "Wikipedia" in command or "wiki" in command:
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

        elif "locate" in command.lower():
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

        elif "new tab" in command or "incog tab" in command or "incognito" in command.lower():
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

        elif "account" in command.lower():
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

        elif "facebook" in command.lower():
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

        elif "instagram" in command.lower():
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

        elif "twitter" in command.lower():
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

        elif "stack overflow" in command.lower():
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

        elif "google news" in command or "gnews" in command.lower():
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

        elif "source code" in command or "src" in command.lower():
            internet_actions(command, voice_var=voice_engine, input_var=input_source, log=incognito)
            return

    # NewsAPI
        # elif "headlines" in command.lower():
        #     news_BBC(voice_var=voice_engine, log=incognito)
        #     return

        # elif "news category" in command.lower():
        #     news_category(voice_var=voice_engine, input_var=input_source, log=incognito)
        #     return

    # GPT3 language model API
        elif "AI" in command or "ai" in command.lower():
            print(Fore.GREEN + "<< ACTIVATED OPENAI GPT-3 >>".center(100))
            casper_speak(speak="ACTIVATED OPENAI GPT3", voice=voice_engine)
            casper_alert("ACTIVATED OPENAI GPT-3")
            print()
            print(Fore.LIGHTBLACK_EX + "<< GPT-3 artificial intelligence language model designed by OpenAI >>".center(100))
            print(Fore.YELLOW + "Hello I'm GPT-3 language model how may i be of service?".center(100))
            casper_speak(speak="Hello, I'm GPT3 language model, how may i be of service?", voice=voice_engine)
            get_prompt = casper_input()
            GPT3(usr_prompt=get_prompt, voice_var=voice_engine, log=incognito)
            return

    # WolframAlpha knowledge engine API
        # elif "knowledge" in command:
        #     print(Fore.YELLOW + "What would you like to know about?".center(100))
        #     casper_speak(speak="What would you like to know about?", voice=voice_engine)
        #     get_query = casper_input()
        #     wolfram_API(get_query)
        #     chronicle_log(Fore.YELLOW + "What would you like to know about?".center(100), var=incognito)
        #     return

    # windows tasks
        elif "play music" in command or "play" in command.lower():
            play_music()
            return

        elif "write" in command.lower():
            print(Fore.YELLOW + "What would you like me to write down sir? ".center(100))
            casper_speak(speak="What would you like me to write down sir? ", voice=voice_engine)
            write_note = casper_input()
            make_note(write_note)
            print(Fore.GREEN + "I've made a note of that".center(100))
            casper_speak(speak="I've made a note of that", voice=voice_engine)

            chronicle_log(Fore.YELLOW + "What would you like me to write down sir? ".center(100), var=incognito)
            chronicle_log(Fore.GREEN + "I've made a note of that".center(100), var=incognito)
            return

        elif "change background" in command.lower():
            system_actions(command, voice_var=voice_engine, log=incognito)
            return

        elif "clear" in command or "recycle" in command.lower():
            system_actions(command, voice_var=voice_engine, log=incognito)
            return

        elif "shutdown" in command.lower():
            system_actions(command, voice_var=voice_engine, log=incognito)
            return

        elif "sign out" in command or "log out" in command.lower():
            system_actions(command, voice_var=voice_engine, log=incognito)
            return

    # opening, closing programs
        elif "open" in command.lower():
            open_program(command.lower(), voice_var=voice_engine, log=incognito)
            return

        elif "close" in command.lower():
            close_program(command.lower(), voice_var=voice_engine, log=incognito)
            return

        elif "activate VPN" in command:
            open_program(command, voice_var=voice_engine, log=incognito)
            return

        elif "task manager" in command.lower():
            open_program(command.lower(), voice_var=voice_engine, log=incognito)
            return
        
    # other projects
        elif "currency" in command or "convert" in command:
            print(Fore.GREEN + "<< ACTIVATED CURRENCY CONVERTER PROJECT >>".center(100))
            casper_speak(speak="ACTIVATED CURRENCY CONVERTER PROJECT", voice=voice_engine)
            chronicle_log("<< ACTIVATED CURRENCY CONVERTER PROJECT >>".center(100), var=incognito)
            convert_currency(voice_var=voice_engine, log=incognito)
            return

        elif "python" in command or "package" in command:
            print(Fore.GREEN + "<< ACTIVATED PIPWIZARD PROJECT >>".center(100))
            casper_speak(speak="ACTIVATED PIPWIZARD PROJECT", voice=voice_engine)
            chronicle_log("<< ACTIVATED PIPWIZARD PROJECT >>".center(100), var=incognito)
            pipwizard(voice_var=voice_engine, log=incognito)
            return

    # Casper tasks
        elif "voice" in command or "change voice" in command:
            print(Fore.GREEN + "<< VOICE ENGINE CHANGED >>".center(100))
            casper_speak(speak="Voice engine changed", voice=voice_engine)
            chronicle_log(Fore.GREEN + "<< VOICE ENGINE CHANGED >>".center(100), var=incognito)
            casper_alert("VOICE ENGINE CHANGED")

        elif "text input" in command:
            print(Fore.GREEN + "<< ENABLED TEXT INPUT MODE >>".center(100))
            casper_speak(speak="ENABLED TEXT INPUT MODE", voice=voice_engine)
            chronicle_log("<< ENABLED TEXT INPUT MODE >>".center(100), var=incognito)
            casper_alert("ENABLED TEXT INPUT MODE")
            input_source += 1

        elif "disable text input" in command or "dis txt" in command:
            print(Fore.RED + "<< DISABLED TEXT INPUT MODE >>".center(100))
            casper_speak(speak="DISABLED TEXT INPUT MODE", voice=voice_engine)
            chronicle_log("<< DISABLED TEXT INPUT MODE >>".center(100), var=incognito)
            casper_alert("DISABLED TEXT INPUT MODE")
            input_source = 0

        elif "enable incognito" in command or "incog" in command:
            print(Fore.RED + "<< ENABLED INCOGNITO MODE >>".center(100))
            casper_speak(speak="ENABLED INCOGNITO MODE", voice=voice_engine)
            chronicle_log("<< ENABLED INCOGNITO MODE >>".center(100), var=incognito)
            chronicle_log("Activity logging disabled".center(100), var=incognito)
            casper_alert("ENABLED INCOGNITO MODE")
            chronicle_log("END LOG >>", var=incognito)
            incognito += 1

        elif "disable incognito" in command in "dis incog" in command:
            print(Fore.RED + "<< DISABLED INCOGNITO MODE >>".center(100))
            casper_speak(speak="DISABLED INCOGNITO MODE", voice=voice_engine)
            chronicle_log("<< DISABLED INCOGNITO MODE >>".center(100), var=incognito)
            chronicle_log("Activity logging disabled".center(100), var=incognito)
            casper_alert("DISABLED INCOGNITO MODE")
            chronicle_log("START LOG >>", var=incognito)
            incognito = 0

        elif "clean" in command or "clean slate" in command:
            clean_slate(voice_var=voice_engine)
            incognito += 1

        elif "timer" in command.lower():
            print(Fore.YELLOW + "For how long sir ?".center(100))
            casper_speak(speak="For how long sir ?", voice=voice_engine)
            chronicle_log(Fore.YELLOW + "For how long sir ?".center(100), var=incognito)
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
            chronicle_audio(voice_var=voice_engine, log=incognito)

        elif "date" in command.lower():
            date_info()
            return

        elif "time" in command.lower():
            time_info()
            return

        elif "telegram" in command.lower():
            print(Fore.YELLOW + "What would you like me to send sir ?".center(100))
            casper_speak(speak="What would you like me to send sir ?", voice=voice_engine)
            send_message = casper_input()
            telegram_text(send_message)
            print(Fore.GREEN + "Message sent".center(100))
            casper_speak(speak="Message sent", voice=voice_engine)

            chronicle_log(Fore.YELLOW + "What would you like me to send sir ?".center(100), var=incognito)
            chronicle_log(Fore.GREEN + "Message sent".center(100), var=incognito)

        elif "whatsapp" in command.lower():
            print(Fore.YELLOW + "What would you like me to send sir ?".center(100))
            casper_speak(speak="What would you like me to send sir ?", voice=voice_engine)
            send_message = casper_input()
            whatsapp_text(send_message)
            print(Fore.GREEN + "Message sent".center(100))
            casper_speak(speak="Message sent", voice=voice_engine)

            chronicle_log(Fore.YELLOW + "What would you like me to send sir ?".center(100), var=incognito)
            chronicle_log(Fore.GREEN + "Message sent".center(100), var=incognito)

        # elif "developer" in command.lower():
        #     print(Fore.GREEN + "<< INITIATED DEVELOPER MODE >>".center(100))

    # Casper responses (hardcoded)
        elif "introduce" in command:
            print(Fore.GREEN + "I'm Casper, version 2.7, your PC assistant.".center(100))
            casper_speak(speak="I'm Casper, version 2 point 7, your PC assistant.", voice=voice_engine)
            chronicle_log(Fore.GREEN + "I'm Casper, version 2.7, your PC assistant.".center(100), var=incognito)

        elif "what's my name" in command or "what is my name" in command.lower():
            print(Fore.GREEN + "Your name is Ashfaaq Rifath.".center(100))
            casper_speak(speak="Your name is Ashfaaq Rifath.", voice=voice_engine)
            chronicle_log(Fore.GREEN + "Your name is Ashfaaq Rifath.".center(100), var=incognito)

        elif "who made you" in command:
            print(Fore.GREEN + "I was developed by Ashfaaq Rifath as a flagship project.".center(100))
            casper_speak(speak="I was developed by Ashfaaq Rifath as a flagship project.", voice=voice_engine)
            chronicle_log(Fore.GREEN + "I was developed by Ashfaaq Rifath as a flagship project.".center(100), var=incognito)

        elif "what's up" in command or "how are you" in command.lower():
            print(Fore.GREEN + "I'm fine sir, thank you for asking".center(100))
            casper_speak(speak="i'm fine sir, thank you for asking", voice=voice_engine)
            chronicle_log(Fore.GREEN + "I'm fine sir, thank you for asking".center(100), var=incognito)

        elif "hi" in command or "hello" in command.lower():
            print(Fore.GREEN + "Hello sir, How can i help".center(100))
            casper_speak(speak="Hello sir, How can i help", voice=voice_engine)
            chronicle_log(Fore.GREEN + "Hello sir, How can i help".center(100), var=incognito)

        elif "thank you" in command:
            print(Fore.GREEN + "You're welcome sir, I'm happy to help".center(100))
            casper_speak(speak="You're welcome sir, i'm happy to help", voice=voice_engine)
            chronicle_log(Fore.GREEN + "You're welcome sir, i'm happy to help".center(100), var=incognito)

        else:
            print(Fore.RED + "Sorry sir, I didn't quite get that".center(100))
            casper_speak(speak="Sorry sir, I didn't quite get that", voice=voice_engine)
            chronicle_log(Fore.RED + "Sorry sir, I didn't quite get that".center(100), var=incognito)

    except RecursionError:
        print(Fore.GREEN + "Countdown completed".center(5))
        casper_speak(speak="Countdown completed", voice=voice_engine)
        #winsound.Beep(1000, 500)
    except:
        print(Fore.RED + "Sorry sir, I didn't quite get that".center(100))
        casper_speak(speak="Sorry sir, I didn't quite get that", voice=voice_engine)

        chronicle_log(Fore.RED + "Sorry sir, I didn't quite get that".center(100), var=incognito)

###################################################################################################################

if __name__ == "__main__":
    # os.system('cmd /c "CasperIntro.gif"')
    # time.sleep(4.5)
    # os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("cls")
    casper_alert("<< ASSISTANT ACTIVATED >>")
    voice_engine = 3

    print("")
    print('''
                                 █▀▀█  █▀▀█  █▀▀▀█  █▀▀█  █▀▀▀  █▀▀█ 
                                 █     █▄▄█  ▀▀▀▄▄  █▄▄█  █▀▀▀  █▄▄▀ 
                                 █▄▄█  █  █  █▄▄▄█  █     █▄▄▄  █  █ v2.7.5
                                 ''')

    nowTime = int(datetime.datetime.now().hour)
    if nowTime >= 0 and nowTime < 12:
        greet = "Good Morning sir, how can i help ?"
        print(Fore.CYAN + greet.center(100))
        chronicle_log(Fore.CYAN + greet.center(100), var=incognito)

    elif nowTime >= 12 and nowTime < 18:
        greet = "Good Afternoon sir, how can i help ?"
        print(Fore.CYAN + greet.center(100))
        chronicle_log(Fore.CYAN + greet.center(100), var=incognito)
    else:
        greet = "Good Evening sir, how can i help ?"
        print(Fore.CYAN + greet.center(100))
        chronicle_log(Fore.CYAN + greet.center(100), var=incognito)

    casper_speak(speak=greet, voice=voice_engine)
    print("")
    print(Fore.YELLOW + "Listening...".center(100))

    chronicle_log(Fore.YELLOW + "Listening...".center(100), var=incognito)

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
            print(Fore.RED + "<< ACIVATED SENTRY MODE >>".center(100))
            casper_speak(speak="Activated sentry mode", voice=voice_engine)
            #winsound.Beep(1000, 500)
            print(Fore.LIGHTBLACK_EX + "Awaiting password".center(100))
            casper_alert("ACIVATED SENTRY MODE")

            chronicle_log(Fore.RED + "<< ACIVATED SENTRY MODE >>".center(100), var=incognito)
            chronicle_log(Fore.LIGHTBLACK_EX + "Awaiting password".center(100), var=incognito)

            def sentry_mode():
                if input_source == 1:
                    print()
                    text = input(Fore.BLUE + "                                    Enter password: ")   
                    try:
                        u_said = text
                        chronicle_log(f"[text] {u_said}".center(100), var=incognito)
                        return u_said
                    except:
                        return 0

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    sentry = r.listen(source)
                    sentry_pass = ""
                try:
                    sentry_pass = r.recognize_google(sentry) 
                    print(Fore.LIGHTBLACK_EX + f"(●) {sentry_pass}".center(100))
                    chronicle_log(f"(●) {sentry_pass}".center(100), var=incognito)
                except Exception as e:
                    pass
                return sentry_pass.lower()

            password = "ghost"
            while True:
                keyword = sentry_mode()
                if keyword.count(password) > 0:
                    casper_alert("PASSWORD ACCEPTED. DISABLED SENRTY MODE")
                    print(Fore.GREEN + "<< PASSWORD ACCEPTED >>".center(100))
                    #winsound.Beep(1000, 500)
                    print(Fore.GREEN + "Welcome back sir, how can i help ?".center(100))
                    casper_speak(speak="Welcome back sir, how can i help ?", voice=voice_engine)
                    print("")
                    print(Fore.YELLOW + "Listening...".center(100))
                    recognize = casper_input()

                    chronicle_log(Fore.GREEN + "Welcome back sir, how can i help ?".center(100), var=incognito)
                    chronicle_log(Fore.YELLOW + "Listening...".center(100), var=incognito)
                    break
                elif keyword == "":
                    pass
                else:
                    #winsound.Beep(1000, 500)
                    print(Fore.RED + "<< WRONG PASSWORD >>".center(100))
                    casper_speak(speak="WRONG PASSWORD", voice=voice_engine)
                    casper_alert("SENRTY MODE ALERT. WRONG PASSWORD")
                    chronicle_log(Fore.RED + "<< WRONG PASSWORD >>".center(100), var=incognito)

        elif "stand by" in str(recognize):
            print(Fore.RED + "<< ACIVATED STANDBY MODE >>".center(100))
            casper_speak(speak="Activated STANDBY mode", voice=voice_engine)
            #winsound.Beep(1000, 500)
            casper_alert("ACIVATED STANDBY MODE")
            print(Fore.LIGHTBLACK_EX + "Awaiting wake command".center(100))

            chronicle_log(Fore.RED + "<< ACIVATED STANDBY MODE >>".center(100), var=incognito)
            chronicle_log(Fore.LIGHTBLACK_EX + "Awaiting wake command".center(100), var=incognito)

            def standby_mode():
                if input_source == 1:
                    print()
                    text = input(Fore.BLUE + "                                    Enter wake command: ")
                    try:
                        u_said = text
                        chronicle_log(f"[text] {u_said}".center(100), var=incognito)
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
                    chronicle_log(f"(●) {wake_command}".center(100), var=incognito)
                except Exception as e:
                    pass
                return wake_command.lower()

            wake = "wake up"
            while True:
                keyword = standby_mode()
                if keyword.count(wake) > 0:
                    #winsound.Beep(1000, 500)
                    print(Fore.GREEN + "Welcome back sir, how can i help ?".center(100))
                    casper_speak(speak="Welcome back sir, how can i help ?", voice=voice_engine)
                    print("")
                    print(Fore.YELLOW + "Listening...".center(100))
                    recognize = casper_input()

                    chronicle_log(Fore.GREEN + "Welcome back sir, how can i help ?".center(100), var=incognito)
                    chronicle_log("", var=incognito)
                    chronicle_log(Fore.YELLOW + "Listening...".center(100), var=incognito)
                    break

        if "sleep" in str(recognize):
            print(Fore.MAGENTA + "Assistant shutdown, have a good day sir!".center(100))
            casper_speak(speak="Assistant shutdown, have a good day sir!", voice=voice_engine)
            chronicle_log(Fore.MAGENTA + "Assistant shutdown, have a good day sir!".center(100), var=incognito)
            chronicle_log("", var=incognito)
            chronicle_log("END LOG >>", var=incognito)
            casper_alert("<< ASSISTANT SHUTDOWN >>")
            exit()

        command_engine(recognize)
        print("")
        print(Fore.YELLOW + "Listening...".center(100))

        chronicle_log("", var=incognito)
        chronicle_log(Fore.YELLOW + "Listening...".center(100), var=incognito)









# Copyright (c) 2024 Ashfaaq Rifath - Casper v2.7.5