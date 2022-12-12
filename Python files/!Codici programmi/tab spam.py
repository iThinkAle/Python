import subprocess
import sys


def main():
    rinomina = input("Do you want to rename a file? (yes, no) ")

    if rinomina == "yes":
        print("Gotcha")
        while True:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

    elif rinomina == "no":
        print("Ok! See you soon!")
        sys.exit()

    else:
        print("Invalid input! Please re-open the program.")


main()
