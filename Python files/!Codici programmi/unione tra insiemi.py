import sys


def inizio():
    print("UNIONE DI LISTE")
    print("Inserisci gli elementi delle due o più liste separandoli da uno spazio")
    print("Premi INVIO per continuare...")
    input()

    a = input("Per prima cosa, digita quante liste vuoi unire (Max. 5) (Digita ESC per uscire dal programma): ")

    if a == "2":
        dueliste()

    elif a == "3":
        treliste()

    elif a == "4":
        quattroliste()

    elif a == "5":
        cinqueliste()

    elif a == "ESC":
        print("Premi INVIO per uscire dal programma...")
        input()
        sys.exit()

    else:
        print("ERRORE")
        sys.exit()


def dueliste():
    inputarray1 = input("Prima lista: ")
    inputarray2 = input("Seconda lista: ")

    array1 = inputarray1.split()
    array2 = inputarray2.split()

    unique = list(set(array1 + array2))
    print(unique)


def treliste():
    inputarray1 = input("Prima lista: ")
    inputarray2 = input("Seconda lista: ")
    inputarray3 = input("Terza lista: ")

    array1 = inputarray1.split()
    array2 = inputarray2.split()
    array3 = inputarray3.split()

    unique = list(set(array1 + array2 + array3))
    print(unique)

def quattroliste():
    inputarray1 = input("Prima lista: ")
    inputarray2 = input("Seconda lista: ")
    inputarray3 = input("Terza lista: ")
    inputarray4 = input("Quarta lista: ")

    array1 = inputarray1.split()
    array2 = inputarray2.split()
    array3 = inputarray3.split()
    array4 = inputarray4.split()

    unique = list(set(array1 + array2 + array3 + array4))
    print(unique)

def cinqueliste():
    inputarray1 = input("Prima lista: ")
    inputarray2 = input("Seconda lista: ")
    inputarray3 = input("Terza lista: ")
    inputarray4 = input("Quarta lista: ")
    inputarray5 = input("Quinta lista: ")

    array1 = inputarray1.split()
    array2 = inputarray2.split()
    array3 = inputarray3.split()
    array4 = inputarray4.split()
    array5 = inputarray5.split()

    unique = list(set(array1 + array2 + array3 + array4 + array5))
    print(unique)

inizio()
