# 2D list = a list of lists

colazione = ["biscotti", "latte", "cereali"]  # 0
pranzo = ["pasta alla carbonara", "patate al forno", "acqua"]  # 1
cena = ["hamburger", "patatine fritte", "acqua"]  # 2

cibo = [colazione, pranzo, cena]

print(cibo)
print(cibo[1])
print(cibo[2][0])

for x in cibo:
    print(x)
