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
        self.btnConfigAdd.clicked.connect(self.clickConfigAdd)
        self.btnConfigRemove.clicked.connect(self.clickConfigRemove)
        self.btnPathSelect.clicked.connect(self.clickSelectPath)
        self.btnStart.clicked.connect(self.clickStart)
        self.btnStop.clicked.connect(self.clickStop)

        self.selectRow = 0

        # self.macroTable.cellChanged.connect(self.onMacroTableChanged)

    def getMacroTableRow(self, row, action, value):
        actionCombo = QComboBox()
        actionCombo.addItems(macroActions)
        index = actionCombo.findText(action)
        if index > -1:
            actionCombo.setCurrentIndex(index)
        # actionCombo.currentTextChanged.connect(self.onActionComboChange)

        self.macroTable.setCellWidget(
            row, 0, actionCombo)
        item = QTableWidgetItem(value)
        # item.setTextAlignment(Qt.AlignCenter)
        self.macroTable.setItem(row, 1, item)

    def setMacroTable(self):
        self.macroTable.setRowCount(0)
        self.macroTable.setRowCount(len(self.core.macro))
        self.macroTable.setAlternatingRowColors(True)
        self.macroTable.setColumnWidth(0, 100)
        self.macroTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        for row, macro in enumerate(self.core.macro):
            self.getMacroTableRow(row, macro['action'], macro['value'])

    @ pyqtSlot(str)
    def onActionComboChange(self, txt):
        # print(txt)
        combo = self.sender()
        row = combo.currentRow()
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
            self.core.macro.append({"action": action, "value": value})
        self.core.saveMacro()
        QMessageBox.information(self, "Information", "저장 완료")

    def clickConfigAdd(self):
        row = self.macroTable.currentRow()
        self.macroTable.insertRow(row+1)
        self.getMacroTableRow(row+1, '', '')

    def clickConfigRemove(self):
        row = self.macroTable.currentRow()
        self.macroTable.removeRow(row)

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
        self.macroTable.setDisabled(False)

    def clickStart(self):
        print("start Clicked")
        self.macroTable.setDisabled(True)
        self.macroTable.selectRow(self.selectRow)
        self.selectRow = self.selectRow + 1
        if self.selectRow >= self.macroTable.rowCount():
            self.selectRow = 0
        # get_screen('test.png')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec_())
