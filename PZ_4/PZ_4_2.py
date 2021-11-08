# Дано целое число N (>1). Вывести наибольшее из целых чисел К,
# для которых сумма 1 + 2 + ... + К будет меньше или равна N, и саму эту сумму.
N = input("Введите целое число: ")
try:
    N = int(N)
    print("Удачно.")
except ValueError:
    print("Ошибка.")
K = 1
S = 1
while S <= N:
    K += 1
    S += K
    print("K = {0}, S = {1} ".format(K, S))
S -= K
K -= 1
print("K = {0}, S = {1}".format(K, S))
