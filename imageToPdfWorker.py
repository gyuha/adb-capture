import os
import sys
import time

from fpdf import FPDF
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from adb.ScrcpyCapture import ScrCpyCapture
from core import mainCore


class ImageToPdfWorker(QThread):
    pdfSaveDone = pyqtSignal()
    updateProgress = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = False
        self.imagePath = None
        self.pdfFileName = None

    def setFiles(self, imagePath, pdfFileName):
        self.imagePath = imagePath
        self.pdfFileName = pdfFileName

    def run(self):
        self.running = True
        pdf = FPDF()
        # imagelist is the list with all image filenames
        imageList = []
        self.updateProgress.emit(0)
        print('📢[imageToPdfWorker.py:32]:', self.imagePath)
        files = os.listdir(self.imagePath)
        fileCount = len(files)
        count = 0
        for file in files:
            if not self.running:
                return
            count = count + 1
            self.updateProgress.emit(int((count / (fileCount / 2)) * 100))
            if file.endswith(".jpg"):
                imageList.append(os.path.join(self.imagePath, file))

        imageCount = len(imageList)
        count = 0
        for image in imageList:
            if not self.running:
                return
            self.updateProgress.emit(
                50 + int((count / (imageCount / 2)) * 100))
            pdf.add_page()
            pdf.image(image, x=0, y=0, w=210, h=297)
        pdf.output(self.pdfFileName, "F")
        self.updateProgress.emit(100)
        self.pdfSaveDone.emit()
        self.running = False

    def stop(self):
        self.running = False
