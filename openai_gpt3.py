import openai
import colorama
from speech_engine import casper_speak
from chronicle_engine import chronicle_log
from colorama import Fore, Back
colorama.init(autoreset=True)

openai.api_key = "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"

def GPT3(usr_prompt, voice_var, log):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=usr_prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=3,
    )
    print(Fore.GREEN + response.choices[0].text)
    casper_speak(speak=response.choices[0].text, voice=voice_var)
    chronicle_log(write=Fore.GREEN + response.choices[0].text, var=log)