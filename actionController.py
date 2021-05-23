from adb.capture import get_screen, imageCrop
from adb.adbKey import send_adb_key
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ActionController(QObject):
    actionDone = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def setAction(self, action, value):
        if action == "delay":
            timeout = int(value)
        else:
            timeout = 100
        QTimer.singleShot(timeout, lambda: self.runAction(action, value))

    def runAction(self, action, value):
        if self.running == False:
            return

        if action == "capture":
            scrcpy = ScrCpyCapture()
            get_screen('./capture/a.png')
        elif action == "crop":
            print('📢[actionController.py:34]:', "crop")
            # imageCrop("t", 1, 2, 3, 4, True)
        elif action == "key":
            send_adb_key(value)

        print(action)
        print(value)

        self.actionDone.emit()

    def sendKey(self, key):
        send_adb_key(key)

    def stopAction(self):
        self.running = False
