import webbrowser

import requests
import sys
from tkinter import *
from tkinter import filedialog
from urllib import request
import urllib
from bs4 import BeautifulSoup


def internetconnection():
    try:
        requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False


if internetconnection():
    pass
else:
    sys.exit()


def openFile():
    filetypes = [("TXT files", "*.txt"), ("All", "*.*")]
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    global file
    file = open(filepath, "r")
    readFile()


def readFile():
    data = file.read()
    global splitdata
    splitdata = data.split(",")
    readURL()


def readURL():
    read = urllib.request.urlopen(splitdata[5]).read()
    data = BeautifulSoup(read, features="html.parser")
    for script in data(["script", "style"]):
        script.extract()
    text = data.getText()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    print(text)

window = Tk()
button = Button(text="Open", command=openFile)
button.pack()
openFile()
window.mainloop()
