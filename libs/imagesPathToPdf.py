import os
from fpdf import FPDF


def imagesPathToPdf(imagesPath, pdfFileName='bookTItle.pdf'):
    pdf = FPDF()
    # imagelist is the list with all image filenames
    imageList = []
    for file in os.listdir(imagesPath):
        if file.endswith(".jpg"):
            imageList.append(os.path.join(imagesPath, file))

    for image in imageList:
        pdf.add_page()
        pdf.image(image, x=0, y=0, w=210, h=297)
    pdf.output(pdfFileName, "F")

    # print([i for i in os.listdir(os.getcwd()+imagesPath) if i.endswith(".jpg")])
    # # try:
    # with open(pdfFileName, 'wb') as f:
    #     f.write(img2pdf.convert(
    #         [i for i in os.listdir(imagesPath) if i.endswith(".jpg")]))
    # # except:
    # #     print('Error')
