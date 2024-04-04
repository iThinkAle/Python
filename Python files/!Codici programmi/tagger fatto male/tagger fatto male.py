# This is a script that, given a file with urls, opens one of them, specified by the user, reads the content and puts
# it into a text file created in the same folder as this script. Not finished yet.
# By iThinkAle

import requests
import sys
from tkinter import *
from tkinter import filedialog
from urllib import request
import urllib
from bs4 import BeautifulSoup


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
    global text
    text = data.getText()


def handleText():
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    global textdef
    textdef = '\n'.join(chunk for chunk in chunks if chunk)
    createTextFile()


def createTextFile():
    urltextfile = open("urlcontent.txt", "x")
    urltextfile.write(textdef)
    sys.exit()


def internetconnection():
    try:
        requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False


if internetconnection():
    openFile()
else:
    sys.exit()


window = Tk()

button = Button(text="Open", command=openFile)
button.pack()
internetconnection()

window.mainloop()
