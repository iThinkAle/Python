# Questo programma scrive ripetutamente una frase prefissata per un numero di volte settato
# By iThinkAle

import pyautogui as pag


def inizio():
    global text, number, time
    text = input(str("Digita il testo da spammare: "))
    number = input("Digita il numero di volte che vuoi che il testo venga scritto: ")
    time = float(input("Digita ogni quanto tempo (in secodi) vuoi che il testo venga scritto: "))
    program()


def program():
    count = 0
    while count <= int(number):
        pag.typewrite(text + " " + str(count))
        pag.press("enter")
        count += 1
        pag.sleep(int(time))


inizio()