from random import random

# class RandomIterator:
#     def __iter__(self):
#         return self
#
#     def __init__(self, k):  # конструктор класса
#         self.k = k  # количество перебираемых чисел
#         self.i = 0  # кол-во перечисленных итератором чисел
#
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration

#for x in RandonIterator(10):
#    print(x)

def random_generator(k): # делает то же самое, что RandomIterator
    # yield генератор вместо функции return,
    # может вернуть значении из функции несколько раз
    for i in range(k):
        yield random()
gen = random_generator(3)
print(type(gen))
for i  in gen:
    print(i)
