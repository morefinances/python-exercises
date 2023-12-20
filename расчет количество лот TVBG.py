# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:01:53 2023

@author: S.Stycenkov
"""

from tkinter import *
from tkinter import messagebox
import pandas as pd

def onlynum(text):
    a = "0123456789.,"
    txt = ""
    for i in text:
        if i in a:
            if i == "." or i == ",":
                txt = txt + "."
            else:
                txt += i
    return txt

def display_full_name():
    first_sum = float(onlynum(a.get()))
    price = float(onlynum(b.get()))
    result_sum = first_sum *0.98
    text1 = 'Начальная сумма: '
    text2 = 'Скорректированная сумма: '
    text3 = 'Текущая котировка (bid): '
    text4 = 'Количество лот для покупки: '
    text5 = 'Количество лот с учетом округления: '
    # print(text1, first_sum)
    # print(text2, result_sum)
    # print(text3, price)
    qual_lot = result_sum / price
    # print(text4, qual_lot)
    # print(text5, int(qual_lot))
    
    result_series = pd.DataFrame({'[расчет]': [first_sum, result_sum, price, qual_lot, int(qual_lot)]},
                              index = [text1, text2, text3, text4, text5])
    print("--"*23)
    pd.options.display.float_format ='{:,.2f}'.format
    print(result_series)
    print("--"*23)
    text_for_message = 'Начальная сумма: ' + str(first_sum) + \
    '\n\nСкорректированная сумма: '+ str(result_sum) + \
    '\n\nКотировка: ' + str(price) + \
    '\n\nКоличество лот для покупки: ' + str(qual_lot) + \
    '\n\nКоличество лот с учетом округления: ' + str(int(qual_lot))
    messagebox.showinfo("Расчет : ", text_for_message)

sizeX = 250
sizeY = 125

root = Tk()
wm = int(0.5*root.winfo_screenwidth())-int(sizeX/2)
wh = int(0.5*root.winfo_screenheight())-int(sizeY/2)
root.geometry('{}x{}+{}+{}'.format(sizeX, sizeY, wm, wh)) #'430x150'
root.title("Лоты по GOLD")

# a_label = Label(text="Cумма:", font=("Courier New", 15, 'bold'))
# a_label.place(x = 15, y = 10) 
# a_label.grid(row=1, column=0, sticky="w")
a = StringVar()
a_entry = Entry(textvariable=a, font=("Courier New", 15, 'bold'), width=9, 
                justify=RIGHT)
a_entry.place(x = 25, y = 30) 
# a_entry.grid(row=1, column=1)

# b_label = Label(text="Переменная В:")
# b_label.grid(row=2, column=0, sticky="w")
# b_label.place(x = 25, y = 51) 
b = StringVar()
b_entry = Entry(textvariable=b, font=("Courier New", 15, 'bold'), width=9, 
                justify=RIGHT)
# b_entry.grid(row=2, column=1)
b_entry.place(x = 25, y = 65) 

message_button = Button(text="Расчет", font=("Courier New", 9, 'bold'),
                        width=8, height=3, bg='#FFFFFF', command=display_full_name)
message_button.place(x = 160, y = 29)
# message_button.grid(row=5, column=1)

root.mainloop()