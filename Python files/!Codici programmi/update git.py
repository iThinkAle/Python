# Questo software aggiorna la repository di GitHub automaticamente muovendo il mouse al posto tuo.
# By iThinkAle
# DISCLAIMER: CODESTO PROGRAMMA FUNZIONA SOLO IN PYCHARM CON FINESTRA A SCHERMO INTERO. IN ALTRI PROGRAMMI O NEL CASO
# PYCHARM NON DOVESSE ESSERE SCHERMO INTERO IL PROGRAMMA NON FUNZIONERA'.

import pyautogui as pag

print("Aggiornando repository di GitHub...")
pag.moveTo(1744, 85, 0.2)
pag.click()
pag.moveTo(169, 767, 0.2)
pag.sleep(2)
pag.click()
pag.moveTo(1201, 792, 0.2)
pag.sleep(3)
pag.click()
pag.alert("Repository aggiornata")
