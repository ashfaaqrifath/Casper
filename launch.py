import time
import sys
import os
from colorama import Fore, Back
import colorama
colorama.init(autoreset=True)


def progress(percent=0, width=30):
    symbol = width * percent // 100
    blanks = width - symbol

    print('\r                                     [', Fore.GREEN + symbol * "█", blanks*' ', ']', f' {percent:.0f}%',
          sep='', flush=True, end='')

def launching():
    print(Fore.LIGHTBLACK_EX + '''                                               :!&@@@@@@@@@@@&!:              
                                           :Y#@@@@@@@@@@@@@@@@@@@#Y^          
                                        .Y&@@@@@@@@@@@@@@@@@@@@@@@@@&5.       
                                      :G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B:     
                                     5@@@@#: 75B&@@@&&#B#&@@@@&B57 ^&@@@@5    
                                   .#@@@@@5       ..       ..       G@@@@@&.  
                                   &@@@@@@5                         G@@@@@@&. 
                                  B@@@@@@@5     .:.         .:.     G@@@@@@@B 
                                 ^@@@@@@@@5   .B@@@@J     J@@@@B.   G@@@@@@@@~
                                 P@@@@@@@@5   ?@@@@@@     @@@@@@?   G@@@@@@@@G
                                 B@@@@@@@@5    J&&&B^     ^B&&&J    G@@@@@@@@B
                                 P@@@@@@@@G                         #@@@@@@@@P
                                 ^@@@@@@@@@:                       ^@@@@@@@@@~
                                  G@@@@@@@@&.                     .@@@@@@@@@B 
                                   &@@@@@@@@@?                    #@@@@@@@@&. 
                                   .#@@@@@@@@@&Y:                 ~@@@@@@@&.  
                                     Y@@@@@@@@@@@&GY!~^::::      ~^#@@@@@5    
                                      .G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B:     
                                        .Y&@@@@@@@@@@@@@@@@@@@@@@@@@&Y.       
                                           :JB@@@@@@@@@@@@@@@@@@@#J:          
                                               :!&@@@@@@@@@@@&!:''')

    print("")
    print(Fore.LIGHTBLACK_EX + '''
                                     █▀▀█  █▀▀█  █▀▀▀█  █▀▀█  █▀▀▀  █▀▀█ 
                                     █     █▄▄█  ▀▀▀▄▄  █▄▄█  █▀▀▀  █▄▄▀ 
                                     █▄▄█  █  █  █▄▄▄█  █     █▄▄▄  █  █
                                              DESKTOP ASSISTANT
                                         ''')
    print(Fore.YELLOW + "        Launching Casper v3.0.0".center(100))
    for i in range(101):
        progress(i)
        time.sleep(0.01)

    print("")
    print(Fore.GREEN + "        Systems ready".center(100))
    time.sleep(1)
    os.system('cls')