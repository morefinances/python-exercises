# -*- coding: utf-8 -*-
"""
Created on Tue May 30 11:26:58 2023

@author: S.Stycenkov
"""

from tkinter import *  
from tkinter import ttk  
  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab_control.add(tab1, text='ввод данных')  
tab_control.add(tab2, text='результат')  
lbl1 = Label(tab1, text='Вкладка 1')  
lbl1.grid(column=0, row=0)  
lbl2 = Label(tab2, text='Вкладка 2')  
lbl2.grid(column=0, row=0)  
tab_control.pack(expand=1, fill='both')  
window.mainloop()