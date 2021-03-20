from random import random

class RandonIterator:
    def __iter__(self):
        return  self

    def __init__(self, k): # конструктор класса
        self.k = k   # количество перебираемых чисел
        self.i = 0   # кол-во перечисленных итератором чисел

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return  random()
        else:
            raise StopIteration

x = RandonIterator(3)
#print(next(x)) # next(x) - x.__next__() --iteraror
#iter(x)

for x in RandonIterator(10):
    print(x)