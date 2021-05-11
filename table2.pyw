# QTableWidget Control Usage
from PyQt5.QtWidgets import QComboBox, QTableView, QAbstractItemView, QHeaderView, QTableWidget, QTableWidgetItem, QMessageBox, QListWidget, QListWidgetItem, QStatusBar,  QMenuBar, QMenu, QAction, QLineEdit, QStyle, QFormLayout,   QVBoxLayout, QWidget, QApplication, QHBoxLayout, QPushButton, QMainWindow, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel, QCursor, QFont, QBrush, QColor
from PyQt5.QtCore import QStringListModel, QAbstractListModel, QModelIndex, QSize, Qt

import sys


class WindowClass(QWidget):

    def __init__(self, parent=None):

        super(WindowClass, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.resize(400, 300)
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)  # Rows
        tableWidget.setColumnCount(4)  # Number of columns
        # All columns stretch automatically to fill the interface
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Set only one row to be selected
        tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # Not editable
        # Set only the row to be selected, the entire row is selected
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Set the column width and height to adapt to the content
        tableWidget.resizeColumnsToContents()
        # Set the line width and height to adapt to the content
        tableWidget.resizeRowsToContents()
        # tableWidget.horizontalHeader().setVisible(False)#Set the column heading to hide (for the column heading horizontal arrangement)
        # tableWidget.verticalHeader().setVisible(False)#Set the column heading to hide (vertical arrangement for the column heading)
        self.layout.addWidget(tableWidget)
        # Horizontal header arrangement, if setVerticalHeaderLabels is used, it is vertical header arrangement
        tableWidget.setHorizontalHeaderLabels(
            ['Name', 'address', 'age', 'operating'])
        items = [['JONES', 'Beijing', '23', ''], ['SMITH', 'SHAngHai', '23', ''], [
            'ZY', 'Tianjin', '23', ''], ['Smith', 'SJT', '22', '']]
        for i in range(len(items)):  # Note that the numbers in the above list are added with single quotes, otherwise they will not be displayed below (or the str method below can be converted)
            item = items[i]

            for j in range(len(item)):
                #-----------------------------After the program is modified, add a button in the last column------------ -------#
                if j != 3:
                    item = QTableWidgetItem(str(items[i][j]))
                    tableWidget.setItem(i, j, item)
                else:  # Add controls in the last column
                    btn = QPushButton("delete")
                    btn.setDown(True)
                    btn.setStyleSheet("QPushButton{margin:3px};")
                    tableWidget.setCellWidget(i, j, btn)
#--------------------------------------------------------------------------#

#------------------------------0,1 position add drop-down list box----------- -----------#
        # Set a cell as a control
        comBox = QComboBox()
        comBox.addItem("Beijing")
        comBox.addItems(["Shanghai", "Tianjin"])
        comBox.setStyleSheet("QComboBox{margin:3px};")
        tableWidget.setCellWidget(0, 1, comBox)
#------------------------------------------------------------------------#
        # Font settings
        newItem = tableWidget.item(0, 0)
        newItem.setFont(QFont("Times", 12, QFont.Black))  # Font style bold
        newItem.setForeground(QBrush(QColor(255, 0, 0)))  # font color
        # Set Sort
        # Qt.DescendingOrder Ascending descending order
        tableWidget.sortItems(1, Qt.AscendingOrder)
        item_00 = tableWidget.item(0, 0)
        item_00.setTextAlignment(Qt.AlignRight)  # Qt.AlignCenter ...
        # Merge Cells
        tableWidget.setSpan(0, 0, 3, 1)
        # Cell width and height settings
        # The first parameter is the row subscript
        tableWidget.setColumnWidth(0, 150)
        tableWidget.setRowHeight(0, 40)
        # Set not to display the dividing line
        tableWidget.setShowGrid(False)

        # Cell Settings Picture
        tableWidget.setItem(1, 1, QTableWidgetItem(
            QIcon("./image/add.ico"), "Baidu"))

        tableWidget.setItem(0, 0, newItem)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowClass()
    win.show()
    sys.exit(app.exec_())
