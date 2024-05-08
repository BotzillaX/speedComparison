from speedComparison import getTime
from hashMap import key_constants
import time
import random
import pyautogui as py
py.FAILSAFE = False
import ctypes
user32 = ctypes.WinDLL('user32', use_last_error=True)
import keyboard





def keyComparison():
    KEYEVENTF_KEYDOWN = 0x0
    KEYEVENTF_KEYUP = 0x2
    text = """hello my name is"""


    for char in text:
        vk_code = key_constants[char]
        user32.keybd_event(vk_code, 0, KEYEVENTF_KEYDOWN, 0)
        
        user32.keybd_event(vk_code, 0, KEYEVENTF_KEYUP, 0)




def keyPyautogui():
    keyboard.write("""hello my name is""")


# keyComparison(text)

getTime(keyComparison, 30)
getTime(keyPyautogui, 30)


