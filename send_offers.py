# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:48:36 2023

@author: S.Stycenkov
"""
import pandas as pd
from tkinter import *  
from tkinter.ttk import Combobox  
from time import sleep

none_str = ['-' * 5, '-' * 3]

def clears_all_tikers():
    for i in range(5):
        combo[i].current(0)
        direction[i].current(2)
        size[i].delete(0, END)


def save_orders():
    global total_id
    A = []
    B = []
    C = []
    D = []
    for u in range(5):
        if combo[u].get() != none_str[0] and direction[u].get() != none_str[1] and size[u].get() != "":
            A.append(total_id)
            B.append(direction[u].get())
            C.append(size[u].get())
            D.append(combo[u].get())
            total_id += 1
    df=pd.DataFrame({
        'id': A,
        'direct': B,
        'size': C,
        'tiker': D
    })    
    print(df)
    df.to_csv("C:/files/offers.csv", sep=" ", index = False, header = False)
    sleep(1/10)
    print('-' * 15)
    
    
total_id = 1
    
# считываем тикеры
file = "C:\\files\\tickers_for_work.csv"
offers = pd.read_csv(file, delimiter=';')

uniq_offers = [none_str[0]]
directions = ['Buy', 'Sell', none_str[1]]

# удаляем дублирование тикеров
for i in range(len(offers.columns)):
    if "." not in offers.columns[i]:
        uniq_offers.append(offers.columns[i])

# создаем панель выставления заявок  
window = Tk()  
window.title("Выставление заявок")  
wm = int(0.5*window.winfo_screenwidth())-int(300)
wh = int(0.5*window.winfo_screenheight())-int(200)
window.geometry('{}x{}+{}+{}'.format(600, 200, wm, wh))


lbl = Label(window, text="Выберите инструмент:")  
lbl.place(x = 19, y = 9)

lbl = Label(window, text="Направление:")  
lbl.place(x = 175, y = 9)

lbl = Label(window, text="Количество:")  
lbl.place(x = 330, y = 9)


combo=[]
direction = []
size = []
size_var = []


for i in range(5):
    combo.append(Combobox(window))
    combo[i]['values'] = (uniq_offers)  
    if i == 0: 
        combo[i].current(1)
    else:
        combo[i].current(0)
    combo[i].place(x = 20, y = 30 + i * 25)

    direction.append(Combobox(window))
    direction[i]['values'] = (directions)  
    if i == 0: 
        direction[i].current(0)
    else:
        direction[i].current(2)
    direction[i].place(x = 175, y = 30 + i * 25)

    size_var.append(StringVar())
    size.append(Entry(textvariable = size_var[i], width=12, justify=RIGHT))
    # size[i] = Entry(textvariable = size_var[i], width=12, justify=RIGHT)
    if i == 0: 
        size[i].insert(0, "10")
    else:
        size[i].insert(0, "")
    size[i].place(x = 330, y = 30 + i * 25) 


message_button = Button(text="выставить заявки", width=18, height=4, bg='#FFFFFF', command=save_orders)
message_button.place(x = 425, y = 30)

message_button = Button(text="очистить", width=18, height=2, bg='#E4E4E4', command=clears_all_tikers)
message_button.place(x = 425, y = 108)


window.mainloop()