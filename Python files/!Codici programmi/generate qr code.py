# Generatore di QR Codes

import time
import pyqrcode
import sys


def generateqrcode():
    string = input("Inserisci l'URL o la frase che vuoi inserire nel qr code: ")
    path = input("Digita la path in cui salvare il file (Es: C:\Users\user\Documents\): ")
    name = input("Digita il nome del file (escludi .png): ")

    url = pyqrcode.create(string)
    url.png(path+name+".png", scale=6)\

    aqrcode = input("Vuoi generare un altro qr code? S/N: ")

    if aqrcode == "S" or aqrcode == "s":
        print("Aspetta qualche secondo prima di generarne un altro qr code")
        time.sleep(3)
        print("Premi INVIO per continuare")
        input()
        generateqrcode()

    if aqrcode == "N" or aqrcode == "n":
        print("Il programma verrà chiuso fra qualche secondo")
        time.sleep(3)
        sys.exit()


def inizio():
    print("Benvenuto nel generatore di QR Codes!")
    print(input("Premi invio per continuare..."))
    generateqrcode()


inizio()
