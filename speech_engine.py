import pyttsx3

def casper_speak(speak, voice):
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)
    engine.say(speak)
    engine.runAndWait()
