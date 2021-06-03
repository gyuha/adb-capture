import sys
from libs.imagesPathToPdf import imagesPathToPdf


def usage():
    print("python " + sys.argv[0] + " [fileName]")


if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        usage()
        exit(1)

    imagesPathToPdf('./capture/', sys.argv[1])
