import re
import badletters
import os

words = open("dictionary.txt", "r")
words2 = words
longestWord = ""
badLetters = re.match(badletters.badLetters)

print("Array lenght:", len(words))
