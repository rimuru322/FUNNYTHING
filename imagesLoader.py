import os
import sys
import random


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class ImagesLoader():
    __instance = None
    __is_first_init = True

    def __new__(cls, *args, **kwargs):
        if ImagesLoader.__instance is None:
            ImagesLoader.__instance = super().__new__(cls, *args, **kwargs)
        return  ImagesLoader.__instance

    def __init__(self):
        if ImagesLoader.__is_first_init:
            self.start_chance = 10
            self.list = []
            list = os.listdir(resource_path("images/"))
            list.remove(".gitkeep")
            print(list)
            for dest in list:
                self.list.append(resource_path("images/" + dest))
            ImagesLoader.__is_first_init = False
    
    def get_random_image(self):
        return random.choice(self.list)


def choose_image():
    return ImagesLoader().get_random_image()
