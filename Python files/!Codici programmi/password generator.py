import sys
import random
import string
import time

x = list(string.ascii_letters+string.digits+string.ascii_lowercase+string.ascii_uppercase+"[]+*ç@#°§()%&$£/=?'^|-_")

print("Ciao e benvenuto sul generatore di password casuali! By Ale.")


def generate_password():

    y = int(input("Digita il numero dei caratteri che vuoi per la tua password: "))

    random.shuffle(x)

    password = []

    for i in range(y):
        password.append(random.choice(x))

    random.shuffle(password)

    print("".join(password))

    print("Ricordati di salvare la password!")
    z = input("Vuoi generare un'altra password? S/N ")

    if z == "S" or z == "s":
        print("Ok! Premi INVIO per continuare.")
        input()
        print("Aspetta qualche secondo prima di generare una nuova password")
        time.sleep(3)
        generate_password()

    elif z == "N" or z == "s":
        print("Grazie per aver usato il generatore. Ciao!")
        input()
        sys.exit()


generate_password()
