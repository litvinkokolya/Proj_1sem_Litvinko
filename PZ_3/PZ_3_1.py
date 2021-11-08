# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Каждое из чисел A,
# B, C положительное».
# Проверки на ввод пользователем целых чисел
A = (input("Введите целое число A: "))
try:
    A = int(A)
    print("Удачно!")

except ValueError:
    print("Что то пошло не так...")

B = (input("Введите целое число B: "))
try:
    B = int(B)
    print("Удачно!")

except ValueError:
    print("Что то пошло не так...")

C = (input("Введите целое число C: "))
try:
    C = int(C)
    print("Удачно!")

except ValueError:
    print("Что то пошло не так...")

print("A = ", A)
print("B = ", B)
print("C = ", C)

# Новые переменные типа bool
a = A > 0
b = B > 0
c = C > 0

x = (a and b and c)
print("A положительно: ", a)
print("B положительно: ", b)
print("C положительно: ", c)
print("Каждое из чисел положительное: ", x)
