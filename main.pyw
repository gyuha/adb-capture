from core import mainCore, macroActions
from adb.capture import get_screen
import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic

import mainUi


# form_class = uic.loadUiType("mainUi.ui")[0]


class MainWindow(QMainWindow, mainUi.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.core = mainCore()

        self.edtCapturePath.setText(self.core.capturePath)

        self.setMacroTable()

        self.btnPathSelect.clicked.connect(self.onSelectPath)
        self.btnStart.clicked.connect(self.onStart)
        self.btnStop.clicked.connect(self.onStop)

    def setMacroTable(self):
        self.macroTable.setRowCount(len(self.core.macro))
        for row, macro in enumerate(self.core.macro):
            actionCombo = QComboBox()
            actionCombo.addItems(macroActions)
            index = actionCombo.findText(
                macro['action'])
            if index > -1:
                actionCombo.setCurrentIndex(index)
            self.macroTable.setCellWidget(row, 0, actionCombo)
            self.macroTable.setItem(
                row, 1, QTableWidgetItem(macro['value']))

    def setCapturePath(self, path):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.edtCapturePath.setText(path)
        self.core.capturePath = path

    def onSelectPath(self):
        print("select path Clicked")
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.edtCapturePath.setText(path)
        self.core.capturePath = path

    def onStop(self):
        print("stop Clicked", self.core.capturePath)

    def onStart(self):
        print("start Clicked")
        get_screen('test.png')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec_())
