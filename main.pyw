import io
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QImage, QPixmap
from core import mainCore, macroActions
from adb.capture import get_screen
import sys
import os

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QDir, pyqtSlot, Qt

import mainUi


# form_class = uic.loadUiType("mainUi.ui")[0]


class MainWindow(QMainWindow, mainUi.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.core = mainCore()

        self.edtCapturePath.setText(self.core.capturePath)

        self.setMacroTable()

        self.actionOpen.triggered.connect(self.clickConfigLoad)
        self.actionSave.triggered.connect(self.clickConfigSave)
        self.actionSaveAs.triggered.connect(self.clickConfigSaveAs)

        self.lbConfigFilePath.setText(self.core.configPath)
        self.btnConfigInsert.clicked.connect(self.clickConfigInsert)
        self.btnConfigAdd.clicked.connect(self.clickConfigAdd)
        self.btnConfigRemove.clicked.connect(self.clickConfigRemove)
        self.btnPathSelect.clicked.connect(self.clickSelectPath)
        self.btnStart.clicked.connect(self.clickStart)
        self.btnStop.clicked.connect(self.clickStop)

        self.selectRow = 0

        self.setLsFiles("C:\\workspace\\adb-capture")
        self.loadCaptureFiles()

    def setLsFiles(self, path):
        self.model = QFileSystemModel()
        # self.model.setRootPath(path)
        # self.index_root = self.model.index(self.model.rootPath())
        # self.lsFiles.setRootIndex(self.index_root)

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

    def clickConfigSaveAs(self):
        path = QFileDialog.getSaveFileName(
            self, 'Save File', "", "JSON (*.json)")

        self.core.configPath = path[0]
        self.core.macro = []

        for row in range(self.macroTable.rowCount()):
            action = self.macroTable.cellWidget(row, 0).currentText()
            value = self.macroTable.item(row, 1).text()
            self.core.macro.append({"action": action, "value": value})
        self.core.saveMacro()

        self.lbConfigFilePath.setText(self.core.configPath)
        self.core.loadMacro()
        self.setMacroTable()
        QMessageBox.information(self, "Information", "저장 완료")

    def clickConfigInsert(self):
        row = self.macroTable.currentRow()
        self.macroTable.insertRow(row)
        self.getMacroTableRow(row, '', '')

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

    def pil2pixmap(self, image):
        bytes_img = io.BytesIO()
        image.save(bytes_img, format='JPEG')

        qimg = QImage()
        qimg.loadFromData(bytes_img.getvalue())

        return QPixmap.fromImage(qimg)

    def loadCaptureFiles(self):
        files = os.listdir(self.core.capturePath)
        for file in files:
            self.addCaptureFile(file)

    def addCaptureFile(self, file):
        path = os.path.join(self.core.capturePath, file)
        # or not (path.endswith(".jpg") and path.endswith(".png")):
        if os.path.isdir(path) or not (path.endswith(".jpg") or path.endswith(".png")):
            return
        picture = Image.open(path)
        picture.thumbnail((80, 120), Image.ANTIALIAS)
        # icon = QIcon(QPixmap.fromImage(ImageQt(picture)))
        icon = QIcon(self.pil2pixmap(picture))
        item = QListWidgetItem(os.path.basename(path), self.lsFiles)
        item.setStatusTip(path)
        item.setIcon(icon)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec_())
