import secrets
import string
import pyttsx3
import os.path
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

print("Coded by Ashfaaq Rifath")
voice1 = " PASSWORD MANAGER "
print(Fore.BLACK + Back.YELLOW + voice1)
engine = pyttsx3.init()
engine.say(voice1)
engine.runAndWait()
# the pyttsx3 module reads out all the outputs in this program (text to speech)

# asks the user if they need to generate or add a new password
pass_option = input("Add new or generate password (a/g): ")


if pass_option.lower() == "a":
    # the desired file path should be added here (hardcoded)
    default_path = "G:/My Drive/Password project"
    pass_name = input("Name your password: ")
    save_path = os.path.join(default_path, pass_name + ".txt")
    my_pass = input("Input your password: ")
    user_pass = len(my_pass)
    if user_pass > 14:
        # also contains a password strength meter
        voice2 = " Your password is strong "
        print(Fore.BLACK + Back.GREEN + voice2)
        engine = pyttsx3.init()
        engine.say(voice2)
        engine.runAndWait()

    elif user_pass < 14:
        voice3 = " Password should be stronger "
        print(Fore.BLACK + Back.RED + voice3)
        engine = pyttsx3.init()
        engine.say(voice3)
        engine.runAndWait()

    # takes the file path the user wants as an input
    choose_loc = input("Save to default location or custom location (d/c): ")

    if choose_loc.lower() == "d":
        add_pass = open(save_path, "w")
        add_pass.write(f"Saved password for {pass_name}: ")
        add_pass.write(my_pass)
        add_pass.close()
        voice4 = "Password saved"
        print(Fore.GREEN + voice4)
        engine = pyttsx3.init()
        engine.say(voice4)
        engine.runAndWait()

    elif choose_loc == "c":
        print(Fore.BLACK + Back.YELLOW + " Enter correct file path ")
        custom_path = input("Enter file path: ")
        save_abs_path = os.path.join(custom_path, pass_name + ".txt")
        add_pass = open(save_abs_path, "w")
        add_pass.write(f"Saved password for {pass_name}: ")
        add_pass.write(my_pass)
        add_pass.close()
        voice5 = "Password saved"
        print(Fore.GREEN + voice5)
        engine = pyttsx3.init()
        engine.say(voice5)
        engine.runAndWait()

    else:
        voice6 = " INVALID OPTION "
        print(Fore.BLACK + Back.RED + voice6)
        engine = pyttsx3.init()
        engine.say(voice6)
        engine.runAndWait()

elif pass_option.lower() == "g":
    name = input("Name your password: ")
    try:
        pass_length = int(input("Enter password length: "))
    except:
        voice7 = " ENTER VALID NUMBER "
        print(Fore.BLACK + Back.RED + voice7)
        engine = pyttsx3.init()
        engine.say(voice7)
        engine.runAndWait()

    special_chars = "!@#$%^&*_~;?<>{}[]"
    characters = string.ascii_letters + string.digits + special_chars

    while True:
        password = ''.join(secrets.choice(characters) for i in range(pass_length))
        password += secrets.choice(special_chars)
        if (any(c.islower() for c in password) and any(c.isupper()
        for c in password) and sum(c.isdigit() for c in password) >= 4):
            voice8 = f"Password generated for {name}"
            print(voice8 , ':', password)
            engine = pyttsx3.init()
            engine.say(voice8)
            engine.runAndWait()

            strength = len(password)
            if strength > 14:
                voice9 = " Your password is strong "
                print(Fore.BLACK + Back.GREEN + voice9)
                engine = pyttsx3.init()
                engine.say(voice9)
                engine.runAndWait()

            elif strength < 14:
                voice10 = " Password should be stronger "
                print(Fore.BLACK + Back.RED + voice10)
                engine = pyttsx3.init()
                engine.say(voice10)
                engine.runAndWait()

            need_save = input("Do you want to save this password? (y/n): ")

            if need_save.lower() == "y":
                choose_loc = input("Save to default location or custom location (d/c): ")

            elif need_save == "n":
                print("---------------")

            else:
                voice11 = " INVALID OPTION "
                print(Fore.BLACK + Back.RED + voice11)
                engine = pyttsx3.init()
                engine.say(voice11)
                engine.runAndWait()
            break

    if choose_loc.lower() == "d":
        save_path = "G:/My Drive/Password project"
        def_path = os.path.join(save_path, name + ".txt")
        saving = open(def_path,"w")
        saving.write(f"Generated password for {name}: ")
        saving.write(password)
        saving.close()
        voice12 = "Password saved"
        print(Fore.GREEN + voice12)
        engine = pyttsx3.init()
        engine.say(voice12)
        engine.runAndWait()

    elif choose_loc.lower() == "c":
        voice13 = " Enter correct file path "
        print(Fore.BLACK + Back.YELLOW + voice13)
        engine = pyttsx3.init()
        engine.say(voice13)
        engine.runAndWait()

        save_path = input("Enter file path: ")
        cus_path = os.path.join(save_path, name + ".txt")
        gen_pass = open(cus_path, "w")
        gen_pass.write(f"Saved password for {name}: ")
        gen_pass.write(password)
        gen_pass.close()
        voice14 = "Password saved"
        print(Fore.GREEN + voice14)
        engine = pyttsx3.init()
        engine.say(voice14)
        engine.runAndWait()

    else:
        voice15 = " INVALID OPTION "
        print(Fore.BLACK + Back.RED + voice15)
        engine = pyttsx3.init()
        engine.say(voice15)
        engine.runAndWait()

else:
    voice16 = " INVALID OPTION "
    print(Fore.BLACK + Back.RED + voice16)
    engine = pyttsx3.init()
    engine.say(voice16)
    engine.runAndWait()