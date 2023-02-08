# Questo programma permette di creare dei QR Codes da URL e frasi.
# By iThinkAle


import time
import pyqrcode
import sys


def generateqrcode():
    string = input("Inserisci l'URL o la frase che vuoi inserire nel qr code: ")
    path = input("Digita la path in cui salvare il file (Es: C:/Users/[user]/Documents/)\n"
                 "Ricordati di utilizzare il backslash (Per questioni di codice non lo ho potuto utilizzare): ")
    name = input("Digita il nome del file (escludi .png): ")

    url = pyqrcode.create(string)
    url.png(path+name+".png", scale=6)

    aqrcode = input("Vuoi generare un altro qr code? S/N: ")

    if aqrcode == "S" or aqrcode == "s":
        print("Aspetta qualche secondo prima di generarne un altro qr code")
        time.sleep(3)
        print("Premi INVIO per continuare")
        input()
        generateqrcode()

    elif aqrcode == "N" or aqrcode == "n":
        print("Il programma verrà chiuso fra qualche secondo")
        time.sleep(3)
        sys.exit()
    else:
        print("Errore (digita una delle opzioni)")
        sys.exit()


def main():
    print("Benvenuto nel generatore di QR Codes!")
    print(input("Premi INVIO per continuare..."))
    generateqrcode()


if __name__ == "__main__":
    main()
