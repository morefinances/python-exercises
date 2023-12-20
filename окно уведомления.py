# -*- coding: utf-8 -*-
"""
Created on Fri May 26 14:18:49 2023

@author: S.Stycenkov

"""
from tkinter import * 

window = Tk()  
window.title("Окно уведомления")  
window.geometry('400x250')
lbl = Label(window, text="Текст сообщения  ", font=("Arial Bold", 22))  
lbl.grid(column=0, row=0)  
btn = Button(window, text="Кнопка")
btn.grid(column=1, row=0)
window.mainloop()

# продолжение:
# https://pythonru.com/uroki/obuchenie-python-gui-uroki-po-tkinter