# Questo programma genera una password casuale rispettando diversi parametri che l'utente inserisce.
# By iThinkAle

import sys
import random
import string

letterList = list(string.ascii_letters+string.digits+string.ascii_lowercase +
                  string.ascii_uppercase+"[]+*ç@#()%&$£/=?'^-_")

print("Hello and welcome to the random password generator! By iThinkAle.")


def main():
    global passwordCharacters
    try:
        passwordCharacters = int(input("Please digit the number of characters you want your password to be: "))
    except ValueError:
        print("Please digit an integer number")
        main()
    else:
        passwordGen()


def passwordGen():

    random.shuffle(letterList)

    password = []

    for i in range(int(passwordCharacters)):
        password.append(random.choice(letterList))

    random.shuffle(password)

    print("".join(password))

    print("Remember to save your password!")

    anotherPass()


def anotherPass():
    anotherOne = input("Do you want to generate another password? Y/N ")

    if anotherOne == "Y" or anotherOne == "y":
        print("Ok! Press Enter to continue.")
        input()
        main()

    elif anotherOne == "N" or anotherOne == "n":
        print("Thank you for using this generator. Bye!")
        sys.exit()
    else:
        print("Please digit one of the options")
        anotherPass()


if __name__ == "__main__":
    main()
