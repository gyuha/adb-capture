import sys
import os
from PyQt5 import QtCore, QtWidgets


class Worker(QtCore.QObject):
    loaded = QtCore.pyqtSignal(int, str)
    finished = QtCore.pyqtSignal()

    def __init__(self, files):
        super().__init__()
        self._files = files

    def run(self):
        self._stop = False
        for count, file in enumerate(self._files, 1):
            QtCore.QThread.sleep(2)  # process file...
            self.loaded.emit(count, file)
            if self._stop:
                break
        self.finished.emit()

    def stop(self):
        self._stop = True


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = QtWidgets.QPushButton('Choose Files')
        self.button.clicked.connect(self.showOpenDialog)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button)
        self.thread = QtCore.QThread()

    def showOpenDialog(self):
        files, filters = QtWidgets.QFileDialog.getOpenFileNames(
            self, 'Open file(s)', '',
            'Raw files (*.rw.dat);;Data files (*.dat)'
            ';;Text files (*.txt);;All files (*)',
            'All files (*)')
        if files and not self.thread.isRunning():
            self.worker = Worker(files)
            self.worker.moveToThread(self.thread)
            self.worker.finished.connect(self.thread.quit)
            self.thread.started.connect(self.worker.run)
            self.thread.finished.connect(self.worker.deleteLater)
            self.showProgress(
                'Loading file(s)...', len(files), self.worker.stop)
            self.worker.loaded.connect(self.updateProgress)
            self.thread.start()

    def updateProgress(self, count, file):
        if not self.progress.wasCanceled():
            self.progress.setLabelText(
                'Loaded: %s' % os.path.basename(file))
            self.progress.setValue(count)
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Load Files', 'Loading Aborted!')

    def showProgress(self, text, length, handler):
        self.progress = QtWidgets.QProgressDialog(
            text, "Abort", 0, length, self)
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.canceled.connect(
            handler, type=QtCore.Qt.DirectConnection)
        self.progress.forceShow()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 100, 100, 50)
    window.show()
    sys.exit(app.exec_())
