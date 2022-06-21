import sys
import os
import datetime

date = datetime.datetime.now().strftime("%h:%H:%M:%S")
log_name = str(date).replace(":", "-") + "-Log.txt"
folder = "Casper Log"
save_path = os.path.join(folder, log_name)


def casper_log(write):
    print_save = sys.stdout
    f = open(save_path, 'a', encoding="utf-8")
    sys.stdout = f
    y = write
    y = write
    y = write

    print(y)

    sys.stdout = print_save
    f.close()