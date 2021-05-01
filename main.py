import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("main.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnPathSelect.clicked.connect(self.onSelectPath)
        self.btnStart.clicked.connect(self.onStart)
        self.btnStop.clicked.connect(self.onStop)

    def onSelectPath(self):
        print("select path Clicked")

    def onStop(self):
        print("stop Clicked")

    def onStart(self):
        print("start Clicked")
        self.edtCapturePath.setText('start')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec_())
