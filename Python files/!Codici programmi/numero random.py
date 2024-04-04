# Questo programma permettere di generare uno o più numeri random.
# By iThinkAle

import random
import sys


def main():

    print("Benvenuto nel generatore casuale di numeri.")
    dec = str(input("Se vuoi generare un numero decimale da 16 cifre dopo la virgola da 0 a 1 digita decimale.\n"
                    "Se non vuoi, digita avanti: "))

    if dec == "decimale" or dec == "Decimale":
        print(random.random())
        sys.exit()
    elif dec == "avanti" or dec == "Avanti":
        numero()
    else:
        print("Errore (digita una delle opzioni)")
        sys.exit()


def numero():

    a = int(input("Come prima cosa, digita il range di numeri da estrarre "
                  "(Es: digito 10, estrarrò un numero da 0 a 10): "))

    z = input("Vuoi generare un numero o una lista di numeri interi random da 0 a " + str(a) + "? (Digita 'uno' per\n"
              "uno solo e 'lista' per la lista o 'no' per generare nulla): ")

    if z == "uno" or z == "1":
        y = random.randint(0, int(a))
        print(y)
    elif z == "lista":
        b = input("Di quanti numeri vuoi la lista?: ")
        x = random.sample(range(0, int(a)), int(b))
        print(x)
    elif z == "no":
        print("Premi INVIO per chiudere il programma...")
        input()
        sys.exit()
    else:
        print("Errore (digita una delle opzioni)")
        sys.exit()


if __name__ == "__main__":
    main()
