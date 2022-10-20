import math
import sys


def main():
    while True:
        print("Benvenuto nella calcolatrice! By Ale. Per prima cosa, che operazione vuoi svolgere? Scegli tra: \n"
          "Addizione: digita 1; \n"
          "Sottrazione: digita 2; \n"
          "Moltiplicazione: digita 3; \n"
          "Divisione: digita 4; \n"
          "Potenza: digita 5; \n"
          "Radice quadrata: digita 6; \n"
          "Fattoriale: digita 7; \n"
          "Per chiudere la calcolatrice: digita ESC \n")

        x = input("Scegli l'operazione: ")

        if x == "1":
            print("Addizione")
            a = float(input("Inserisci il primo numero:  "))
            b = float(input("Inserisci secondo numero: "))
            print("Il risultato dell'operazione é: " + str(a + b))

        elif x == "2":
            print("Sottrazione")
            a = float(input("Inserisci il primo numero:  "))
            b = float(input("Inserisci secondo numero: "))
            print("Il risultato dell'operazione é: " + str(a - b))

        elif x == "3":
            print("Moltiplicazione")
            a = float(input("Inserisci il primo numero:  "))
            b = float(input("Inserisci secondo numero: "))
            print("Il risultato dell'operazione é: " + str(a * b))

        elif x == "4":
            print("Divisione")
            a = float(input("Inserisci il primo numero:  "))
            b = float(input("Inserisci secondo numero: "))
            print("Il risultato dell'operazione é: " + str(a / b))

        elif x == "5":
            print("Potenza")
            a = float(input("Inserisci il numero da elevare:  "))
            b = float(input("Inserisci l'esponente: "))
            print("Il numero "+str(a)+" elevato a "+str(b)+" é: "+str(math.pow(a, b)))

        elif x == "6":
            print("Radice quadrata")
            rq = float(input("Inserisci numero: "))
            print("La radice quadrata di "+str(rq)+" è: "+str(math.sqrt(rq)))

        elif x == "7":
            print("Fattoriale")
            ft = float(input("Inserisci numero: "))
            print("Il fattoriale di "+str(ft)+" è: "+str(math.factorial(ft)))

        elif x == "ESC" or x == "esc":
            print("La calcolatrice si chiuderà ora!")
            input()
            sys.exit()

        loop = input("Vuoi continuare ad usare la calcolatrice? S/N ")

        if loop == "S" or loop == "s":
            print("Sto tornando al menù principale!"
              " ")
            input()
            continue

        elif loop == "N" or "n":
            print("La calcolatrice verrà chiusa ora!")
            input()
            sys.exit()


if __name__ == "__main__":
    main()
