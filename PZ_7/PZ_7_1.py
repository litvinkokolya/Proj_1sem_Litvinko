# Дана непустая строка S и целое число N (>0). Вывести строку, содержащую символы строки S, между которыми
# вставлено по N символов "*" (звездочка).

S = input("Введите фразу: ")
N = int(input("Введите натуральное число: "))

A = "*" * N   #Считает количество звездочек.
print(A)

print(A.join(S))

