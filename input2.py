# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:01:53 2023

@author: S.Stycenkov
"""

from tkinter import *
from tkinter import messagebox, scrolledtext  

def display_full_name():
    # messagebox.showinfo("Результат:", a.get() + " " + b.get())  -- изначальный вариант
    # messagebox.showinfo("Результат:", 'М = ' + str(int(a.get()) * int(b.get()))) -- промежуточный
    # txt.configure(state ='normal')
    # txt.insert(INSERT, 'Результат200:')
    txt.configure(state ='normal')
    txt.insert(INSERT, 'Результат:\nМ = ' + str(int(a.get()) * int(b.get())))

def hello_boss():
    pass 

def sys_time():
    pass 

def sber_price():
    pass 
    
root = Tk()
# root.geometry('430x250')
# root.place(x = 80, y = 42) 
# root.geometry(f"+{(root.winfo_screenwidth())//2}+{(root.winfo_screenheight())//2}")
wm = int(0.5*root.winfo_screenwidth())-210
wh = int(0.5*root.winfo_screenheight())-225
print(root.geometry('430x550+{}+{}'.format(wm,wh)))
# print(root.winfo_screenwidth())
# print(root.winfo_screenheight())

root.title("Графическая панель управления скриптом")


message_button_one = Button(width=26, height=3, text="Приветствие", command=hello_boss, font=("Courier New", 12, 'bold'), bg='#87CEEB', activebackground='#B7E3F9')
message_button_one.place(x = 80, y = 20)

message_button_two = Button(width=26, height=3, text="Системное время", command=sys_time, font=("Courier New", 12, 'bold'), bg='#B0E0E6', activebackground='#B7E3F9')
message_button_two.place(x = 80, y = 105)

message_button_two = Button(width=26, height=3, text="Данные по сбербанку", command=sys_time, font=("Courier New", 12, 'bold'), bg='#98FB98', activebackground='#B7E3F9')
message_button_two.place(x = 80, y = 190)

txt=Text(width=26, height=6, wrap=WORD, font=("Courier New", 12)) # текст, вернуться позже
txt.place(x = 82, y = 285)
txt.configure(state ='disabled')

message_button_tre = Button(width=26, height=3, text="Напоминание", command=sys_time, font=("Courier New", 12, 'bold'), bg='#B0C4DE', activebackground='#B7E3F9')
message_button_tre.place(x = 80, y = 430)

# txt.geometry('200x100')




# message_button.grid(row=5, column=1)

root.mainloop()