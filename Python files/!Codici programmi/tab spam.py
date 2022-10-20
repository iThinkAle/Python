import subprocess
import sys


def main():
    rinomina = input("Do you want to rename a file? ")

    if rinomina == "yes":
        print("Gotcha")
        while 1 == 1:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

    elif rinomina == "no":
        print("Ok! See you soon!")
        sys.exit()

    else:
        print("Invalid input! Please re-open the program.")


main()
