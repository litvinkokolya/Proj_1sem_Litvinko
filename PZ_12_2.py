# Разработать программу с применением пакета tk, взяв в качестве условия задачу из ПЗ 2-8.
# Я взял ПЗ #2.
import tkinter as tk
import math

def func():
    try:
        S = float(entry_1.get())
        if 9 < S < 100:
            Res1 = (S // 10) + math.fmod(S, 10)
            Res2 = (S // 10) * math.fmod(S, 10)
        label.config(text="Сумма и произведение его цифр будет равна: {}, {}".format(Res1, Res2))
    except ValueError:
        label.config(text="Ошибка, введите цифры")


root = tk.Tk()
entry_1 = tk.Entry(root)
entry_1.pack()
label = tk.Label(root, text="Числа:")
label.pack()
button = tk.Button(root, text='Получить числа', command=func)
button.pack()
root.mainloop()