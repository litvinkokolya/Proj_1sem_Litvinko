# Дан список размера N. Найти два соседних элемента, сумма которых максимальна и вывести.

from random import randint

N = int(input('Сколько элементов в массиве: '))
arr = []
for i in range(N):
    a = randint(1, 100)
    arr.append(a)
print(arr)
k = 1
max_sum = arr[k] + arr[k + 1]
for i in range(3, N):
    if arr[i - 1] + arr[i] > max_sum:
        max_sum = arr[i - 1] + arr[i]
        k = i - 1

print('arr[{}] + arr[{}] = {} '.format(k + 1, k + 2, max_sum))
