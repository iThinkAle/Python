# Questo programma scrive ripetutamente una frase prefissata per un numero di volte settato.
# By iThinkAle

import pyautogui as pag
import sys


def main():
    global text, number, time
    try:
        text = input(str("Digita il testo da spammare: "))
        number = int(input("Digita il numero di volte che vuoi che il testo venga scritto: "))
        time = float(input("Digita ogni quanto tempo (in secondi) vuoi che il testo venga scritto: "))
        program()
    except ValueError:
        print("Errore! Metti gli input al posto giusto! Riprova!")
        main()


def program():
    count = 0
    while count < int(number):
        pag.typewrite(text)
        pag.press("enter")
        pag.sleep(int(time))
        count += 1
    else:
        sys.exit()


if __name__ == "__main__":
    main()
