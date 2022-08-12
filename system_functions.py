import os
import winshell
import subprocess
import ctypes
import colorama
from speech_engine import casper_speak
from activity_log import casper_log
from colorama import Fore, Back
colorama.init(autoreset=True)


def system_task(command, voice_var, log):
    if "change background" in command.lower():
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/ashfa/Downloads/Wallpapers/blocks.png", 0)
        print(Fore.GREEN + "Desktop background changed sir".center(100))
        casper_speak(speak="Desktop background changed sir", voice=voice_var)
        casper_log(write=Fore.GREEN + "Desktop background changed sir".center(100), var=log)

    elif "clear" in command or "recycle" in command.lower():
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
        print(Fore.GREEN + "Recycle bin cleared sir".center(100))
        casper_speak(speak="Recycle bin cleared sir", voice=voice_var)
        casper_log(write=Fore.GREEN + "Recycle bin cleared sir".center(100), var=log)

    elif "shutdown" in command.lower():
        print(Fore.GREEN + "Windows will shutdown in T minus 60 seconds".center(100))
        casper_speak(speak="Windows will shutdown in T minus 60 seconds", voice=voice_var)
        print(Fore.MAGENTA + "Assistant shutdown, see you later sir".center(100))
        casper_speak(speak="Assistant shutdown, see you later sir", voice=voice_var)

        casper_log(write=Fore.GREEN + "Windows will shutdown in T minus 60 seconds".center(100), var=log)
        casper_log(write=Fore.MAGENTA + "Assistant shutdown, see you later sir".center(100), var=log)
        casper_log("")
        casper_log("END LOG >>>")

        os.system("shutdown /s /t 60")
        os.system("taskkill /f /im python.exe")

    elif "restart" in command.lower():
        print(Fore.GREEN + "Rebooting windows".center(100))
        casper_speak(speak="Rebooting windows", voice=voice_var)
        print(Fore.MAGENTA + "Assistant shutdown, see you later sir".center(100))
        casper_speak(speak="Assistant shutdown, see you later sir", voice=voice_var)

        casper_log(write=Fore.GREEN + "Rebooting windows".center(100), var=log)
        casper_log(write=Fore.MAGENTA + "Assistant shutdown, see you later sir".center(100), var=log)
        casper_log("")
        casper_log("END LOG >>>")

        subprocess.call(["shutdown", "/r"])
        os.system("taskkill /f /im python.exe")

    elif "sign out" in command or "log out" in command.lower():
        print(Fore.GREEN + "Windows signing out".center(100))
        casper_speak(speak="Windows signing out", voice=voice_var)
        print(Fore.MAGENTA + "Assistant shutdown, see you later sir".center(100))
        casper_speak(speak="Assistant shutdown, see you later sir", voice=voice_var)

        casper_log(write=Fore.GREEN + "Windows signing out".center(100), var=log)
        casper_log(write=Fore.MAGENTA + "Assistant shutdown, see you later sir".center(100), var=log)
        casper_log("")
        casper_log("END LOG >>>")

        subprocess.call(["shutdown", "/l"])
        os.system("taskkill /f /im python.exe")