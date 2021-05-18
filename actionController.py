import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ActionController(QObject):
    actionDone = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.running = False

    def setAction(self, action, value):
        if self.running == True:
            return
        self.running = True
        if action == "delay":
            timeout = int(value)
        else:
            timeout = 100
        print('📢[actionController.py:20]:', timeout)
        QTimer.singleShot(timeout, lambda: self.runAction(action, value))

    def runAction(self, action, value):
        print(action)
        print(value)

        if self.running == False:
            return
        self.actionDone.emit()

    def stopAction(self):
        self.running = False
