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
    temperature=0.5,
    )
    print(Fore.GREEN + response.choices[0].text)
    casper_speak(speak=response.choices[0].text, voice=voice_var)
    chronicle_log(write=Fore.GREEN + response.choices[0].text, var=log)