n = int(input('Введите n '))
A  = [True]*n
A[0]=A[1]=False

for k in range(2, n):
    if A[k]:
        for m in range(2*k, n, k):
            A[m] = False
for l in range(n):
    print (l, '-', 'простое' if A[l] else 'составное')