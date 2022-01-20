# 2. Ихз предложенного текстового файла (text18-12.txt) вывести на экран его содержимое,
# количество пробельных смиволов. Сформировать новый файл, в который поместить текст
#  стихотворной форме предварительно вставив после каждой строки строку из символов "*".

t = 0
for i in open('text-18-12.txt', encoding='UTF-8'):
    print(i, end='')
    for j in i:
        if j == ' ':
            t += 1
print('\nКоличество пробелов в тексте: ', t)

f1 = open('text-18-12.txt', encoding='UTF-8-sig')
l = f1.readlines()
f1.close()

f2 = open('editText-18-12.txt', 'w')
lenList = int(len(l))
i = 0

#Вывод строки из символов "*".
while i <= lenList - 1:
    f2.writelines(l[i])

    if i == lenList - 1:
        f2.writelines('\n{}\n'.format('*' * len(l[i])))
    else:
        f2.writelines('{}\n'.format('*' * len(l[i])))
    i += 1
f2.close()
