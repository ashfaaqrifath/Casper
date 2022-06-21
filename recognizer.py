import speech_recognition as sr
import sys
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

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

        print_save = sys.stdout
        f = open("Casper Log.txt", 'a', encoding="utf-8")
        sys.stdout = f
        print(Fore.BLUE + "Processing...".center(100))
        print(f"(●) {u_said}".center(100))
        sys.stdout = print_save
        f.close()
        return u_said
    except:
        #print(Fore.LIGHTBLACK_EX + "Awaiting command.".center(100))
        return 0