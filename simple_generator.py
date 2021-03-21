def simple_gen():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    return 'No more elements' #Показывается при выбросе ошибки StopIteration: No more elements
    yield  2 # при присутствии return, недостижимая операция
    print('Checkpoint 3')

gen = simple_gen()
x = next(gen)
print(x)
y = next(gen)
print(y)
z = next(gen)
print(z)