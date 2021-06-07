import subprocess
import os
import sys
from enum import Enum


class AdbKey(Enum):
    KEYCODE_UNKNOWN = "KEYCODE_UNKNOWN"
    KEYCODE_MENU = "KEYCODE_MENU"
    KEYCODE_SOFT_RIGHT = "KEYCODE_SOFT_RIGHT"
    KEYCODE_HOME = "KEYCODE_HOME"
    KEYCODE_BACK = "KEYCODE_BACK"
    KEYCODE_CALL = "KEYCODE_CALL"
    KEYCODE_ENDCALL = "KEYCODE_ENDCALL"
    KEYCODE_0 = "KEYCODE_0"
    KEYCODE_1 = "KEYCODE_1"
    KEYCODE_2 = "KEYCODE_2"
    KEYCODE_3 = "KEYCODE_3"
    KEYCODE_4 = "KEYCODE_4"
    KEYCODE_5 = "KEYCODE_5"
    KEYCODE_6 = "KEYCODE_6"
    KEYCODE_7 = "KEYCODE_7"
    KEYCODE_8 = "KEYCODE_8"
    KEYCODE_9 = "KEYCODE_9"
    KEYCODE_STAR = "KEYCODE_STAR"
    KEYCODE_POUND = "KEYCODE_POUND"
    KEYCODE_DPAD_UP = "KEYCODE_DPAD_UP"
    KEYCODE_DPAD_DOWN = "KEYCODE_DPAD_DOWN"
    KEYCODE_DPAD_LEFT = "KEYCODE_DPAD_LEFT"
    KEYCODE_DPAD_RIGHT = "KEYCODE_DPAD_RIGHT"
    KEYCODE_DPAD_CENTER = "KEYCODE_DPAD_CENTER"
    KEYCODE_VOLUME_UP = "KEYCODE_VOLUME_UP"
    KEYCODE_VOLUME_DOWN = "KEYCODE_VOLUME_DOWN"
    KEYCODE_POWER = "KEYCODE_POWER"
    KEYCODE_CAMERA = "KEYCODE_CAMERA"
    KEYCODE_CLEAR = "KEYCODE_CLEAR"


def send_adb_key(keymap):
    adbPath = os.path.realpath('./bin/scrcpy/adb.exe')
    cmd = [adbPath, "shell", "input", "keyevent", keymap]
    try:
        subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError:
        print('connect error')
