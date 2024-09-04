import time
import pyautogui as pag


def mine():
    for _ in range(5):
        time.sleep(6)
        pag.click()
    pag.move(80, 0)
    chop()


def chop():
    time.sleep(2)
    pag.click()
    pag.move(-80, 0)
    mine()


mine()
