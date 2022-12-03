# Questo software aggiorna la repository di GitHub automaticamente muovendo il mouse al posto tuo.
# By iThinkAle

import pyautogui as pag

print("Aggiornando repository di GitHub...")
pag.moveTo(1744, 85, 0.2)
pag.click()
pag.moveTo(183, 746, 0.2)
pag.sleep(2)
pag.click()
pag.moveTo(1201, 792, 0.2)
pag.sleep(4)
pag.click()
pag.alert("Repository aggiornata")


