import os
from programmi import *


x = input("Cosa vuoi aprire? ")

if x in ["prima", "prima apertura"]:
    chrome()
    taskmgr()

elif x in ["explorer", "ex"]:
    explorer()
