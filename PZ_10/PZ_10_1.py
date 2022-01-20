# 1. Средствами языка Python формировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов:
# Исходные данные, Количество элементов, Максимальный элемент, Среднее арифметическое первой трети.

l = ['-99 6 12 -36 20 45 100 -15 72']
f1 = open('data_1.txt', 'w')
f1.writelines(l)
f1.close()


f2 = open('data_2.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(l)
f2.close()


f1 = open('data_1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()


f1 = open('data_1.txt')
max, t = 0, 0
for i in range(len(k)):
    max = max > k[i] and max or k[i]


p = []
f2 = open('data_2.txt', 'a')
p.append(k[0:3])
p = (k[0] + k[1] + k[2]) / 3


f2 = open('data_2.txt', 'a')
f2.write('\n')
print("Количество элементов: ", len(k), "Среднее арифметическое: ", p, "Максимальный элемент: ", max, file=f2, )
f2.close()
