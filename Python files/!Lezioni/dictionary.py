# dictionary  = a changeable, unordered collection of unique keys:value pairs

#            key : value
capitali = {"USA":"Washington DC",
            "India":"New Delhi",
            "Cina":"Beijing",
            "Russia":"Mosca"}

capitali.update({"Italia":"Roma"}) # aggiungi
capitali.update({"USA":"N.Y.C."}) # aggiorna
capitali.pop("India") # rimuovi
#capitali.clear() # cancella tutto

print(capitali.get("India"))
print(capitali.keys())
print(capitali.values())
print(capitali.items())

for key,value in capitali.items():
    print(key,value)
