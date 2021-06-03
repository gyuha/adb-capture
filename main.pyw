from actionController import ActionController
import io
import glob
import time
import re

from libs.fileUtil import removePathFiles
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

        self.btnCapture.clicked.connect(self.clickCapture)
        self.btnStart.clicked.connect(self.clickStart)
        self.btnStop.clicked.connect(self.clickStop)

        self.btnDeleteFile.clicked.connect(self.clickDeleteSelectFile)
        self.btnDeleteAllFiles.clicked.connect(self.clickDeleteAllFiles)

        self.lsFiles.itemSelectionChanged.connect(self.onCaptureFileChanged)

        self.selectRow = 0

        self.actionController = ActionController()
        self.actionController.actionDone.connect(self.actionDone)
        self.actionController.addImage.connect(self.addImage)

        # self.setLsFiles("C:\\workspace\\adb-capture")
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

    @pyqtSlot(str)
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
        self.loadCaptureFiles()

    def clickSelectPath(self):
        print("select path Clicked")
        path = str(QFileDialog.getExistingDirectory(self, "경로 선택"))
        self.edtCapturePath.setText(path)
        self.core.capturePath = path
        self.loadCaptureFiles()

    def clickStop(self):
        print("stop Clicked", self.core.capturePath)
        self.actionController.stop()
        self.actionController.stopAction()
        self.macroTable.setDisabled(False)

    def clickStart(self):
        print("start Clicked")
        self.macroTable.setDisabled(True)
        self.selectRow = 0
        self.macroTable.selectRow(self.selectRow)
        self.actionController.start()
        self.actionController.setAction("capture", "take")
        # get_screen('test.png')

    def getRowValues(self):
        row = self.selectRow
        action = self.macroTable.cellWidget(row, 0).currentText()
        value = self.macroTable.item(row, 1).text()
        return (action, value)

    def nextAction(self):
        self.selectRow = self.selectRow + 1
        if self.selectRow >= self.macroTable.rowCount():
            self.selectRow = 0
        self.macroTable.selectRow(self.selectRow)
        action, value = self.getRowValues()
        self.actionController.setAction(action, value)

    @pyqtSlot()
    def actionDone(self):
        self.nextAction()
        self.leCurrentCount.setText(str(self.core.fileNumber))

    @pyqtSlot(str)
    def addImage(self, path):
        self.addCaptureFile(path)
        self.lastLsFileSelect()

    def clickCapture(self):
        file = self.core.newFilePath()
        get_screen(file)
        self.addCaptureFile(file)
        self.lsFiles.scrollToBottom()
        self.lastLsFileSelect()

    def pil2pixmap(self, image):
        bytesImg = io.BytesIO()
        image.save(bytesImg, format='JPEG')

        qImg = QImage()
        qImg.loadFromData(bytesImg.getvalue())

        return QPixmap.fromImage(qImg)

    def loadCaptureFiles(self):
        self.lsFiles.clear()
        files = os.listdir(self.core.capturePath)
        for file in files:
            path = os.path.join(self.core.capturePath, file)
            self.addCaptureFile(path)
        self.startFileNumber()

    def startFileNumber(self):
        files = os.listdir(self.core.capturePath)
        p = re.compile('^\d+.jpg$')
        files = [s for s in files if p.match(s)]
        if len(files) == 0:
            self.core.fileNumber = 0
            return
        basename = os.path.basename(files[-1])
        num = int(os.path.splitext(basename)[0])
        self.core.fileNumber = num
        self.leCurrentCount.setText(str(num))

    def addCaptureFile(self, path):
        print('📢[main.pyw:243]:', path)
        # or not (path.endswith(".jpg") and path.endswith(".png")):
        if os.path.isdir(path) or not (path.endswith(".jpg")):
            return
        picture = Image.open(path)
        picture.thumbnail((80, 120), Image.ANTIALIAS)

        try:
            icon = QIcon(self.pil2pixmap(picture))
            item = QListWidgetItem(os.path.basename(path), self.lsFiles)
            item.setStatusTip(path)
            item.setIcon(icon)
        except Exception as e:
            print(e)

    def onCaptureFileChanged(self):
        item = self.lsFiles.selectedItems()
        if len(item) > 0:
            path = os.path.join(self.core.capturePath, item[0].text())
            self.previewDisplay(path)

    def previewDisplay(self, path):
        pix = QPixmap()
        pix.load(path)
        pix = pix.scaledToWidth(self.lbPreview.width(),
                                Qt.SmoothTransformation)
        self.lbPreview.setPixmap(pix)

    def clickDeleteSelectFile(self):
        try:
            item = self.lsFiles.selectedItems()
            row = self.lsFiles.currentRow()
            if len(item) > 0:
                os.remove(os.path.join(self.core.capturePath, item[0].text()))
                self.lsFiles.takeItem(row)
        except Exception as e:
            print(e)

    def lastLsFileSelect(self):
        self.lsFiles.setCurrentRow(self.lsFiles.count() - 1)

    def clickDeleteAllFiles(self):
        ret = QMessageBox.question(
            self, "경고", "정말 모든 파일을 지우시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if ret == QMessageBox.Yes:
            try:
                for file in ['*.png', '*.jpg']:
                    path = os.path.join(self.core.capturePath, file)
                    files = glob.glob(path)
                    removePathFiles(files)
                self.lsFiles.clear()
                self.startFileNumber()
            except Exception as e:
                print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec_())
