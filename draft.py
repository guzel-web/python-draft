# x = input().split()              # 10 15 28 51 63 12
# xs = (int(i) for i in x)
#
# # def even(x):                      # 1
# #     return x % 2 == 0             # 1
# even = lambda x: x % 2 == 0  # 2    # 2       [10, 28, 12]
#
# # evens = filter(even, xs)          # 1       [10, 28, 12]
# # for i in evens:                   # 1
# #     print(i)                      # 1
# evens = list(filter(even, xs))
# print(evens)
# ***********************************************************
#
# x = [
#     ("Guido", "van", "Rossum"),
#     ("Haskell", "Curry"),
#     ("John", "Baskus")
# ]
#
# # def lenght(name):                                  # 3
# #     return len(" ".join(name))                     # 3
# #                                                    # 3
# # name_lenghts = [lenght(name) for name in x]        # 3
# # print(name_lenghts)                                # 3
# #                                                    # 3
# # x.sort(key=lenght)                                 # 3
# # print(x)                                           # 3
#
#
# x.sort(key=lambda name: len(" ".join(name)))
# print(x)
# ***********************************************************

import operator as op

# print(op.add(4, 5))
# print(op.mul(4,5))
# print(op.contains([1, 2, 3], 4))       # 4 in [1,2,3,]

x =[1, 2, 3]
x = {"123": 3}
f = op.itemgetter("123")      # f(x) = x["123"]
print(f(x))
