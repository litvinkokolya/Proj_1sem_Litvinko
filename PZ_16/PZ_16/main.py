import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#c93c20', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="img/add.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить марку', command=self.open_dialog, bg='#ca3a27', bd=0, fg='white',
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.edit_img = tk.PhotoImage(file="img/edit.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#ca3a27',
                                    bd=0, fg='white', compound=tk.TOP, image=self.edit_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="img/delete.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#ca3a27',
                               bd=0, fg='white', compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="img/search.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#ca3a27',
                               bd=0, fg='white', compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="img/update.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#ca3a27',
                                bd=0, fg='white', compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=(
            'number', 'mark', 'zavod', 'cost', 'date', 'document', 'master', 'sum'), height=15,
                                 show='headings')

        self.tree.column('number', width=20, anchor=tk.CENTER)
        self.tree.column('mark', width=100, anchor=tk.CENTER)
        self.tree.column('zavod', width=100, anchor=tk.CENTER)
        self.tree.column('cost', width=100, anchor=tk.CENTER)
        self.tree.column('date', width=120, anchor=tk.CENTER)
        self.tree.column('document', width=100, anchor=tk.CENTER)
        self.tree.column('master', width=100, anchor=tk.CENTER)
        self.tree.column('sum', width=120, anchor=tk.CENTER)

        self.tree.heading('number', text='#')
        self.tree.heading('mark', text='Марка')
        self.tree.heading('zavod', text='Завод')
        self.tree.heading('cost', text='Цена')
        self.tree.heading('date', text='Дата ремонта')
        self.tree.heading('document', text='Документ')
        self.tree.heading('master', text='Мастер')
        self.tree.heading('sum', text='Сумма оплаты')

        self.tree.pack()

    def records(self, number, mark, zavod, cost, date, document, master, sum):
        self.db.insert_data(number, mark, zavod, cost, date, document, master, sum)
        self.view_records()

    def update_record(self, number, mark, zavod, cost, date, document, master, sum):
        self.db.cur.execute(
            """UPDATE users SET number=?, mark=?, zavod=?, cost=?, date=?, document=?, master=?, sum=? WHERE number=?""",
            (number, mark, zavod, cost, date, document, master, sum, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE number=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, mark):
        mark = (mark,)
        self.db.cur.execute("""SELECT * FROM users WHERE mark=?""", mark)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить игрока')
        self.geometry('400x250+400+300')
        self.resizable(False, False)

        label_number = tk.Label(self, text='Номер')
        label_number.place(x=50, y=1)
        self.number = ttk.Entry(self)
        self.number.place(x=170, y=1)

        label_mark = tk.Label(self, text='Марка')
        label_mark.place(x=50, y=25)
        self.mark = ttk.Combobox(self, values=[u'LG', u'Samsung', u'Xiaomi', u'Apple',
                                                u'Redmi', u'Corsair', u'Papia', u'Ikra'])
        self.mark.place(x=170, y=25)

        label_zavod = tk.Label(self, text='Завод')
        label_zavod.place(x=50, y=50)
        self.entry_zavod = ttk.Entry(self)
        self.entry_zavod.place(x=170, y=50)

        label_cost = tk.Label(self, text='Цена')
        label_cost.place(x=50, y=75)
        self.cost = ttk.Entry(self)
        self.cost.place(x=170, y=75)

        label_date = tk.Label(self, text='Дата ремонта')
        label_date.place(x=50, y=100)
        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x=170, y=100)

        label_document = tk.Label(self, text='Документ')
        label_document.place(x=50, y=125)
        self.document = ttk.Combobox(self, values=[u'Паспорт', u'Тех. паспорт', u'СНИЛС', u'Полис'])
        self.document.place(x=170, y=125)

        label_master = tk.Label(self, text='Мастер')
        label_master.place(x=50, y=150)
        self.entry_master = ttk.Entry(self)
        self.entry_master.place(x=170, y=150)

        label_sum = tk.Label(self, text='Сумма оплаты')
        label_sum.place(x=50, y=175)
        self.entry_sum = ttk.Entry(self)
        self.entry_sum.place(x=170, y=175)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=200)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=200)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.number.get(),
                                                                       self.mark.get(),
                                                                       self.entry_zavod.get(),
                                                                       self.cost.get(),
                                                                       self.entry_date.get(),
                                                                       self.document.get(),
                                                                       self.entry_master.get(),
                                                                       self.entry_sum.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=200)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.number.get(),
                                                                          self.mark.get(),
                                                                          self.entry_zavod.get(),
                                                                          self.cost.get(),
                                                                          self.entry_date.get(),
                                                                          self.document.get(),
                                                                          self.entry_master.get(),
                                                                          self.entry_sum.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        self.mark_search = ttk.Combobox(self,
                                        values=[u'LG', u'Samsung', u'Xiaomi', u'Apple',
                                                u'Redmi', u'Corsair', u'Papia', u'Ikra'])
        self.mark_search.place(x=60, y=20, width=200)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=70, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.mark_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('Telemasterskaya.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                number INTEGER PRIMARY KEY AUTOINCREMENT,
                mark TEXT, 
                zavod TEXT NOT NULL,
                cost INTEGER,
                date TEXT,
                document TEXT,
                master TEXT,
                sum INTEGER
                )""")

    def insert_data(self, number, mark, zavod, cost, date, document, master, sum):
        self.cur.execute(
            """INSERT INTO users(number, mark, zavod, cost, date, document, master, sum) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (number, mark, zavod, cost, date, document, master, sum))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Телемастерская")
    root.geometry("1000x450+300+200")
    root.resizable(False, False)
    root.mainloop()
