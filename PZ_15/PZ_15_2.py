# В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива.
from random import randint


J = int(input("Введите сколько будет столбцов у матрицы: "))
I = int(input("Введите сколько будет строчек у матрицы: "))

matrix = [[randint(-2, 2) for j in range(J)] for i in range(I)]

matrix_length = len(matrix)

print("Изначальная матрица:")
for i in range(matrix_length):
    print(matrix[i])

massiv_new = []

print("Отрицательные числа из матрицы:")
for i in matrix:
    for index,value in enumerate(i):
        if value < 0:
            print(value)
            massiv_new.append(value)
print("Новый массив: ", massiv_new)
print("Размер нового массива: ", len(massiv_new))