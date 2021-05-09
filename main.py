from adb.capture import get_screen
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
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.edtCapturePath.setText(path)

    def onStop(self):
        print("stop Clicked")

    def onStart(self):
        print("start Clicked")
        get_screen('test.png')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec_())
