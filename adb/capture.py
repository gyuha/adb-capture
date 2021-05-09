import subprocess
import os
import sys
from PIL import Image


def get_screen(filename):
    print(filename)
    cmd = "adb  shell screencap -p"
    try:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        binary_screenshot = process.stdout.read()

        binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')
        with open(filename, 'wb') as f:
            f.write(binary_screenshot)
    except Exception:
        print(Exception)


def imageCrop(filename, x, y, width, height, toJpg=False):
    img = Image.open(filename)
    area = (x, y, width, height)
    croppedImg = img.crop(area)
    img.close()
    try:
        if toJpg:
            os.remove(filename)
            filename = filename.replace('.png', '.jpg')
            croppedImg = croppedImg.convert('RGB')
            croppedImg.save(filename, quality=85)
        else:
            croppedImg.save(filename)
    except Exception:
        print(Exception)
