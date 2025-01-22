# Questo programma muove il mouse in una posizione random ogni 5 secondi.
# By iThinkAle

import pyautogui as pag
import time
import random

while True:
    x = (random.randint(600, 800))
    y = (random.randint(200, 600))

    pag.moveTo(x, y, 0.5)
    time.sleep(0.2)


if __name__ == "__main__":
    main()
