import webbrowser
import wikipedia
import colorama
from speech_engine import casper_speak
from recognizer import casper_listen
from chronicle_engine import chronicle_log
from message_engine import casper_alert
from colorama import Fore, Back
colorama.init(autoreset=True)


def surf_web(command, voice_var, log):
    if "search" in command.lower():
        indx = command.lower().split().index("search")
        conv = command.split()[indx + 1:]
        query = ' '.join([str(item) for item in conv])
        print(Fore.GREEN + f"Searching for {query}".center(100))
        casper_speak(speak=f"searching for {query}", voice=voice_var)
        webbrowser.open(f"https://www.google.com/search?q={query}")
        casper_speak(speak="I found these results", voice=voice_var)

        chronicle_log(write=Fore.GREEN + f"Searching Google for {query}".center(100), var=log)
        chronicle_log(write="I found these results".center(100), var=log)
        return

    elif "youtube" in command.lower():
        indx = command.lower().split().index("youtube")
        conv = command.split()[indx + 1:]
        yt_search = ' '.join([str(item) for item in conv])
        print(Fore.GREEN + f"Searching YouTube for {yt_search}".center(100))
        casper_speak(speak=f"Searching YouTube for {yt_search}", voice=voice_var)
        webbrowser.open(f"https://www.youtube.com/results?search_query={yt_search}")
        casper_speak(speak="I found these results", voice=voice_var)

        chronicle_log(Fore.GREEN + f"Searching YouTube for {yt_search}".center(100), var=log)
        chronicle_log(write="I found these results".center(100), var=log)
        return

    elif "Wikipedia" in command:
        print(Fore.YELLOW + "What do you want to search?".center(100))
        casper_speak(speak="what do you want to search?", voice=voice_var)
        wiki_search = casper_listen(log)

        print()
        print(Fore.GREEN + f"Searching wikipedia for {wiki_search}".center(100))
        casper_speak(speak=f"searching wikipedia for {wiki_search}", voice=voice_var)

        wiki_summary = wikipedia.summary(wiki_search, sentences=2)
        centr = str(wiki_summary)
        webbrowser.open(f"https://en.wikipedia.org/wiki/{wiki_search}")
        print("")
        print(Fore.LIGHTBLUE_EX + centr.center(100))
        casper_speak(speak=f"According to wikipedia, {wiki_summary}", voice=voice_var)

        chronicle_log(write=Fore.YELLOW + "What do you want to search?".center(100), var=log)
        chronicle_log(write=Fore.GREEN + f"Searching wikipedia for {wiki_search}".center(100), var=log)
        chronicle_log(write="", var=log)
        chronicle_log(write=Fore.LIGHTBLUE_EX + centr.center(100), var=log)
        return

    elif "gmail" in command.lower():
        print(Fore.GREEN + "Opening your Gmail account".center(100))
        casper_speak(speak="Opening your Gmail account", voice=voice_var)
        webbrowser.open("https://mail.google.com/")
        chronicle_log(write=Fore.GREEN + "Opening your Gmail account".center(100), var=log)
        return 

    elif "google news" in command.lower():
        print(Fore.YELLOW + "What do you want to search?".center(100))
        casper_speak(speak="what do you want to search?", voice=voice_var)
        gnews = casper_listen(log)

        print()
        print(Fore.GREEN + f"Searching Google News for {gnews}".center(100))
        casper_speak(speak=f"searching Google News for {gnews}", voice=voice_var)
        webbrowser.open(f"https://news.google.com/search?q={gnews}&hl=en-US&gl=US&ceid=US%3Aen")
        casper_speak(speak="I found these results", voice=voice_var)

        chronicle_log(write=Fore.GREEN + f"Searching Google News for {gnews}".center(100), var=log)
        chronicle_log(write="I found these results".center(100), var=log)
        return

    elif "github" in command or "account" in command.lower():
        print(Fore.GREEN + "Opening your GitHub account".center(100))
        casper_speak(speak="Opening your GitHub account", voice=voice_var)
        webbrowser.open("https://github.com/ashfaaqrifath")
        chronicle_log(write=Fore.GREEN + "Opening your GitHub account".center(100), var=log)
        return

    elif "facebook" in command.lower():
        print(Fore.GREEN + "Opening your Facebook profile".center(100))
        casper_speak(speak="Opening your Facebook profile", voice=voice_var)
        webbrowser.open("https://www.facebook.com/ashfaaq.rifath")
        chronicle_log(write=Fore.GREEN + "Opening your Facebook profile".center(100), var=log)
        return

    elif "instagram" in command.lower():
        print(Fore.GREEN + "Opening your Instagram profile".center(100))
        casper_speak(speak="Opening your Instagram profile", voice=voice_var)
        webbrowser.open("https://www.instagram.com/ashfaaqrifath/")
        chronicle_log(write=Fore.GREEN + "Opening your Instagram profile".center(100), var=log)
        return

    elif "twitter" in command.lower():
        print(Fore.GREEN + "Opening your Twitter profile".center(100))
        casper_speak(speak="Opening your Twitter profile", voice=voice_var)
        webbrowser.open("https://twitter.com/ashfaaqrifth")
        chronicle_log(write=Fore.GREEN + "Opening your Twitter profile".center(100), var=log)
        return

    elif "source code" in command.lower():
        print(Fore.GREEN + "Accessing source code from GitHub".center(100))
        casper_speak(speak="Accessing source code from GitHub", voice=voice_var)
        webbrowser.open("https://github.com/ashfaaqrifath/Casper")
        chronicle_log(write=Fore.GREEN + "Accessing source code from GitHub".center(100), var=log)
        return

    elif "stack overflow" in command.lower():
        print(Fore.GREEN + "Opening Stack Overflow".center(100))
        casper_speak(speak="Opening Stack Overflow", voice=voice_var)
        webbrowser.open("https://stackoverflow.com")
        chronicle_log(write=Fore.GREEN + "Opening Stack Overflow".center(100), var=log)
        return

    elif "new tab" in command or "chrome tab" in command.lower():
        webbrowser.open("https://google.com")
        print(Fore.GREEN + "Opened new chrome tab".center(100))
        casper_speak(speak="opened new chrome tab", voice=voice_var)
        chronicle_log(write=Fore.GREEN + "Opened new chrome tab".center(100), var=log)
        return

    elif "incognito tab" in command.lower():
        tab = "www.google.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"
        webbrowser.get(chrome_path).open_new(tab)
        print(Fore.RED + "Enabled Incognito mode".center(100))
        casper_speak(speak="Enabled Incognito mode", voice=voice_var)
        chronicle_log(write=Fore.RED + "Enabled Incognito mode".center(100), var=log)
        casper_alert("ENABLED CHROME INCOGNITO MODE")
        return

    elif "locate" in command.lower():
        location = command.replace("locate", "")
        print(Fore.GREEN + f"Locating {location}".center(100))
        casper_speak(speak=f"locating {location}", voice=voice_var)
        webbrowser.open(f"https://www.google.nl/maps/place/{location}")
        chronicle_log(write=Fore.GREEN + f"Locating {location} sir".center(100), var=log)
        return