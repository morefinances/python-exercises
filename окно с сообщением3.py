# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:07:04 2023

@author: S.Stycenkov
"""

from tkinter import * 

window = Tk()  
window.title("Окно уведомления")  
window.geometry('400x150')
lbl = Label(window, text="Текст сообщения  ", font=("Courier New", 18)) 
lbl.place(x=80, y=20) 
# lbl.grid(column=0, row=0)  
window.mainloop()