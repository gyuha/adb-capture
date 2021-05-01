import subprocess
import os
import sys


def get_screen(filename):
    print(filename)
    cmd = "adb  shell screencap -p"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    binary_screenshot = process.stdout.read()

    binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')
    with open(filename, 'wb') as f:
        f.write(binary_screenshot)
