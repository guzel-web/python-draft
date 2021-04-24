# print("abc" in "abcba")
# print("abce" in "abcba")

# print("cabcd".find("abc", 1))  # индекс первого вхождения или -1
# print("cabcd"[1:].find("abc"))
#print(str.find.__doc__)

# print("cabcd".index("abc"))  # индекс первого вхождения или ValueError
# print("cabcd".index("aec"))

# s = "The whale in black fled across the desert, and the gunslinger followed"
# print(s.startswith(("The woman", "The dog", "The man in black")))
# print(s.startswith.__doc__)

# s = "image.png"
# print(s.endswith(".png"))

# s = "abacaba"
# print(s.count("aba"))
# print(s.count.__doc__)
# print(s.find("aba"))
# print(s.rfind("aba"))

# s = "The man in black fled across the desert, and the gunslinger followed"
# print(s.lower())
# print(s.upper())
# print(s.count("the"))
# print(s.lower().count("the"))

# s = "1,2,3,4"
# print(s)
# print(s.replace(",", ", ", 2))
# print(s.replace.__doc__)

# s = "1\t\t 2  3       4       "
# print(s.split())
# print(s.split.__doc__)

# s = "_*__1, 2, 3, 4__*_"
# print(repr(s.rstrip("*_")))
# print(repr(s.lstrip("*_")))
# print(repr(s.strip("*_")))

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
# res = requests.get("https://docs.python.org/3.5/")
# print(template.format(res))
#
# res = requests.get("https://docs.python.org/3.5/random")
# print(template.format(res))
#********************************

# users = [
#     {'first_name': 'Nikita', 'last_name': 'Ivanov', 'city': 'Moscow', 'age': 19},
#     {'first_name': 'Boris', 'last_name': 'Ivanov', 'city': 'Minsk', 'age': 19},
#     {'first_name': 'Mihail', 'last_name': 'Avdeev', 'city': 'London', 'age': 20}
# ]
#
# for user in users:
#     print('Hello {0[first_name]} {0[last_name]} from {0[city]}!'.format(user))
#
# from random import random
# x = random()
# print(x)
# print("{:.3}".format(x))
#
# print('Hello {0[first_name]} {0[last_name]} from {0[city]}!'.format(user))
#********************************

# # После двоеточия в f-строках можно указывать те же значения,
# # что и при использовании format:
# oct1, oct2, oct3, oct4 = [10, 1, 1, 1]
# print(f'''
# IP address:
# {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
# {oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}''')
# # IP address:
# # 10       1        1        1
# # 00001010 00000001 00000001 00000001

# ====================

# # Ширина столбцов может быть указана через переменную:
# topology = [['sw1', 'Gi0/1', 'r1', 'Gi0/2'],
#             ['sw1', 'Gi0/2', 'r2', 'Gi0/1'],
#             ['sw1', 'Gi0/3', 'r3', 'Gi0/0'],
#             ['sw1', 'Gi0/5', 'sw4', 'Gi0/2']]
# width = 10
# for connection in topology:
#     l_device, l_port, r_device, r_port = connection
#     print(f'{l_device:{width}} '
#           f'{l_port:{width}} '
#           f'{r_device:{width}} '
#           f'{r_port:{width}}')
# # sw1        Gi0/1      r1         Gi0/2
# # sw1        Gi0/2      r2         Gi0/1
# # sw1        Gi0/3      r3         Gi0/0
# # sw1        Gi0/5      sw4        Gi0/2

# ====================

# # Конвертация чисел в двоичный формат:
# ip = '10.1.1.1'
# oct1, oct2, oct3, oct4 = ip.split('.')
# print(f'{int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}')
# # 00001010 00000001 00000001 00000001

# ====================

# # Пример функции шаблона f-строки:
# def show_me_ip(i_p, mask):
#     return f'IP: {i_p}, mask: {mask}'
#
# print(show_me_ip('10.1.1.1', 24))
# # IP: 10.1.1.1, mask: 24