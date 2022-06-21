import os
import colorama
from speech_engine import casper_speak
from colorama import Fore, Back
colorama.init(autoreset=True)


def open_program(command, voice_var):
    if "chrome" in command.lower():
        print(Fore.GREEN + "Opening Google Chrome".center(100))
        casper_speak(speak="Opening Google Chrome", voice=voice_var)
        os.startfile(
            "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
        return

    elif "drive" in command:
        print(Fore.GREEN + "Opening Google Drive".center(100))
        casper_speak(speak="Opening Google Drive", voice=voice_var)
        os.startfile(
            "C:/Program Files/Google/Drive File Stream/56.0.11.0/GoogleDriveFS.exe")
        return

    elif "code" in command.lower():
        print(Fore.GREEN + "Opening Visual Studio Code".center(100))
        casper_speak(speak="Opening Visual Studio Code", voice=voice_var)
        os.startfile(
            "C:/Users/ashfa/AppData/Local/Programs/Microsoft VS Code/Code.exe")
        return

    elif "downloader" in command or "video" in command.lower():
        print(Fore.GREEN + "Opening YouTube Downloader".center(100))
        casper_speak(speak="Opening YouTube Downloader", voice=voice_var)
        os.startfile(
            "C:/Users/ashfa/OneDrive/Documents/VScode Projects/My YT Downloader/YTdownloader.exe")
        return

    elif "word" in command:
        print(Fore.GREEN + "Opening Microsoft Word".center(100))
        casper_speak(speak="Opening Microsoft Word", voice=voice_var)
        os.startfile(
            "C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE")
        return

    elif "excel" in command or "worksheet" in command:
        print(Fore.GREEN + "Opening Microsoft Excel".center(100))
        casper_speak(speak="Opening Microsoft Excel", voice=voice_var)
        os.startfile(
            "C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE")
        return

    elif "access" in command or "database" in command:
        print(Fore.GREEN + "Opening Microsoft Access".center(100))
        casper_speak(speak="Opening Microsoft Access", voice=voice_var)
        os.startfile(
            "C:/Program Files (x86)/Microsoft Office/root/Office16/MSACCESS.EXE")
        return

    elif "notepad" in command.lower():
        print(Fore.GREEN + "Opening Notepad".center(100))
        casper_speak(speak="Opening Notepad", voice=voice_var)
        os.startfile("%windir%/system32/notepad.exe")
        return

    elif "zoom" in command.lower():
        print(Fore.GREEN + "Opening Zoom".center(100))
        casper_speak(speak="Opening Zoom", voice=voice_var)
        os.startfile("C:/Users/ashfa/AppData/Roaming/Zoom/bin/Zoom.exe")
        return

    elif "activate VPN" in command:
        print(Fore.GREEN + "Activating VPN sir".center(100))
        casper_speak(speak="Activating VPN sir", voice=voice_var)
        os.startfile(
            "C:/Program Files (x86)/Windscribe/WindscribeLauncher.exe")
        return

    elif "task manager" in command.lower():
        print(Fore.GREEN + "Accessing Task Manager".center(100))
        casper_speak(speak="Accessing Task Manager", voice=voice_var)
        os.startfile("%windir%/system32/taskmgr.exe /7")
        return