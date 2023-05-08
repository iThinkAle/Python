# Questo programma è ua classica calcolatrice con addizione, sottrazione, moltiplicazione, divisione,
# elevamento a potenza, radice quadrata e fattoriale.
# By iThinkAle

import sys
import operazioni


def main():

    print("Benvenuto nella calcolatrice! By iThinkAle. Per prima cosa, che operazione vuoi svolgere? Scegli tra: \n"
          "Addizione: digita 1; \n"
          "Sottrazione: digita 2; \n"
          "Moltiplicazione: digita 3; \n"
          "Divisione: digita 4; \n"
          "Potenza: digita 5; \n"
          "Radice quadrata: digita 6; \n"
          "Fattoriale (solo numeri interi): digita 7; \n"
          "Per chiudere la calcolatrice: digita ESC \n")

    selectOperation = input("Scegli l'operazione: ")

    if selectOperation == "1":
        operazioni.addizione()

    elif selectOperation == "2":
        operazioni.sottrazione()

    elif selectOperation == "3":
        operazioni.moltiplicazione()

    elif selectOperation == "4":
        operazioni.divisione()

    elif selectOperation == "5":
        operazioni.potenza()

    elif selectOperation == "6":
        operazioni.radicequadrata()

    elif selectOperation == "7":
        operazioni.fattoriale()

    elif selectOperation == "ESC" or selectOperation == "esc":
        print("La calcolatrice si chiuderà ora!")
        input()
        sys.exit()
    else:
        print("Digita una delle opzioni")
        main()

    loop = input("Vuoi continuare ad usare la calcolatrice? S/N ")

    if loop == "S" or loop == "s":
        print("Sto tornando al menù principale!"
              " ")
        input()
        main()
    elif loop == "N" or "n":
        print("La calcolatrice verrà chiusa ora!")
        input()
        sys.exit()
    else:
        print("Errore (digita una delle opzioni)")
        sys.exit()


if __name__ == "__main__":
    main()
