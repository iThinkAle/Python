a = True
b = True
c = True
d = False
e = False

print(((a or b) and c) ^ d)

print((a or d) or (c and b) and (d or e)) and c

print((((d or e) ^ (not c and not d) or (c and not a)) ^ d) ^ d)
