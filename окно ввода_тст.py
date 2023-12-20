# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:01:53 2023

@author: S.Stycenkov
"""

from tkinter import *
from tkinter import messagebox

def display_full_name():
    messagebox.showinfo("Результат:", a.get() + " " + b.get())

root = Tk()
root.geometry('430x150')
root.title("Ввод данных")

a_label = Label(text="Переменная А:")
a_label.place(x = 80, y = 21) 
# a_label.grid(row=1, column=0, sticky="w")
a = StringVar()
a_entry = Entry(textvariable=a)
a_entry.place(x = 180, y = 21) 
# a_entry.grid(row=1, column=1)

b_label = Label(text="Переменная В:")
# b_label.grid(row=2, column=0, sticky="w")
b_label.place(x = 80, y = 51) 
b = StringVar()
b_entry = Entry(textvariable=b)
# b_entry.grid(row=2, column=1)
b_entry.place(x = 180, y = 51) 

message_button = Button(text="Click Me", command=display_full_name)
message_button.place(x = 200, y = 81)
# message_button.grid(row=5, column=1)

root.mainloop()