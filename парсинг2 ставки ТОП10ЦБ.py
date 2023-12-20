# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:11:05 2023

@author: S.Stycenkov
"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tkinter import * 

URL_TEMPLATE = "https://www.cbr.ru/statistics/avgprocstav/"
r = requests.get(URL_TEMPLATE)
# print(r.text)

soup = bs(r.text, "html.parser")
vacancies_names = soup.find_all('table', class_='data')

for name in vacancies_names:
    # print(name.text[2:80])      
    window = Tk()  
    window.title("Динамика максимальной процентной ставки")
    ww = int(0.5*window.winfo_screenwidth())-115
    wh = int(0.5*window.winfo_screenheight())-225
    window.geometry('230x450+{}+{}'.format(ww,wh))
    lbl = Label(window, text=name.text[2:80], font=("Courier New", 18)) 
    lbl.place(x=30, y=10) 
    # lbl.grid(column=0, row=0)  
    window.mainloop()
     