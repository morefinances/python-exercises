# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:10:07 2023

@author: S.Stycenkov
"""

import pandas as pd
from tkinter import *
from tkinter import ttk

def create_table(dataframe):
    root = Tk()
    root.title("Таблица данных")
 
    # Создаем таблицу с использованием ttk.Treeview
    table = ttk.Treeview(root)
    table["columns"] = tuple(dataframe.columns)
    table["show"] = "headings"
 
    # Добавляем заголовки столбцов
    for column in dataframe.columns:
        table.heading(column, text=column)
 
    # Добавляем данные в таблицу
    for row in dataframe.itertuples(index=False):
        table.insert("", "end", values=tuple(row))
 
    # Добавляем полосу прокрутки для таблицы
    scroll = ttk.Scrollbar(root, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    table.pack(side="left", fill="both")
 
    # Запускаем главный цикл событий tkinter
    root.mainloop()
    
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
}
df = pd.DataFrame(data)

	
create_table(df)