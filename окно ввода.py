# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:01:53 2023

@author: S.Stycenkov
"""

from tkinter import *
from tkinter import messagebox

def display_full_name():
    messagebox.showinfo("GUI Python", name.get() + " " + surname.get())

root = Tk()
root.title("GUI на Python")

name_label = Label(text="Введите имя:")
name_label.grid(row=0, column=0, sticky="w")
name = StringVar()
name_entry = Entry(textvariable=name)
name_entry.grid(row=0, column=1)

surname_label = Label(text="Введите фамилию:")
surname_label.grid(row=1, column=0, sticky="w")
surname = StringVar()
surname_entry = Entry(textvariable=surname)
surname_entry.grid(row=1, column=1)

message_button = Button(text="Click Me", command=display_full_name)
message_button.grid(row=2, column=1)

root.mainloop()