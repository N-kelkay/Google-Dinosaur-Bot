import pyautogui
import time

class coordinate():
    replyBtn = (357, 365)

def restartGame():
    pyautogui.doubleClick(coordinate.replyBtn)

restartGame()