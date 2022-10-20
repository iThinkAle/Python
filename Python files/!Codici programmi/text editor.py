import tkinter.filedialog
from tkinter import *


window = Tk("Text Editor")

text = Text(window)
text.grid()

window.mainloop()


def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfile()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()


button = Button(
    window,
    text="Save",
    command=saveas
)

button.grid()
