import math
import sys

# OPERAZIONI


def addizione():
    print("Addizione")
    a = float(input("Inserisci il primo numero:  "))
    b = float(input("Inserisci secondo numero: "))
    print("Il risultato dell'operazione é: " + str(a + b))


def sottrazione():
    print("Sottrazione")
    a = float(input("Inserisci il primo numero:  "))
    b = float(input("Inserisci secondo numero: "))
    print("Il risultato dell'operazione é: " + str(a - b))


def moltiplicazione():
    print("Moltiplicazione")
    a = float(input("Inserisci il primo numero:  "))
    b = float(input("Inserisci secondo numero: "))
    print("Il risultato dell'operazione é: " + str(a * b))


def divisione():
    print("Divisione")
    a = float(input("Inserisci il primo numero:  "))
    b = float(input("Inserisci secondo numero: "))
    print("Il risultato dell'operazione é: " + str(a / b))


def potenza():
    print("Potenza")
    a = float(input("Inserisci il numero da elevare:  "))
    b = float(input("Inserisci l'esponente: "))
    print("Il numero " + str(a) + " elevato a " + str(b) + " é: " + str(math.pow(a, b)))


def radicequadrata():
    print("Radice quadrata")
    rq = float(input("Inserisci numero: "))
    print("La radice quadrata di " + str(rq) + " è: " + str(math.sqrt(rq)))


def fattoriale():
    print("Fattoriale")
    ft = int(input("Inserisci numero: "))
    print("Il fattoriale di " + str(ft) + " è: " + str(math.factorial(ft)))


############################################################################################################
# SCELTA OPERAZIONI

def main():

    print("Benvenuto nella calcolatrice! By Ale. Per prima cosa, che operazione vuoi svolgere? Scegli tra: \n"
          "Addizione: digita 1; \n"
          "Sottrazione: digita 2; \n"
          "Moltiplicazione: digita 3; \n"
          "Divisione: digita 4; \n"
          "Potenza: digita 5; \n"
          "Radice quadrata: digita 6; \n"
          "Fattoriale (solo numeri interi): digita 7; \n"
          "Per chiudere la calcolatrice: digita ESC \n")

    x = input("Scegli l'operazione: ")

    if x == "1":
        addizione()

    elif x == "2":
        sottrazione()

    elif x == "3":
        moltiplicazione()

    elif x == "4":
        divisione()

    elif x == "5":
        potenza()

    elif x == "6":
        radicequadrata()

    elif x == "7":
        fattoriale()

    elif x == "ESC" or x == "esc":
        print("La calcolatrice si chiuderà ora!")
        input()
        sys.exit()
    else:
        print("Errore (digita una delle opzioni)")
        sys.exit()

    loop = input("Vuoi continuare ad usare la calcolatrice? S/N ")

    if loop == "S" or loop == "s":
        print("Sto tornando al menù principale!"
              " ")
        input()
    elif loop == "N" or "n":
        print("La calcolatrice verrà chiusa ora!")
        input()
        sys.exit()
    else:
        print("Errore (digita una delle opzioni)")
        sys.exit()


if __name__ == "__main__":
    main()
