import os
from dir import *


x = input("Cosa vuoi aprire? ")

if x in ["prima", "prima apertura"]:
    chrome()
    taskmgr()

elif x in ["explorer", "ex"]:
    explorer()
