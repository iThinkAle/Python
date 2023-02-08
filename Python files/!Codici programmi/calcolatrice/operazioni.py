# Questo programma è usato per calcolatrice.py
# By iThinkAle

import math


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
