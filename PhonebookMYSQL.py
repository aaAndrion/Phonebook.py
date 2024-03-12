import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import *

db = mysql.connector.connect(
    host='',
    user='root',
    password='37lldh2hkooc',
    db='my_contacts'
)
cursor = db.cursor()


class Phone:
    def __init__(self):
        # Main Window
        window.title('Phone Directory')
        window.geometry('500x400')
        window.wm_minsize(100, 100)
        # Close and Save
        self.Quitbtn = ttk.Button(window, text='Quit', command=self.close)
        self.Quitbtn.place(x=415, y=365)

        self.save_btn = ttk.Button(window, text='Save', command=self.save)
        self.save_btn.place(x=330, y=365)

        self.history_button = Button(window, text="History", command=history)
        self.history_button.place(x=400, y=10)

        # Labels ------------------------------------------
        self.name_label = ttk.Label(window, text='Name')
        self.name_label.place(x=10, y=50)

        self.family_label = ttk.Label(window, text='Family Name')
        self.family_label.place(x=10, y=100)

        self.phone_label = ttk.Label(window, text='Phone Number')
        self.phone_label.place(x=10, y=150)

        name = tk.StringVar()
        global name_entry
        name_entry = tk.Entry(window, textvariable=name, width=20)
        name_entry.place(x=100, y=50)

        family = tk.StringVar()
        global family_entry
        family_entry = tk.Entry(window, textvariable=family, width=20)
        family_entry.place(x=100, y=100)

        phone = tk.IntVar()
        global phone_entry
        phone_entry = tk.Entry(window, textvariable=phone, width=20)
        phone_entry.place(x=100, y=150)

    @staticmethod
    def close():
        db.close()
        window.quit()

    @staticmethod
    def save():
        name = name_entry.get()
        family = family_entry.get()
        phone = phone_entry.get()

        cursor.execute("insert into list1 (name, family, phone) values ('{}', '{}', '{}')".
                       format(name, family, phone))
        db.commit()

        tk.Label(window, text='Saved Successfully!', fg='green', font=20).place(x=100, y=350)


def history():
    cursor.execute("SELECT * FROM list1")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)


window = tk.Tk()
obj = Phone()
window.mainloop()
