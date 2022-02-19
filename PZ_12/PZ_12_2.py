# Разработать программу с применением пакета tk, взяв в качестве условия задачу из ПЗ 3-8.
# Я взял ПЗ #4.1:
# Дано целое число N (>0). Найти значение выражения 1.1 - 1.2 +1.3 - ...
# (N слагаемых, знаки чередуются). Условный оператор не использовать.
import tkinter as tk

def func():
    N = int(entry_1.get())
    while type(N) != int:
        try:
            N = int(N)
        except ValueError:
            print("Введите число!")
            N = input("Введите число")
    S = 0.0
    i = 1
    while N >= 1:
        x = (1 + i * 0.1) * (-1) ** (i + 1)
        S += x
        N -= 1
        i += 1
    label.config(text="Сумма: {}".format(S))

root = tk.Tk()
entry_1 = tk.Entry(root)
entry_1.pack()
label = tk.Label(root, text="Числа:")
label.pack()
button = tk.Button(root, text='Получить числа', command=func)
button.pack()
root.mainloop()
