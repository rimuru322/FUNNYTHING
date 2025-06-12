from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap
from pynput import mouse
from imagesLoader import choose_image

import threading
import sys


class LolWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(QtCore.Qt.SplashScreen  | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowTransparentForInput | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.0)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
    
    def change_image(self):
        image = QImage(choose_image())
        pixmap = QPixmap.fromImage(image)
        self.image_label.setPixmap(pixmap)
        self.image_label.resize(pixmap.width(), pixmap.height())


def hide():
    global window
    window.hide()


def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        global window
        window.change_image()
        window.show()
        timer = threading.Timer(0.08, hide)
        timer.start()

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        global window
        window = LolWindow()
        window.show()
        window.hide()
        window.setWindowOpacity(0.4)
        self.listener = mouse.Listener(on_click=on_click)

    def start(self):
        self.listener.start()
        window.hide()
        window.setWindowOpacity(0.4)
        self.app.exec()
