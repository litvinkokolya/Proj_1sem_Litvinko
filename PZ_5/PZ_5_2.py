# Описать функцию SortDec3(A, B, C), меняющую содержимое переменных A, B, C таким образом, чтобы их значения оказались
# упорядоченными по убыванию (A, B, C - вещественные параметры, являющиеся одновременно входными и выходными).
# С помощью этой функции упорядочить по убыванию два данных набора из трех чисел: (А1, B1, C1) и (A2, B2, C2).

a = int(input("Введите A: "))
b = int(input("Введите B: "))
c = int(input("Введите C: "))

def SortDec3(a, b, c):

    a1 = max(a, max(b, c))
    b1 = min(a, max(b, c))
    c1 = min(a, min(b, c))

    return(a1, b1, c1)


print(SortDec3(a, b, c))
