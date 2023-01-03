n = input("Numeratore: ")
d = input("Denominatore: ")

try:
    ans = int(n)/int(d)
except ZeroDivisionError:
    print("Non si può dividere per zero!")
except ValueError:
    print("Inserire un numero!")
else:
    print(ans)
