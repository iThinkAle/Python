# Questo programma genera una password casuale rispettando diversi parametri che l'utente inserisce.
# By iThinkAle

import sys
import random
import string
import time

letterList = list(string.ascii_letters+string.digits+string.ascii_lowercase +
                  string.ascii_uppercase+"[]+*ç@#°§()%&$£/=?'^|-_")

print("Ciao e benvenuto sul generatore di password casuali! By Ale.")


def main():

    passwordCharacters = int(input("Digita il numero dei caratteri che vuoi per la tua password: "))

    random.shuffle(letterList)

    password = []

    for i in range(passwordCharacters):
        password.append(random.choice(letterList))

    random.shuffle(password)

    print("".join(password))

    print("Ricordati di salvare la password!")

    anotherPass = input("Vuoi generare un'altra password? S/N ")

    if anotherPass == "S" or anotherPass == "s":
        print("Ok! Premi INVIO per continuare.")
        input()
        print("Aspetta qualche secondo prima di generare una nuova password")
        time.sleep(3)
        main()

    elif anotherPass == "N" or anotherPass == "s":
        print("Grazie per aver usato il generatore. Ciao!")
        input()
        sys.exit()
    else:
        print("Errore (digita una delle opzioni)")
        sys.exit()


if __name__ == "__main__":
    main()
