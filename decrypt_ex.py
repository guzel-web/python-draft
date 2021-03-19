# from simplecrypt import decrypt, DecryptionException
#
# passwords = []
# with open('passwords.txt', 'r') as pw:
#     for line in pw:
#         passwords.append(line.strip())
#
# with open("encrypted.bin", "rb") as inp:
#     encrypted = inp.read()
#
# for password in passwords:
#     try:
#         print(decrypt(password, encrypted).decode('utf8'), password)
#     except DecryptionException:
#         print(password, 'is wrong')
#     else:
#         print(password, 'is correct')

import simplecrypt
from urllib import request

encrypted = request.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read()
passwords = request.urlopen('https://stepic.org/media/attachments/lesson/24466/passwords.txt').read().strip().split()

for password in passwords:
    password = password[:-1]
    try:
        print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
    except simplecrypt.DecryptionException:
        print(password, 'is wrong')
    else:
        print(password, 'is correct')