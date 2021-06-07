import os
import sys
import time
from PIL import Image

from fpdf import FPDF
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from adb.ScrcpyCapture import ScrCpyCapture
from core import mainCore


class ImageToPdfWorker(QThread):
    pdfSaveDone = pyqtSignal()
    updateProgress = pyqtSignal(int, str)

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
        self.updateProgress.emit(0, 'start')
        files = os.listdir(self.imagePath)
        fileCount = len(files)
        count = 0
        for file in files:
            if not self.running:
                return
            count = count + 1
            self.updateProgress.emit(
                int((count / (fileCount * 3)) * 100), 'image add')
            if file.endswith(".jpg"):
                imageList.append(os.path.join(self.imagePath, file))

        imageCount = len(imageList)
        count = 0

        # 이미지 비율 가져 오기
        im = Image.open(imageList[0])
        rate = im.width / im.height
        width = 210
        height = 297

        for image in imageList:
            if not self.running:
                return
            count = count + 1
            self.updateProgress.emit(
                35 + int((count / (imageCount * 3)) * 100), 'image convert')
            pdf.add_page()

            x = ((width*(3/4) - (width*rate)) / 2)
            x = x if x > 0 else 0

            w = (height*rate)
            w = width if w > width else w

            pdf.image(image, x=x,
                      y=0, w=w, h=height)
        self.updateProgress.emit(80, 'save to pdf')
        pdf.output(self.pdfFileName, "F")
        self.updateProgress.emit(100, 'complete')
        self.pdfSaveDone.emit()
        self.running = False

    def stop(self):
        self.running = False
