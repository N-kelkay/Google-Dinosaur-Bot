import pyautogui
import time


class coordinate ():
    replyBtn = (357, 365)
    dinosaur = (146, 369)


def restartGame():
    pyautogui.doubleClick(coordinate.replyBtn)


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')


restartGame()

time.sleep(1)

pressSpace()
