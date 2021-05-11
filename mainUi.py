# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.edtCapturePath = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.edtCapturePath.setFont(font)
        self.edtCapturePath.setAccessibleName("")
        self.edtCapturePath.setObjectName("edtCapturePath")
        self.gridLayout.addWidget(self.edtCapturePath, 0, 0, 1, 1)
        self.btnPathSelect = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnPathSelect.setFont(font)
        self.btnPathSelect.setAccessibleName("")
        self.btnPathSelect.setObjectName("btnPathSelect")
        self.gridLayout.addWidget(self.btnPathSelect, 0, 1, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.macroTable = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.macroTable.setFont(font)
        self.macroTable.setRowCount(0)
        self.macroTable.setObjectName("macroTable")
        self.macroTable.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.macroTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.macroTable.setHorizontalHeaderItem(1, item)
        self.macroTable.verticalHeader().setVisible(True)
        self.macroTable.verticalHeader().setHighlightSections(True)
        self.verticalLayout_4.addWidget(self.macroTable)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.checkBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_4)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCapture = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnCapture.setFont(font)
        self.btnCapture.setObjectName("btnCapture")
        self.horizontalLayout.addWidget(self.btnCapture)
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnStop.setFont(font)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbFileList = QtWidgets.QLabel(self.centralwidget)
        self.lbFileList.setObjectName("lbFileList")
        self.verticalLayout_3.addWidget(self.lbFileList)
        self.lsFiles = QtWidgets.QTableWidget(self.centralwidget)
        self.lsFiles.setFrameShape(QtWidgets.QFrame.Box)
        self.lsFiles.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lsFiles.setTextElideMode(QtCore.Qt.ElideLeft)
        self.lsFiles.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.lsFiles.setShowGrid(True)
        self.lsFiles.setGridStyle(QtCore.Qt.SolidLine)
        self.lsFiles.setWordWrap(True)
        self.lsFiles.setCornerButtonEnabled(True)
        self.lsFiles.setRowCount(0)
        self.lsFiles.setColumnCount(2)
        self.lsFiles.setObjectName("lsFiles")
        item = QtWidgets.QTableWidgetItem()
        self.lsFiles.setHorizontalHeaderItem(0, item)
        self.lsFiles.horizontalHeader().setVisible(True)
        self.lsFiles.verticalHeader().setVisible(False)
        self.lsFiles.verticalHeader().setHighlightSections(True)
        self.verticalLayout_3.addWidget(self.lsFiles)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnDeleteFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteFile.setObjectName("btnDeleteFile")
        self.horizontalLayout_3.addWidget(self.btnDeleteFile)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADB Caputre automate"))
        self.label_4.setText(_translate("MainWindow", "ADB capture automate"))
        self.label.setText(_translate("MainWindow", "저장경로"))
        self.edtCapturePath.setText(_translate("MainWindow", "./caputre"))
        self.btnPathSelect.setText(_translate("MainWindow", "선택"))
        self.label_2.setText(_translate("MainWindow", "실행"))
        item = self.macroTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Action"))
        item = self.macroTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.checkBox.setText(_translate("MainWindow", "편집"))
        self.pushButton_2.setText(_translate("MainWindow", "추가"))
        self.pushButton.setText(_translate("MainWindow", "삭제"))
        self.btnCapture.setText(_translate("MainWindow", " 캡쳐"))
        self.btnStart.setText(_translate("MainWindow", "시작"))
        self.btnStop.setText(_translate("MainWindow", "정지"))
        self.lbFileList.setText(_translate("MainWindow", "파일 목록"))
        self.lsFiles.setSortingEnabled(False)
        item = self.lsFiles.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File Name"))
        self.btnDeleteFile.setText(_translate("MainWindow", "삭제"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
