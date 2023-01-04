# Questo software aggiorna la repository di GitHub automaticamente muovendo il mouse al posto tuo.
# By iThinkAle
# DISCLAIMER: CODESTO PROGRAMMA FUNZIONA SOLO IN PYCHARM CON FINESTRA A SCHERMO INTERO. IN ALTRI PROGRAMMI O NEL CASO
# PYCHARM NON DOVESSE ESSERE SCHERMO INTERO IL PROGRAMMA NON FUNZIONERA'.

import time
import pyautogui as pag
import keyboard as kb


print("Aggiornando repository di GitHub...")
pag.moveTo(1744, 85, 0.2)
pag.click()
pag.alert("Ora scrivere il messaggio e selezionare i file da aggiornare nella repository. Appena finito, premere F1")
time.sleep(2)
kb.is_pressed("enter")
pag.moveTo(169, 767, 0.2)
pag.click()
pag.moveTo(1201, 792, 0.2)
pag.sleep(3)
pag.click()
pag.alert("Repository aggiornata")
