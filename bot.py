import pyautogui
from numpy import *
import time
from PIL import ImageGrab, ImageOps

class coordinate ():
    replyBtn = (357, 365)  # Original numbers 357, 365
    dinosaur = (146, 369)
    # x and y coordinate of top left: X ->168,  y ->378
    # y intersect -> 387


def restartGame():
    pyautogui.doubleClick(coordinate.replyBtn)


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')


def imageGrab():
    box = (coordinate.dinosaur[0] + 44, coordinate.dinosaur[1], coordinate.dinosaur[0] + 189, coordinate.dinosaur[1]+22)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab() != 1447):
            pressSpace()
            time.sleep(0.1)

main()


while True:
    imageGrab()


restartGame()

time.sleep(1)

pressSpace()
