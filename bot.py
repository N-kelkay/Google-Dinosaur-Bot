from PIL import ImageGrab, ImageOps
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

def imageGrab():
    box = (coordinate.dinosaur[0] + 240, coordinate.dinosaur[1], coordinate.dinosaur[0] + 280, coordinate.dinosaur[1] + 30);
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)


restartGame()

time.sleep(1)

pressSpace()
