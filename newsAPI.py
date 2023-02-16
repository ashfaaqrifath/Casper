import requests
import colorama
import pycountry
from newsapi import NewsApiClient
from speech_engine import casper_speak
from chronicle_engine import chronicle_log
from input_engine import casper_input
from colorama import Fore, Back
colorama.init(autoreset=True)


def news_BBC(voice_var, log):
    print()
    print(Fore.YELLOW + "Accessing BBC Network...".center(100))
    casper_speak(speak="Accessing BBC network...", voice=voice_var)
    chronicle_log(Fore.YELLOW + "Accessing BBC Network...".center(100), var=log)

    print()
    print(Fore.GREEN + "<<< HEADLINES TODAY >>>".center(100))
    casper_speak(speak="Headlines Today", voice=voice_var)
    chronicle_log(Fore.GREEN + "<<< HEADLINES TODAY >>>".center(100), var=log)

    query_api = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "YOUR API KEY"
    }
    news_url = "https://newsapi.org/v1/articles"
    res = requests.get(news_url, params=query_api)
    open_bbc = res.json()

    headlines = open_bbc["articles"]
    results = []

    for hl in headlines:
        results.append(hl["title"])

    for i in range(len(results)):
        print("----------------------------------------------------")
        print(i + 1, results[i])

    chronicle_log(write=results, var=log)
    casper_speak(speak=results, voice=voice_var)

###########################################################################################


def news_category(voice_var, log):
    newsapi = NewsApiClient(api_key="YOUR API KEY")
    # input_country = input("Country: ")
    # input_countries = [f'{input_country.strip()}']
    # countries = {}

    # for country in pycountry.countries:

    #     countries[country.name] = country.alpha_2

    # codes = [countries.get(country.title(), 'Unknown code')
    #          for country in input_countries]

    print(Fore.GREEN + "NEWS CATEGORIES" + Fore.WHITE + "\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology")
    chronicle_log(write=Fore.GREEN + "NEWS CATEGORIES" + Fore.WHITE + "\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology", var=log)
    print()

    print(Fore.YELLOW + "Which category are you interested in sir ?")
    casper_speak(speak="Which category are you interested in sir?", voice=voice_var)
    chronicle_log(write=Fore.YELLOW + "Which category are you interested in sir ?", var=log)

    categorize = casper_input(log)
    chronicle_log(write=categorize, var=log)

    top_headlines = newsapi.get_top_headlines(category=f'{categorize.lower()}', language='en')  # , country=f'{codes[0].lower()}')
    Headlines = top_headlines['articles']

    if Headlines:
        print()
        print(Fore.GREEN + f"<<< {categorize.upper()} HEADLINES TODAY >>>".center(100))
        casper_speak(speak=f"{categorize} Headlines Today", voice=voice_var)
        chronicle_log(write=Fore.GREEN + f"<<< {categorize.upper()} HEADLINES TODAY >>>".center(100), var=log)

        for articles in Headlines:
            b = articles['title'][::-1].index("-")
            if "news" in (articles['title'][-b+1:]).lower():
                print("----------------------------------------------------")
                print(f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
            else:
                print("----------------------------------------------------")
                print(f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")

        chronicle_log(write=f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.", var=log)
        chronicle_log(write=f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.", var=log)
    else:
        print(Fore.RED + "Sorry sir, no articles found".center(100))
        chronicle_log(write=Fore.RED + "Sorry sir, no articles found".center(100), var=log)
