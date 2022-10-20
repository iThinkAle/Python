#slicing: create a substring by extracting elements from another string
#         indexing[] or slice()
#         [start:stop:step]

name = "Alessandro Ricordy"

first_name = name[:3]
last_name = name[4:7]
funky_name = name[::5]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website1 = "http://google.com/"
website2 = "http://wikipedia.com/"

slice = slice(7,-5)


print(website1[slice])
print(website2[slice])
