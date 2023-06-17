import re


dictionary_path = "E:\!PERSONALE\Programming\Python\Python files\!Codici programmi\longest word on 7 segment display\dictionary.txt"

with open(dictionary_path, "r", encoding="utf8") as file:
    dictionary = file.read()
    words = re.split(r"\s+", dictionary)

longestWord = ""
badLetters = re.compile(r"[gkmqvwxy]", re.IGNORECASE)

for testWord in words:
    if len(testWord) <= len(longestWord):
        continue

    test2 = re.search(str(badLetters), testWord)
    if test2 is True:
        continue

    longestWord = testWord

print(longestWord)
