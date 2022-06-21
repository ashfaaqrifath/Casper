import webbrowser
import wikipedia
import colorama
from speech_engine import casper_speak
from recognizer import casper_listen
from activity_log import casper_log
from colorama import Fore, Back
colorama.init(autoreset=True)


def search_web(command, voice_var):
    if "youtube" in command.lower():
        indx = command.lower().split().index("youtube")
        yt_search = command.split()[indx + 1:]
        print(Fore.GREEN + f"Searching YouTube for {yt_search}".center(100))
        casper_speak(speak=f"Searching YouTube for {yt_search}", voice=voice_var)
        webbrowser.open(f"http://www.youtube.com/results?search_query={yt_search}")
        casper_speak(speak="I found these results", voice=voice_var)

        casper_log(Fore.GREEN + f"Searching YouTube for {yt_search}".center(100))
        casper_log(f"http://www.youtube.com/results?search_query={yt_search}")
        casper_log("I found these results")
        return

    elif "wikipedia" in command.lower():
        print(Fore.YELLOW + "What do you want to search?".center(100))
        casper_speak(speak="what do you want to search?", voice=voice_var)

        wiki_search = casper_listen()
        print(Fore.GREEN + f"Searching wikipedia for {wiki_search}".center(100))
        casper_speak(speak=f"searching wikipedia for {wiki_search}", voice=voice_var)

        wiki_summary = wikipedia.summary(wiki_search, sentences=2)
        centr = str(wiki_summary)
        webbrowser.open(f"https://en.wikipedia.org/wiki/{wiki_search}")
        print("")
        print(Fore.LIGHTBLUE_EX + centr.center(100))
        casper_speak(speak=f"According to wikipedia, {wiki_summary}", voice=voice_var)

        casper_log(Fore.YELLOW + "What do you want to search?".center(100))
        casper_log(Fore.GREEN + f"Searching wikipedia for {wiki_search}".center(100))
        casper_log("")
        casper_log(Fore.LIGHTBLUE_EX + centr.center(100))
        return

    elif "github" in command or "account" in command.lower():
        print(Fore.GREEN + "Accessing your GitHub account".center(100))
        casper_speak(speak="Accessing your GitHub account", voice=voice_var)
        webbrowser.open("https://github.com/ashfaaqrifath")
        return

    elif "source code" in command.lower():
        print(Fore.GREEN + "Accessing my source code from GitHub".center(100))
        casper_speak(speak="Accessing my source code from GitHub", voice=voice_var)
        webbrowser.open("https://github.com/ashfaaqrifath/Casper")
        return

    elif "stack overflow" in command.lower():
        print(Fore.GREEN + "Opening Stack Overflow".center(100))
        casper_speak(speak="Opening Stack Overflow", voice=voice_var)
        webbrowser.open("https://stackoverflow.com/questions/tagged/python+python-3.x+visual-studio-code?sort=Newest&uqlId=57773")
        # This link is with my stackoverflow filter.
        return

    elif "search" in command.lower():
        indx = command.lower().split().index("search")
        query = command.split()[indx + 1:]
        print(Fore.GREEN + f"Searching Google for {query}".center(100))
        casper_speak(speak=f"searching google for {query}", voice=voice_var)
        webbrowser.open(f"http://www.google.com/search?q={query}")
        casper_speak(speak="I found these results", voice=voice_var)
        return

    elif "new tab" in command or "chrome tab" in command.lower():
        webbrowser.open("https://google.com")
        print(Fore.GREEN + "Opened new chrome tab".center(100))
        casper_speak(speak="opened new chrome tab", voice=voice_var)
        return

    elif "incognito" in command.lower():
        tab = "www.google.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"
        webbrowser.get(chrome_path).open_new(tab)
        print(Fore.RED + "Enabled Incognito mode".center(100))
        casper_speak(speak="Enabled Incognito mode", voice=voice_var)
        return

    elif "where is" in command.lower():
        location = command.replace("where is", "")
        google_maps = location
        print(Fore.GREEN + f"Locating {google_maps}".center(100))
        casper_speak(speak=f"locating {google_maps}", voice=voice_var)
        webbrowser.open(f"https://www.google.nl/maps/place/{location}")
        casper_speak(speak=f"{google_maps} Located sir.", voice=voice_var)
        return