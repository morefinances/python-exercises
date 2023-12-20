# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:01:53 2023

@author: S.Stycenkov
"""

from tkinter import *
from tkinter import messagebox
import pandas as pd
import colorama
from colorama import Fore, Style, Back

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

def hr_line():
    print(Fore.BLUE, end = "")
    print("--"*23)
    print(Style.RESET_ALL, end="")

def display_full_name():
    if onlynum(a.get()) == "" or onlynum(b.get()) == "":
        print()
        print('Введены не полные данные, повторите запрос.')
    else:
        print(Fore.BLUE, end = "")
        print("\nРасчет по", broker[int(selected.get()) - 1])
        print(Style.RESET_ALL, end="")
        first_sum = float(onlynum(a.get()))
        price = float(onlynum(b.get()))
        text1 = 'Начальная сумма: '
        text2 = 'Скорректированная сумма: '
        text3 = 'Текущая котировка (bid): '
        text4 = 'Количество лот для покупки: '
        text5 = 'Количество лот с учетом округления: '
        if int(selected.get()) == 1:
            result_sum = first_sum *0.98
            qual_lot = result_sum / price
        else:
            result_sum = first_sum * 0.9989 - 2
            qual_lot = result_sum / price
        result_series = pd.DataFrame({'[' + broker[int(selected.get()) - 1] + ']': [first_sum, result_sum, price, qual_lot, int(qual_lot)]}, index = [text1, text2, text3, text4, text5])
        hr_line()
        pd.options.display.float_format ='{:,.2f}'.format
        print(result_series)
        hr_line()
        text_for_message = 'Брокер: ' +  broker[int(selected.get()) - 1] + \
            '\n\nНачальная сумма: ' + str(first_sum) + \
        '\n\nСкорректированная сумма: '+ str(int(100*result_sum)/100) + \
        '\n\nКотировка: ' + str(price) + \
        '\n\nКоличество лот для покупки: ' + str(int(100*qual_lot)/100) + \
        '\n\nКоличество лот с учетом округления: ' + str(int(qual_lot))
        messagebox.showinfo("Расчет : ", text_for_message)
    
    
sizeX = 250
sizeY = 155

root = Tk()
wm = int(0.5*root.winfo_screenwidth())-int(sizeX/2)
wh = int(0.5*root.winfo_screenheight())-int(sizeY/2)
root.geometry('{}x{}+{}+{}'.format(sizeX, sizeY, wm, wh)) #'430x150'
root.title("Лоты по GOLD")

broker = ['VTB', 'OB']

f_top = LabelFrame(root, text="Брокер",  width=200, height=50)
f_top.pack(padx=5, pady=5)

selected = IntVar() 
rad1 = Radiobutton(f_top, text='VTB', value=1, variable=selected)  
rad2 = Radiobutton(f_top, text='OB', value=2, variable=selected)  
rad1.place(x = 30, y = 0)  
rad2.place(x = 110, y = 0)  
selected.set(1)

a = StringVar()
a_entry = Entry(textvariable=a, font=("Courier New", 15, 'bold'), width=9, 
                justify=RIGHT)
a_entry.place(x = 25, y = 66) 
b = StringVar()
b_entry = Entry(textvariable=b, font=("Courier New", 15, 'bold'), width=9, 
                justify=RIGHT)
b_entry.place(x = 25, y = 110) 

message_button = Button(text="Расчет", font=("Courier New", 9, 'bold'),
                        width=9, height=4, bg='#FFFFFF', command=display_full_name)
message_button.place(x = 150, y = 65)

root.mainloop()