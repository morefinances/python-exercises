# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:01:53 2023

@author: S.Stycenkov
"""

from tkinter import *
from tkinter import messagebox, scrolledtext  
import csv
from PIL import Image, ImageTk

def display_full_name():
    # messagebox.showinfo("Результат:", a.get() + " " + b.get())  -- изначальный вариант
    # messagebox.showinfo("Результат:", 'М = ' + str(int(a.get()) * int(b.get()))) -- промежуточный
    # txt.configure(state ='normal')
    # txt.insert(INSERT, 'Результат200:')
    txt.configure(state ='normal')
    txt.insert(INSERT, 'Результат:\nМ = ' + str(int(a.get()) * int(b.get())))

def hello_boss():
    with open('C:\\files\command.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows('A')

def sys_time():
    with open('C:\\files\command.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows('B')

def sber_price():
    with open('C:\\files\command.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows('C')
        
    messagebox.showinfo('Выгрузка данных из торгового терминала!', "Будут выгружены\nтекущие котировки\nиз терминала Quik\nпо инструменту SBER\n")
        
    txt.delete(1.0, 'end')
    txt.configure(state ='normal')
    txt.insert(1.0, "Данные текущей торговой сессии:\n\n")
    uno = 0
        
    with open('C:\\files\SBER.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(*row)
            txt.insert(END, pricetitle[uno])
            txt.insert(END, float(*row))
            txt.insert(END, "\n")
            uno += 1
            
                
def remember_it():
    with open('C:\\files\command.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows('D')        
    img = PhotoImage(file='C:/files/picture_small.png')
    label = Label(root, image=img).pack()
    label.pack()

    
root = Tk()
# root.geometry('430x250')
# root.place(x = 80, y = 42) 
# root.geometry(f"+{(root.winfo_screenwidth())//2}+{(root.winfo_screenheight())//2}")
wm = int(0.5*root.winfo_screenwidth())-210
wh = int(0.5*root.winfo_screenheight())-230
print(root.geometry('445x555+{}+{}'.format(wm,wh)))
# print(root.winfo_screenwidth())
# print(root.winfo_screenheight())

root.title("Графическая панель управления скриптом")

pricetitle = ['Ближайший BID = ','Ближайший OFFER = ','Цена открытия OPEN = ','Максимальная цена HIGH = ','Минимальная цена LOW = ','Цена последней сделки LAST = ']


message_button_one = Button(width=28, height=3, text="Приветствие", command=hello_boss, font=("Courier New", 12, 'bold'), bg='#87CEEB', activebackground='#B7E3F9', highlightcolor="white")
message_button_one.place(x = 80, y = 20)

message_button_two = Button(width=28, height=3, text="Системное время", command=sys_time, font=("Courier New", 12, 'bold'), bg='#B0E0E6', activebackground='#B7E3F9')
message_button_two.place(x = 80, y = 105)

message_button_two = Button(width=28, height=3, text="Данные по сбербанку", command=sber_price, font=("Courier New", 12, 'bold'), bg='#98FB98', activebackground='#B7E3F9')
message_button_two.place(x = 80, y = 190)

txt=Text(width=36, height=8, wrap=WORD, font=("Courier New", 10)) # текст, вернуться позже
txt.place(x = 80, y = 285)
# txt.configure(state ='disabled')

message_button_tre = Button(width=28, height=3, text="Напоминание", command=remember_it, font=("Courier New", 12, 'bold'), bg='#B0C4DE', activebackground='#B7E3F9')
message_button_tre.place(x = 80, y = 440)

# txt.geometry('200x100')




# message_button.grid(row=5, column=1)

root.mainloop()