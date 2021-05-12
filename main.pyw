from core import mainCore, macroActions
from adb.capture import get_screen
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, Qt

import mainUi


# form_class = uic.loadUiType("mainUi.ui")[0]


class MainWindow(QMainWindow, mainUi.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.core = mainCore()

        self.edtCapturePath.setText(self.core.capturePath)

        self.setMacroTable()

        self.lbConfigFilePath.setText(self.core.configPath)
        self.btnConfigLoad.clicked.connect(self.clickConfigLoad)
        self.btnConfigSave.clicked.connect(self.clickConfigSave)
        self.btnPathSelect.clicked.connect(self.clickSelectPath)
        self.btnStart.clicked.connect(self.clickStart)
        self.btnStop.clicked.connect(self.clickStop)

        # self.macroTable.cellChanged.connect(self.onMacroTableChanged)

    def setMacroTable(self):
        self.macroTable.setRowCount(0)
        self.macroTable.setRowCount(len(self.core.macro))
        for row, macro in enumerate(self.core.macro):
            actionCombo = QComboBox()
            actionCombo.addItems(macroActions)
            index = actionCombo.findText(
                macro['action'])
            if index > -1:
                actionCombo.setCurrentIndex(index)
            actionCombo.setProperty('row', row)
            actionCombo.currentTextChanged.connect(self.onActionComboChange)
            self.macroTable.setCellWidget(row, 0, actionCombo)
            self.macroTable.setItem(
                row, 1, QTableWidgetItem(macro['value']))

    @ pyqtSlot(str)
    def onActionComboChange(self, txt):
        # print(txt)
        combo = self.sender()
        row = combo.property('row')
        print(row)
        index = combo.currentIndex()
        self.core.macro[row]['action'] = txt
        print(self.core.macro)

    def clickConfigLoad(self):
        path = QFileDialog.getOpenFileName(
            self, "Select Config file", "", "JSON (*.json)")
        if path[0]:
            self.core.configPath = path[0]
            self.lbConfigFilePath.setText(self.core.configPath)
            self.core.loadMacro()
            self.setMacroTable()

    def clickConfigSave(self):
        self.core.macro = []
        for row in range(self.macroTable.rowCount()):
            action = self.macroTable.cellWidget(row, 0).currentText()
            value = self.macroTable.item(row, 1).text()
            print(action, value)
            self.core.macro.append({"action": action, "value": value})
        self.core.saveMacro()
        QMessageBox.information(self, "Information", "저장 완료")

    def onMacroTableChanged(self):
        text = self.macroTable.currentItem().text()

    def setCapturePath(self, path):
        path = str(QFileDialog.getExistingDirectory(self, "경로 선택"))
        self.edtCapturePath.setText(path)
        self.core.capturePath = path

    def clickSelectPath(self):
        print("select path Clicked")
        path = str(QFileDialog.getExistingDirectory(self, "경로 선택"))
        self.edtCapturePath.setText(path)
        self.core.capturePath = path

    def clickStop(self):
        print("stop Clicked", self.core.capturePath)

    def clickStart(self):
        print("start Clicked")
        get_screen('test.png')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec_())
