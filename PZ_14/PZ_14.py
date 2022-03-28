# В исходном текстовом файле (dates.txt) найти все даты в формате ДД.ММ.ГГГГ и ДД/ММ/ГГГГ.
# Посчитать количество дат в каждом формате. Поместить в новый текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.
import re

withslash = re.compile(r'\n(\d{2}/02/\d{4})')
withtochka = re.compile(r'\n(\d{2}\.02\.\d{4})')


with open('dates.txt', 'r') as dates_open:
    f = dates_open.read()
    dateswithslash = withslash.findall(f)
    dateswithtochka = withtochka.findall(f)
    dottoslash = re.sub(r"[\.\,]", '/', f)
    print('ДД/ММ/ГГГГ:', len(dateswithslash))
    print('ДД.ММ.ГГГГ:', len(dateswithtochka))



file = open('new_dates', 'w', encoding='utf-8')
file.write(str(dottoslash))