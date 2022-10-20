# for loop: a statement that will execute its block of code for a limited amount of time
#           while loop = unlimited
#           for loop = limited

import time

for i in range(10):
    print(i+1)

for i in range(50,100,2):
    print(i)

for i in "Ale Ric":
    print(i)

for seconds in range(100,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new year")

