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
    pdfSaveProgress = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self, imagesPath, pdfFileName):
        self.running = True
        pdf = FPDF()
        # imagelist is the list with all image filenames
        imageList = []
        self.pdfSaveProgress.emit(0)
        files = os.listdir(imagesPath)
        fileCount = len(files)
        count = 0
        for file in files:
            count = count + 1
            self.pdfSaveProgress.emit(int((count / (fileCount / 2)) * 100))
            if file.endswith(".jpg"):
                imageList.append(os.path.join(imagesPath, file))

        imageCount = len(imageList)
        count = 0
        for image in imageList:
            self.pdfSaveProgress.emit(
                50 + int((count / (imageCount / 2)) * 100))
            pdf.add_page()
            pdf.image(image, x=0, y=0, w=210, h=297)
        pdf.output(pdfFileName, "F")
        self.pdfSaveProgress.emit(100)
        self.pdfSaveDone.emit()
