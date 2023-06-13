import re


dictionary = open("dictionary.txt")
longestWord = ""
badLetters = [r"g", r"k", r"m", r"q", r"v", r"w", r"x", r"z"]


for testWord in dictionary:
    if len(testWord) <= len(longestWord):
        continue

    test2 = re.search(str(badLetters), testWord)
    if test2 is True:
        continue

    longestWord = testWord

dictionary.close()

print(longestWord)
