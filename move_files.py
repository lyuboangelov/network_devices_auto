import shutil
import os

def move_files(source, dest):

    files = os.listdir(source)

    for f in files:
        if (f.startswith("run_conf_")):
            shutil.move(f, dest)        
    return
