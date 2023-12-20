# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 11:23:39 2023

@author: S.Stycenkov
"""

from tkinter import *
import time
import os

root = Tk()
frames = [PhotoImage(file='C:/Users/S.Stycenkov/Documents/alfac/Epitrochoid.gif',format = 'gif -index %i' %(i)) for i in range(66)]
def update(ind):
    frame = frames[ind]
    ind = ind+1 if ind<66 else 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()