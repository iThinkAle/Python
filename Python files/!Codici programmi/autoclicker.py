# Semplicissimo autoclicker
# By iThinkAle

import pyautogui as pag
import time


scelta_tasto = input("Che tasto vuoi che venga cliccato? (left, right, middle) ")
tempo = float(input("Ogni quanto vuoi che venga cliccato? (in secondi) "))

try:
    while True:
        pag.click(button=scelta_tasto)
        time.sleep(tempo)
