from speedComparison import getTime


import pyautogui as py
import ctypes


py.FAILSAFE = False


user32 = ctypes.WinDLL('user32', use_last_error=True)
def move_mouse_ctypes(x, y):
    user32.SetCursorPos(x, y)

def move_mouse_pyauto(x, y):
    py.moveTo(x, y)


def funktion1():
    move_mouse_ctypes(100, 100)  
    

def funktion2():
    move_mouse_pyauto(200, 200)  


getTime()