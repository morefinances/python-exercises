# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:48:36 2023

@author: S.Stycenkov
"""
import pandas as pd
from tkinter import *  
from tkinter.ttk import Combobox  
from time import sleep
import datetime as dtm

none_str = ['' , '' ]

number_string = 6

def clears_all_tikers():
    for i in range(number_string):
        combo[i].current(0)
        direction[i].current(2)
        size[i].delete(0, END)


def save_orders():
    global total_id
    A = []
    B = []
    C = []
    D = []
    for u in range(number_string):
        if combo[u].get() != none_str[0] and direction[u].get() != none_str[1] and size[u].get() != "":
            A.append(total_id)
            B.append(direction[u].get())
            C.append(size[u].get())
            D.append(combo[u].get())
            total_id += 1
            # if total_id == 2:
            #     total_id = 5
    df=pd.DataFrame({
        'id': A,
        'direct': B,
        'size': C,
        'tiker': D
    })    
    print(df)
    df.to_csv("C:/files/offers.csv", sep=" ", index = False, header = False)
    df.to_csv("C:/files/historyoffers.csv", mode='a', sep=" ", index = False, header = False)
    sleep(1/10)
    print('-' * 30)
    print(dtm.datetime.now())
    
def id_clear():
    global total_id
    total_id = 1

def send_five_orders():
    global total_id
    A = []
    B = []
    C = []
    D = []
    for i in range(0,5):
        #print(i)
        combo[i].current(i+1)
        direction[i].current(i%2)
        size[i].delete(0, END)
        size[i].insert(0, str((i+1)*10))
    for i in range(5):
        A.append(total_id)
        B.append(direction[i].get())
        C.append(size[i].get())
        D.append(combo[i].get())
        total_id += 1

        
    df=pd.DataFrame({
        'id': A,
        'direct': B,
        'size': C,
        'tiker': D
    })    
    print(df)
    df.to_csv("C:/files/offers.csv", sep=" ", index = False, header = False)
    df.to_csv("C:/files/historyoffers.csv", mode='a', sep=" ", index = False, header = False)
    sleep(1/10)
    print('-' * 20)    
    #print('='*25)
    
total_id = 1
    
# считываем тикеры
file = "C:\\files\\tickers_for_work.csv"
offers = pd.read_csv(file, delimiter=';')

#print(offers)

uniq_offers = [none_str[0]]
directions = ['Buy', 'Sell', none_str[1]]

# удаляем дублирование тикеров
for i in range(len(offers.columns)):
    if "." not in offers.columns[i] and "Unnamed" not in offers.columns[i]:
        uniq_offers.append(offers.columns[i])

total_len = 0
for ii in range(1, len(uniq_offers)):
    total_len += len(uniq_offers[ii]) + 3
print('- ' * int(total_len/2))
print('tickers_for_work:')
print(*uniq_offers[1:], sep=" | ")
print('- ' * int(total_len/2))

# создаем панель выставления заявок  
window = Tk()  
window.title("Выставление заявок")  
window.config(bg="#E2F1FE") #CFCFCF
wm = int(0.5*window.winfo_screenwidth())-int(300)
wh = int(0.5*window.winfo_screenheight())-int(150)
window.geometry('{}x{}+{}+{}'.format(600, 210, wm, wh))



lbl = Label(window, text="Выберите инструмент :", bg="#E2F1FE")  
lbl.place(x = 19, y = 9)

lbl = Label(window, text="Направление :", bg="#E2F1FE")  
lbl.place(x = 175, y = 9)

lbl = Label(window, text="Количество :", bg="#E2F1FE")  
lbl.place(x = 330, y = 9)


combo=[]
direction = []
size = []
size_var = []


for i in range(number_string):
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
    if i == 0: 
        size[i].insert(0, "10")
    else:
        size[i].insert(0, "")
    size[i].place(x = 330, y = 30 + i * 25) 


message_button = Button(text="send offers", width=18, height=2, bg="#E2F1FE", command=save_orders)
message_button.place(x = 430, y = 30)

message_button = Button(text="clear", width=8, height=2, bg='white', command=clears_all_tikers)
message_button.place(x = 430, y = 80)

message_button = Button(text="id=1", width=8, height=2, bg='white', command=id_clear)
message_button.place(x = 500, y = 80)

message_button = Button(text="5 offers", width=18, height=2, bg='#CBE6FE', command=send_five_orders)
message_button.place(x = 430, y = 130)


window.mainloop()