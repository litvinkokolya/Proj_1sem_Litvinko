# Составить функцию, которая выполнит суммирования числового ряда.
def proverka(a): #Функция обработки исключения.
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            print(f"{a} не может быть числом! Напишите заново.")
            a = input("Введите число: ")
    return a


def summa(): #Функция с призывом функции обработки исключения и расчёта.
    stopWord = "123"
    sum = 0
    while stopWord != "0":
        num = input("Введите число: ")
        num = proverka(num)
        sum += num
        stopWord = input("Если не хотите больше суммировать числа введите (0), иначе нажмите (Enter)")
    return sum
print(f"Сумма числового ряда равна {summa()}")