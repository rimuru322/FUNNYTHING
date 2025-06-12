import os, shutil, json, sys
from os.path import expanduser

from imagesLoader import resource_path


def set_startup():
    with open(resource_path("config.json"), encoding="utf8") as cfg:
        cfg_data = json.load(cfg)
    if not cfg_data["enableAutoStartup"]:
        print("skipping enable startup")
        return
    
    file_name = os.path.dirname(sys.executable)
    print(file_name)
    if(file_name == "startup.py"):
        print("skipping enable startup because of debug")
        return
    startup_path = expanduser(r'~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    shutil.copy2(file_name, startup_path)
    file_path = os.path.join(startup_path, file_name)
    os.system(f"attrib +H {file_path}")
    os.rename(file_path, os.path.join(startup_path, cfg_data["autoStartupName"] + ".exe"))
