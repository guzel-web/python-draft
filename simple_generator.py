# def simple_gen():
#     print('Checkpoint 1')
#     yield 1
#     print('Checkpoint 2')
#     return 'No more elements' #Показывается при выбросе ошибки StopIteration: No more elements
#     yield  2 # при присутствии return, недостижимая операция
#     print('Checkpoint 3')
#
# gen = simple_gen()
# x = next(gen)
# print(x)
# y = next(gen)
# print(y)
# z = next(gen)
# print(z)

def simple():
    a = 0
    while True:
        a += 1
        yield a

gen = simple()
#print(gen)
for i in gen:
    print(i, end = ' ')

# def random_generator(k): # делает то же самое, что RandomIterator
#     # yield генератор вместо функции return,
#     # может вернуть значении из функции несколько раз
#     for i in range(k):
#         yield random()
# gen = random_generator(3)
# for i  in gen:
#     print(i)