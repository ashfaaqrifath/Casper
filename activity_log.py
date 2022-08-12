import datetime
import os
import sys

date = datetime.datetime.now().strftime("%h:%H:%M:%S")
act_log = str(date).replace(":", "-") + "-Log.txt"
audio_log = str(date).replace(":", "-") + "-Audio.wav"

folder = "Casper Log"
save_path = os.path.join(folder, act_log)
folderB = "Casper Log"
save_pathB = os.path.join(folder, audio_log)


def casper_log(write, var):
    if var == 0:
        print_save = sys.stdout
        f = open(save_path, 'a', encoding="utf-8")
        sys.stdout = f
        y = write
        print(y)
        sys.stdout = print_save
        f.close()

    elif var == 1:
        print_save = sys.stdout
        f = open(save_path, 'a', encoding="utf-8")
        sys.stdout = f
        y = write
        pass
        sys.stdout = print_save
        f.close()
