n = 32 #int(input('Введите n ')) + 1
A = [True] * n
A[0] = A[1] = False

for k in range(2, n):
    if A[k]:
        for m in range(2 * k, n, k):
            A[m] = False
M =[]
for l in range(n):
    if A[l]:
        yield l

# def simple():
#     a = 0
#     while True:
#         a += 1
#         yield a
#
# gen = simple()
# #print(gen)
# for i in gen:
#     print(i, end = ' ')