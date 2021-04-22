# print('abc' in 'abcde')
# print('abce' in 'adcba')

# print('cabcd'.find('abc')) #индекс первого вхождения или -1 если не не входит
# print('cabcd'.find('aec'))
#print(str.find.__doc__)

# print('cabcd'.index('abc')) #индекс первого вхождения или ValueError: substring not found
# print('cabcd'.index('aec'))
#s = "The man in back fleg across the desert, and gunslinger followed"
#print(s.startswith("The man in back"))
#print(s.startswith.__doc__) # S.startswith(prefix[, start[, end]]) -> bool
#print(s.startswith(("The man in back", "The dog", "The woman"))) # prefix can also be a tuple of strings to try

# s = "image.png"
# print(s.endswith(".png"))

# s = "abracadabra"
# print(s.count("abra")) #непересечающиеся аналоги ищет
# print(s.find("abr"))
# print(s.rfind("abr"))

# s = "The man in back fleg across the desert, and gunslinger followed"
# print(s.lower())
# print(s.upper())
# print(s.count("the"))
# print(s.lower().count("the"))

#s = "1, 2, 3, 4"
# print(s)
#print(s.replace(",", ", "))
#print(repr(s.rstrip()))

# print(s.split(", ")) # ['1', '2', '3', '4']
# print(s.split(", ", 2)) #['1', '2', '3, 4']

#s = "1, 2, 3\n, 4     "
#print(s.split()) #['1,', '2,', '3', ',', '4']

# s = "_*__1, 2, 3, 4__*_"
# print(repr(s.rstrip("*_"))) #'_*__1, 2, 3, 4'
# print(repr(s.lstrip("*_"))) # '1, 2, 3, 4__*_'
# print(repr(s.strip("*_"))) # '1, 2, 3, 4'

# numbers = map(str, [1, 2, 3, 4, 5])
# print(repr(" ".join(numbers)))

# capital = 'London is the capital of Great Britain'
# template = '{} is the capital of {}'
# print(template.format("London", "Great Britain"))
# print(template.format("Vaduz", "Liechtenstein"))
# print(template.format.__doc__)


# template = '{capital} is the capital of {country}'
# print(template.format(capital="London", country="Great Britain"))
# print(template.format(country="Liechtenstein", capital="Vaduz"))

#
# import requests
# template = "Response from {0.url} with code {0.status_code}"
#
# res = requests.get("https://docs.python.org/3.5/") #Response from https://docs.python.org/3.5/ with code 200
# print(template.format(res))
#
# res = requests.get("https://docs.python.org/3.5/random") #Response from https://docs.python.org/3.5/random with code 404
# print(template.format(res))

# from random import random
# x = random()
# print(x) # 0.842719576081823
# print("{:.3}".format(x)) # 0.843

import os.path
print(os.getcwd())

