import tkinter as tk

window = tk.Tk()

a = tk.Label(
    text="Name",
    fg="black",  # foreground color
    bg="white",  # background color
    width=100,
    height=10
)

#button = tk.Button(
#    text="Click",
#    width=100,
#    height=10,
#    bg="black",
#    fg="white"
#)

entry = tk.Entry(
    fg="black",
    bg="white",
    width=50
)

a.pack()
entry.pack()


window.mainloop()
