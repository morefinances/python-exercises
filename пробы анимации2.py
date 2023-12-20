# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:31:07 2023

@author: S.Stycenkov
"""

from tkinter import *
root = Tk()
c = Canvas(width=500, height=500, bg='white')

ww = int(0.5*root.winfo_screenwidth())-250
wh = int(0.5*root.winfo_screenheight())-250
root.geometry('500x500+{}+{}'.format(ww,wh))

ball = c.create_oval(150, 150, 250, 250, fill='lightblue')

# r = c.create_rectangle(100,100,300,300, fill='yellow',
                   # outline='green',
                   # width=3,
                   # activedash=(5, 4))

c.create_line(100, 100, 400, 400)

i = 0

def my_draw(i):
    c.move(ball, 3, 2)
    i +=1
    if i == 50: return i
    c.after(20,my_draw, i)
    

c.focus_set()
c.pack()

c.after(50,my_draw(i))



root.mainloop()