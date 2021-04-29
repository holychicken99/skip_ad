
import random
import time

import keyboard
import pyautogui
import win32api
import win32con
from pyautogui import *



while 1:
    if pyautogui.locateOnScreen('Capture.png',confidence=0.6,grayscale=True)!=None:
        a,b,c,d = pyautogui.locateOnScreen('Capture.png',confidence=0.6,grayscale=True)
        a+=15
        print(a)
        b+=20
        print(b)
        pyautogui.click(x=a,y=b)
        
        
       # print(type(pyautogui.locateOnScreen('Capture.png',confidence=0.5,grayscale=True)))
        time.sleep(0.5)
   