# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:01:53 2023

@author: S.Stycenkov
"""

from tkinter import *
from tkinter import messagebox

def display_full_name():
    # messagebox.showinfo("Результат:", a.get() + " " + b.get())
    messagebox.showinfo("Результат:", 'М = ' + str(int(a.get()) * int(b.get())))
    # a_label.configure(text="текст") 
    
root = Tk()
root.geometry('430x250')
root.title("Ввод данных")
# root.attributes("-alpha", 0.9)
# root.iconbitmap(default="C:\Users\S.Stycenkov\Documents\alfac\favicon.ico")

a_label = Label(text="Переменная А:", font=("Courier New", 13, 'bold'))
a_label.place(x = 80, y = 10) 
a = StringVar()
a_entry = Entry(textvariable=a, font=("Courier New", 13), width=26)
a_entry.place(x = 80, y = 40) 
a_entry.focus()

b_label = Label(text="Переменная В:", font=("Courier New", 13, 'bold'))
b_label.place(x = 80, y = 80) 
b = StringVar()
b_entry = Entry(textvariable=b, font=("Courier New", 13), width=26)
b_entry.place(x = 80, y = 110) 

message_button = Button(text="Расчет", command=display_full_name, font=("Courier New", 12))
message_button.place(x = 180, y = 170)
# message_button.grid(row=5, column=1)

root.mainloop()