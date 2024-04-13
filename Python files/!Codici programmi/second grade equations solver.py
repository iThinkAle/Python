# Simple script to solve second grade equations
# By iThinkAle

import math

ainput = float(input("Enter A: "))
binput = float(input("Enter B: "))
cinput = float(input("Enter C: "))

a = ainput
b = binput
c = cinput

try:
    delta = math.sqrt((b**2)-(4*a*c))
except ValueError:
    print("No solution exists")
else:
    pass

x1 = (-b+delta)/(2*a)
x2 = (-b-delta)/(2*a)

print(f"x1 = {x1}, x2 = {x2}")
print(f"delta = {delta}")
