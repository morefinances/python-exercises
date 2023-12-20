# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 10:07:10 2023

@author: S.Stycenkov
"""

from tkinter import *  
from tkinter.ttk import Radiobutton  
  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
rad1 = Radiobutton(window, text='Первый', value=1)  
rad2 = Radiobutton(window, text='Второй', value=2)  
rad3 = Radiobutton(window, text='Третий', value=3)  
rad1.grid(column=0, row=0)  
rad2.grid(column=1, row=0)  
rad3.grid(column=2, row=0)  
window.mainloop()