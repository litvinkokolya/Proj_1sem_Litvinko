# Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов списка вправо на K
# позиций (при этом A1 перейдет в Ak+1, A2 - в Ak+2, .... An-k - в An, а исходное значение K последних
# элементов будет потерян). Первые K элементов полученного списка положить равными 0.

from random import randint
ListN = []
i = 0
a = input('Введите размер списка: ')
K = input('введите натуральное число меньше размера списка:')

while i < int(a):
    ListN.append(randint(0, 100))
    i += 1
print('Изначальный список: ', ListN)


t = 0
while t < int(K):
    ListN.insert(0, 0)
    t += 1
print(ListN)
