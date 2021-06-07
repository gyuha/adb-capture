import io
import subprocess
import os
import sys
from PIL import Image


def get_screen(filename, toJpg=True):
    print(filename)
    cmd = "adb  shell screencap -p"
    try:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        binary_screenshot = process.stdout.read()
        binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')

        if toJpg:
            filename = filename.replace('.png', '.jpg')
            img = Image.open(io.BytesIO(binary_screenshot))
            img = img.convert('RGB')
            img.save(filename, format='JPEG', quality=90)
        else:
            with open(filename, 'wb') as f:
                f.write(binary_screenshot)
    except Exception:
        print(Exception)


def imageCrop(filename, x, y, width, height, toJpg=False):
    try:
        img = Image.open(filename)
        area = (x, y, width, height)
        croppedImg = img.crop(area)
        img.close()

        if toJpg:
            os.remove(filename)
            filename = filename.replace('.png', '.jpg')
            croppedImg = croppedImg.convert('RGB')
            croppedImg.save(filename, quality=90)
        else:
            croppedImg.save(filename)
    except Exception:
        print(Exception)
