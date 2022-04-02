# В матрице найти сумму и произведение элементов столбца N (N задать с клавиатуры).
from random import randint


J = int(input("Введите сколько будет столбцов у матрицы: "))
I = int(input("Введите сколько будет строчек у матрицы: "))

matrix = [[randint(-2, 2) for j in range(J)] for i in range(I)]

matrix_length = len(matrix)

print("Изначальная матрица:")
for i in range(matrix_length):
    print(matrix[i])


N = int(input("Введите с каким столбцом будем работать (от 1 до {}): ".format(matrix_length)))

M = N-1
result_proiz = 1
result_sum = 0

print("Значения из {} столбца:".format(N))
for i in matrix:
    for index,value in enumerate(i):
        if index == M:
            result_proiz *= value
            result_sum += value
            print(value)
print("Сумма:", result_sum)
print("Произведение:", result_proiz)