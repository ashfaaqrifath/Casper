import os
import winshell
import subprocess
import ctypes
import colorama
from speech_engine import casper_speak
from colorama import Fore, Back
colorama.init(autoreset=True)


def windows_tasks(command, voice_var):
    if "change background" in command.lower():
        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, "C:/Users/ashfa/Downloads/Wallpapers/dtwall11.png", 0)
        print(Fore.GREEN + "Desktop background changed sir.".center(100))
        casper_speak(speak="Desktop background changed sir.", voice=voice_var)

    elif "clear" in command or "recycle" in command.lower():
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
        print(Fore.GREEN + "Recycle bin cleared sir.".center(100))
        casper_speak(speak="Recycle bin cleared sir.", voice=voice_var)

    elif "shutdown" in command.lower():
        print(Fore.GREEN + "Windows will shutdown in T minus 60 seconds.".center(100))
        casper_speak(
            speak="Windows will shutdown in T minus 60 seconds.", voice=voice_var)
        print(Fore.MAGENTA + "System power down, see you later sir.".center(100))
        casper_speak(speak="System power down, see you later sir.", voice=voice_var)
        os.system("shutdown /s /t 60")
        os.system("taskkill /f /im python.exe")

    elif "restart" in command.lower():
        print(Fore.GREEN + "Restarting windows sir.".center(100))
        casper_speak(speak="Restarting windows sir.", voice=voice_var)
        print(Fore.MAGENTA + "System power down, see you later sir.".center(100))
        casper_speak(speak="System power down, see you later sir.", voice=voice_var)
        subprocess.call(["shutdown", "/r"])
        os.system("taskkill /f /im python.exe")

    elif "sign out" in command or "log off" in command.lower():
        print(Fore.GREEN + "Windows signing out.".center(100))
        casper_speak(speak="Windows signing out.", voice=voice_var)
        print(Fore.MAGENTA + "System power down, see you later sir.".center(100))
        casper_speak(speak="System power down, see you later sir.", voice=voice_var)
        subprocess.call(["shutdown", "/l"])
        os.system("taskkill /f /im python.exe")