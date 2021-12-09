#codes/custom-meet-scr/start.py
#изпробвано на 1920х1080
#ако имате 2 монитора или повече - ще го изпълни на най - левия
import pyautogui
import webbrowser
import time

def click():
    pyautogui.moveTo(771, 767, 2)
    pyautogui.click()
    pyautogui.moveTo(688, 785, 0.5)
    pyautogui.click()
    pyautogui.moveTo(1281, 641, 2)
    pyautogui.click()

click()
