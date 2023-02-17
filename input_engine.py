import speech_recognition as sr
import sys
import colorama
import winsound
from chronicle_engine import chronicle_log
from colorama import Fore, Back
colorama.init(autoreset=True)


def casper_input(input_src, log_var):
    if input_src == 1:
        print()
        text = input(Fore.BLUE + "                                    Enter prompt: ")
        try:
            u_said = text
            print()
            chronicle_log(f"[text] {u_said}".center(100), var=log_var)
            return u_said
        except:
            return 0

    r = sr.Recognizer()
    audio = ""
    with sr.Microphone() as source:
        # print("")
        # print(Fore.YELLOW + "Listening...".center(100))
        audio = r.listen(source, phrase_time_limit=15)
    #print(Fore.BLUE + "Processing...".center(100))
    try:
        u_said = r.recognize_google(audio, language='en-US')
        print(f"(●) {u_said}".center(100))
        print(Fore.GREEN + "Processing...".center(100))

        chronicle_log(f"(●) {u_said}".center(100), var=log_var)
        chronicle_log(Fore.GREEN + "Processing...".center(100), var=log_var)
        return u_said
    except:
        #print(Fore.LIGHTBLACK_EX + "Awaiting command.".center(100))
        return 0