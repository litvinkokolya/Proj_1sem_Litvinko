# Дан список A размера N (N — нечетное число). Вывести его элементы с нечетными
# номерами в порядке  номеров. Условный оператор не использовать.

from random import randint
a = []
n = int(input('Введите размер списка: '))


while n:
    a.append(randint(0, 100))
    n -= 1
print('Изначальный список: ', a)


for i in a[1::2]:
    print(i)

