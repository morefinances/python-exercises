# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:36:24 2023

@author: S.Stycenkov
"""

from tkinter import * 

def my_int(e, u, a):
    print(e)
    label_result.config(text=e) 
    return e
 
top = Tk() 
top.title("Ввод переменных")   
top.geometry("400x250") 
 
name = Label(top, text = "Переменная A:").place(x = 30,y = 50) 
 
email = Label(top, text = "Переменная B:").place(x = 30, y = 90) 
 
password = Label(top, text = "Переменная C:").place(x = 30, y = 130) 
 

 
e1 = Entry(top).place(x = 120, y = 51) 
e2 = Entry(top).place(x = 120, y = 91) 
e3 = Entry(top).place(x = 120, y = 131) 

sbmitbtn = Button(top, text = "Ввод", command=my_int(name,email, password), activebackground = "gray", activeforeground = "blue").place(x = 30, y = 180) 

# buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0) 
 
top.mainloop() 
# Источник: https://pythonpip.ru/osnovy/vidzhet-tkinter-entry-v-python-kak-ispolzovat