import os, shutil, json, sys
from os.path import expanduser

from imagesLoader import resource_path


def set_startup():
    with open(resource_path("config.json"), encoding="utf8") as cfg:
        cfg_data = json.load(cfg)
    if not cfg_data["enableAutoStartup"]:
        print("skipping enable startup")
        return
    
    file_name = sys.executable.split("\\")[-1]
    print(file_name)
    if(file_name == "python.exe"):
        print("skipping enable startup because of debug")
        return
    startup_path = expanduser(r'~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    if sys.executable.split("\\")[-2] == "Startup" or os.path.exists(os.path.join(startup_path, cfg_data["autoStartupName"] + ".exe")):
        print("file alredy in startup")
        return
    shutil.copy2(sys.executable, startup_path)
    file_path = os.path.join(startup_path, file_name)
    os.rename(file_path, os.path.join(startup_path, cfg_data["autoStartupName"] + ".exe"))
