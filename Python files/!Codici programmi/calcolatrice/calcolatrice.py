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

    x = input("Scegli l'operazione: ")

    if x == "1":
        operazioni.addizione()

    elif x == "2":
        operazioni.sottrazione()

    elif x == "3":
        operazioni.moltiplicazione()

    elif x == "4":
        operazioni.divisione()

    elif x == "5":
        operazioni.potenza()

    elif x == "6":
        operazioni.radicequadrata()

    elif x == "7":
        operazioni.fattoriale()

    elif x == "ESC" or x == "esc":
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
