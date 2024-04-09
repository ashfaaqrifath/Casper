import os
import winshell
import subprocess
import ctypes
import colorama
from speech_engine import casper_speak
from chronicle_engine import chronicle_log
from message_functions import casper_alert
from colorama import Fore, Back
colorama.init(autoreset=True)


def system_actions(command, voice_var, log):
    if "change wallpaper" in command.lower():
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/ashfa/Downloads/Wallpapers/blocks.png", 0)
        print(Fore.GREEN + "Wallpaper changed".center(100))
        casper_speak(speak="Wallpaper changed", voice=voice_var)
        chronicle_log(write=Fore.GREEN + "Wallpaper changed".center(100), var=log)

    elif "clear" in command or "recycle" in command.lower():
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
        print(Fore.GREEN + "Recycle bin cleared".center(100))
        casper_speak(speak="Recycle bin cleared", voice=voice_var)
        chronicle_log(write=Fore.GREEN + "Recycle bin cleared".center(100), var=log)

    elif "shutdown" in command.lower():
        print(Fore.GREEN + "Windows will shutdown in T minus 60 seconds".center(100))
        casper_speak(speak="Windows will shutdown in T minus 60 seconds", voice=voice_var)
        casper_alert("WINDOWS SHUTDOWN")
        print(Fore.MAGENTA + "Assistant shutdown, have a good day sir!".center(100))
        casper_speak(speak="Assistant shutdown, have a good day sir!", voice=voice_var)

        chronicle_log(write=Fore.GREEN + "Windows will shutdown in T minus 60 seconds".center(100), var=log)
        chronicle_log(write=Fore.MAGENTA + "Assistant shutdown, have a good day sir!".center(100), var=log)
        chronicle_log("", var=log)
        chronicle_log("END LOG >>", var=log)
        casper_alert("« ASSISTANT SHUTDOWN »")

        os.system("shutdown /s /t 60")
        os.system("taskkill /f /im python.exe")

    elif "restart" in command.lower():
        print(Fore.GREEN + "Rebooting windows".center(100))
        casper_speak(speak="Rebooting windows", voice=voice_var)
        casper_alert("REBOOTING WINDOWS")
        print(Fore.MAGENTA + "Assistant shutdown, have a good day sir!".center(100))
        casper_speak(speak="Assistant shutdown, have a good day sir!", voice=voice_var)

        chronicle_log(write=Fore.GREEN + "Rebooting windows".center(100), var=log)
        chronicle_log(write=Fore.MAGENTA + "Assistant shutdown, have a good day sir!".center(100), var=log)
        chronicle_log("", var=log)
        chronicle_log("END LOG >>", var=log)
        casper_alert("« ASSISTANT SHUTDOWN »")

        subprocess.call(["shutdown", "/r"])
        os.system("taskkill /f /im python.exe")

    elif "sign out" in command or "log out" in command.lower():
        print(Fore.GREEN + "User signing out".center(100))
        casper_speak(speak="User signing out", voice=voice_var)
        casper_alert("USER SING OUT")
        print(Fore.MAGENTA + "Assistant shutdown, have a good day sir!".center(100))
        casper_speak(speak="Assistant shutdown, have a good day sir!", voice=voice_var)

        chronicle_log(write=Fore.GREEN + "User signing out".center(100), var=log)
        chronicle_log(write=Fore.MAGENTA + "Assistant shutdown, have a good day sir!".center(100), var=log)
        chronicle_log("", var=log)
        chronicle_log("END LOG >>>", var=log)
        casper_alert("<< ASSISTANT SHUTDOWN >>")

        subprocess.call(["shutdown", "/l"])
        os.system("taskkill /f /im python.exe")