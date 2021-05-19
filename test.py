import time

from adb.adbKey import AdbKey, send_adb_key
from adb.capture import get_screen, imageCrop
from libs.imagesPathToPdf import imagesPathToPdf

# print(AdbKey.KEYCODE_DPAD_DOWN.value)

for i in range(236):
    # for i in range(3):
    filepath = "./capture/b{:04d}.png".format(i)
    print('Capture : ', filepath, end="\r")
    get_screen(filepath)
    imageCrop(filepath, 0, 485, 1080, 2015, True)
    send_adb_key(AdbKey.KEYCODE_VOLUME_DOWN.value)
    time.sleep(0.2)
