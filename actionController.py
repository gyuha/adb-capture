import os
import time
from adb.ScrcpyCapture import ScrCpyCapture
from core import mainCore
from adb.capture import get_screen, imageCrop
from adb.adbKey import send_adb_key
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ActionController(QObject):
    actionDone = pyqtSignal()
    addImage = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.running = False
        self.core = mainCore()

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
            path = os.path.join(self.core.newFilePath())
            scrcpy.capture(path)
            # get_screen('./capture/a.png')
            time.sleep(0.3)
            self.addImage.emit(path)
        elif action == "crop":
            print(value)
            size = value.split(',')
            if len(size) < 4:
                print(size)
                return
            imageCrop(
                os.path.join(self.core.currentFilePath()),
                int(size[0]),
                int(size[1]),
                int(size[2]),
                int(size[3])
            )
        elif action == "key":
            send_adb_key(value)

        print(action)
        print(value)

        self.actionDone.emit()

    def sendKey(self, key):
        send_adb_key(key)

    def stopAction(self):
        self.running = False
