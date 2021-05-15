from PyQt5 import QtCore, QtGui, QtWidgets


class DirectoryView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

        self.listview = QtWidgets.QListView()
        self.listview.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection)
        self.fileModel = QtWidgets.QFileSystemModel(nameFilterDisables=False)
        self.listview.setModel(self.fileModel)

        self.cb = QtWidgets.QComboBox()
        self.cb.currentTextChanged.connect(self.filterChanged)

        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.listview)
        layout.addWidget(self.cb)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
            for url in e.mimeData().urls():
                if url.isLocalFile():
                    if self.updateDirectoryView(url.toLocalFile()):
                        break

    def updateDirectoryView(self, path):
        fi = QtCore.QFileInfo(path)
        if fi.isDir():
            self.listview.setRootIndex(self.fileModel.setRootPath(path))
            d = QtCore.QDir(path)
            suffixes = set()
            for fi in d.entryInfoList(filters=QtCore.QDir.Files):
                if fi.isFile():
                    suffixes.add("."+fi.suffix())
            self.cb.clear()
            self.cb.addItems(sorted(suffixes))
            return True
        return False

    @QtCore.pyqtSlot(str)
    def filterChanged(self, text):
        self.fileModel.setNameFilters(["*"+text])


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = DirectoryView()
    w.show()
    sys.exit(app.exec_())
