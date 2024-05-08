from speedComparison import getTime
import random
import pyautogui as py
py.FAILSAFE = False
import ctypes
user32 = ctypes.WinDLL('user32', use_last_error=True)




# def move_mouse_ctypes(x, y): #10.000 times faster
#     user32.SetCursorPos(x, y)

# def move_mouse_pyauto(x, y):
#     py.moveTo(x, y)








getTime()
