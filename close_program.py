import os
import colorama
from speech_engine import casper_speak
from colorama import Fore, Back
colorama.init(autoreset=True)


def close_program(command, voice_var):
    if "chrome" in command:
        print(Fore.GREEN + "Closing Google Chrome".center(100))
        casper_speak(speak="Closing Google Chrome", voice=voice_var)
        os.system("taskkill /f /im chrome.exe")
        return

    elif "excel" in command or "worksheet" in command:
        print(Fore.GREEN + "Closing Microsoft Excel".center(100))
        casper_speak(speak="Closing Microsoft Excel", voice=voice_var)
        os.system("taskkill /f /im excel.exe")
        return

    elif "word" in command:
        print(Fore.GREEN + "Closing Microsoft Word".center(100))
        casper_speak(speak="Closing Microsoft Word", voice=voice_var)
        os.system("taskkill /f /im winword.exe")
        return

    elif "code" in command.lower():
        print(Fore.GREEN + "Closing Visual Studio Code".center(100))
        casper_speak(speak="Closing Visual Studio Code", voice=voice_var)
        os.system("taskkill /f /im Code.exe")
        return

    elif "close notepad" in command.lower():
        print(Fore.GREEN + "Understood sir".center(100))
        casper_speak(speak="Understood sir", voice=voice_var)
        os.system("taskkill /f /im notepad.exe")
        return

    elif "close this" in command.lower():
        print(Fore.GREEN + "Understood sir".center(100))
        casper_speak(speak="Understood sir", voice=voice_var)
        os.system("taskkill /f /im notepad.exe")
        return