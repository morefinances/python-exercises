# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:29:59 2023

@author: S.Stycenkov
"""

from tkinter import *
 
 
def red_label():
    label['bg'] = 'red'
 
 
def green_label():
    label['bg'] = 'green'
 
 
def blue_label():
    label['bg'] = 'blue'
 
 
root = Tk()
 
var = IntVar()
var.set(0)
Radiobutton(text="Red", command=red_label,
            variable=var, value=0).pack()
Radiobutton(text="Green", command=green_label,
            variable=var, value=1).pack()
Radiobutton(text="Blue", command=blue_label,
            variable=var, value=2).pack()
label = Label(width=20, height=10, bg='red')
label.pack()
 
root.mainloop()