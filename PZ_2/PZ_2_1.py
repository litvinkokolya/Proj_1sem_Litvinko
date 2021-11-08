# Дано двузначное число.
# Найти сумму и произведение его цирф. Вывести.
# Импортируем math из библиотеки для решения задачи.
import math

# Данный блок написан для вывода "Ошибки" при вводе нецелого числа
# и продолжении выполнения кода при правильном числе.
A = input('Введите целое двузначное число: ')
try:
    A = int(A)
    if A != int:
        A = int(A)
except ValueError:
    print('Ошибка. Попробуйте еще раз ввести целое число.')

if 9 < A < 100:
    Res1 = (A // 10) + math.fmod(A, 10)
    print('Сумма его цифр равна:', int(Res1))
    Res2 = (A // 10) * math.fmod(A, 10)
    print('Произведение его цифр равно:', int(Res2))
else:
    print('Введено неправильное число')
