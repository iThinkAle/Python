# set = collection which is unordered and unindexed and does not allow any duplicate values.

utensili = {"coltello", "forchetta", "cucchiaio", "mestolo"}
portate = {"piatto", "scodella", "tazza"}
tavolo = utensili.union(portate)

utensili.add("pentola")
utensili.remove("coltello")
utensili.clear()
utensili.update(portate)


print(utensili.difference(portate)) # cosa utensili non ha in comune con portate
print(utensili.intersection(portate)) # cosa utensili ha in comune con portate

print(utensili)
for i in utensili:
    print(i)

print(tavolo)
for i in tavolo:
    print(i)