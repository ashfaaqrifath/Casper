import os
import colorama
from speech_engine import casper_speak
from chronicle_engine import chronicle_log
from colorama import Fore, Back
colorama.init(autoreset=True)


def open_program(command, voice_var, log):
    if "chrome" in command.lower():
        print(Fore.GREEN + "Opening Google Chrome".center(100))
        casper_speak(speak="Opening Google Chrome", voice=voice_var)
        os.startfile("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
        chronicle_log(write=Fore.GREEN + "Opening Google Chrome".center(100), var=log)
        return

    elif "drive" in command:
        print(Fore.GREEN + "Opening Google Drive".center(100))
        casper_speak(speak="Opening Google Drive", voice=voice_var)
        os.startfile("C:/Program Files/Google/Drive File Stream/56.0.11.0/GoogleDriveFS.exe")
        chronicle_log(write=Fore.GREEN + "Opening Google Drive".center(100), var=log)
        return

    elif "code" in command.lower():
        print(Fore.GREEN + "Opening Visual Studio Code".center(100))
        casper_speak(speak="Opening Visual Studio Code", voice=voice_var)
        os.startfile("C:/Users/ashfa/AppData/Local/Programs/Microsoft VS Code/Code.exe")
        chronicle_log(write=Fore.GREEN + "Opening Visual Studio Code".center(100), var=log)
        return

    elif "downloader" in command or "video" in command.lower():
        print(Fore.GREEN + "Opening YouTube Downloader".center(100))
        casper_speak(speak="Opening YouTube Downloader", voice=voice_var)
        os.startfile("C:/Users/ashfa/OneDrive/Documents/My Projects/My YT Downloader/YT Downloader.exe")
        chronicle_log(write=Fore.GREEN + "Opening YouTube Downloader".center(100), var=log)
        return

    elif "word" in command:
        print(Fore.GREEN + "Opening Microsoft Word".center(100))
        casper_speak(speak="Opening Microsoft Word", voice=voice_var)
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE")
        chronicle_log(write=Fore.GREEN + "Opening Microsoft Word".center(100), var=log)
        return

    elif "excel" in command or "worksheet" in command:
        print(Fore.GREEN + "Opening Microsoft Excel".center(100))
        casper_speak(speak="Opening Microsoft Excel", voice=voice_var)
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE")
        chronicle_log(write=Fore.GREEN + "Opening Microsoft Excel".center(100), var=log)
        return

    elif "access" in command or "database" in command:
        print(Fore.GREEN + "Opening Microsoft Access".center(100))
        casper_speak(speak="Opening Microsoft Access", voice=voice_var)
        os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/MSACCESS.EXE")
        chronicle_log(write=Fore.GREEN + "Opening Microsoft Access".center(100), var=log)
        return

    elif "explorer" in command.lower():
        print(Fore.GREEN + "Opening File Explorer".center(100))
        casper_speak(speak="Opening File Explorer", voice=voice_var)
        os.startfile("C:/Windows/explorer.exe")
        chronicle_log(write=Fore.GREEN + "Opening File Explorer".center(100), var=log)
        return

    elif "notepad" in command.lower():
        print(Fore.GREEN + "Opening Notepad".center(100))
        casper_speak(speak="Opening Notepad", voice=voice_var)
        os.startfile("%windir%/system32/notepad.exe")
        chronicle_log(write=Fore.GREEN + "Opening Notepad".center(100), var=log)
        return

    elif "zoom" in command.lower():
        print(Fore.GREEN + "Opening Zoom".center(100))
        casper_speak(speak="Opening Zoom", voice=voice_var)
        os.startfile("C:/Users/ashfa/AppData/Roaming/Zoom/bin/Zoom.exe")
        chronicle_log(write=Fore.GREEN + "Opening Zoom".center(100), var=log)
        return

    elif "activate VPN" in command:
        print(Fore.GREEN + "Activating VPN".center(100))
        casper_speak(speak="Activating VPN", voice=voice_var)
        os.startfile("C:/Program Files (x86)/Windscribe/WindscribeLauncher.exe")
        chronicle_log(write=Fore.GREEN + "Activating VPN".center(100), var=log)
        return

    elif "task manager" in command.lower():
        print(Fore.GREEN + "Accessing Task Manager".center(100))
        casper_speak(speak="Accessing Task Manager", voice=voice_var)
        os.startfile("%windir%/system32/taskmgr.exe /7")
        chronicle_log(write=Fore.GREEN + "Accessing Task Manager".center(100), var=log)
        return

########################################################################################################

def close_program(command, voice_var, log):
    if "chrome" in command:
        print(Fore.GREEN + "Closing Google Chrome".center(100))
        casper_speak(speak="Closing Google Chrome", voice=voice_var)
        os.system("taskkill /f /im chrome.exe")
        chronicle_log(write=Fore.GREEN + "Closing Google Chrome".center(100), var=log)
        return

    elif "zoom" in command.lower():
        print(Fore.GREEN + "Closing Zoom".center(100))
        casper_speak(speak="Closing Zoom", voice=voice_var)
        os.startfile("taskkill /f /im Zoom.exe")
        chronicle_log(write=Fore.GREEN + "Closing Zoom".center(100), var=log)
        return

    elif "excel" in command or "worksheet" in command:
        print(Fore.GREEN + "Closing Microsoft Excel".center(100))
        casper_speak(speak="Closing Microsoft Excel", voice=voice_var)
        os.system("taskkill /f /im excel.exe")
        chronicle_log(write=Fore.GREEN + "Closing Microsoft Excel".center(100), var=log)
        return

    elif "word" in command:
        print(Fore.GREEN + "Closing Microsoft Word".center(100))
        casper_speak(speak="Closing Microsoft Word", voice=voice_var)
        os.system("taskkill /f /im winword.exe")
        chronicle_log(write=Fore.GREEN + "Closing Microsoft Word".center(100), var=log)
        return

    elif "code" in command.lower():
        print(Fore.GREEN + "Closing Visual Studio Code".center(100))
        casper_speak(speak="Closing Visual Studio Code", voice=voice_var)
        os.system("taskkill /f /im Code.exe")
        chronicle_log(write=Fore.GREEN + "Closing Visual Studio Code".center(100), var=log)
        return

    elif "close notepad" in command.lower():
        print(Fore.GREEN + "Closing Notepad".center(100))
        casper_speak(speak="Closing Notepad", voice=voice_var)
        os.system("taskkill /f /im notepad.exe")
        chronicle_log(write=Fore.GREEN + "Closing Notepad".center(100), var=log)
        return