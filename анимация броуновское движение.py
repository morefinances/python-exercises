# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:31:07 2023

@author: S.Stycenkov
"""

import random

from tkinter import *
root = Tk()
c = Canvas(width=500, height=500, bg='white')

ww = int(0.5*root.winfo_screenwidth())-250
wh = int(0.5*root.winfo_screenheight())-250
root.geometry('500x500+{}+{}'.format(ww,wh))

def newx(x):
    return x + 250

def newy(y):
    return 250 - y

ball = c.create_oval(newx(-100), newy(-100), newx(100), newy(100), dash=(1, 1))
ball3 = c.create_oval(newx(-200), newy(-200), newx(200), newy(200), dash=(5, 4))
ball2 = c.create_oval(newx(-15), newy(-15), newx(15), newy(15), fill='lightblue')


c.create_line(0, 250, 500, 250)
c.create_line(250, 0, 250, 500)

i = 0

def my_draw(i):
    x = random.randint(1, 10)
    znak1 = random.randint(1, 10)
    y = random.randint(1, 10)
    znak2 =  random.randint(1, 10)
    if znak1%2 == 0: x = -x
    if znak2%2 == 0: y = -y
    c.move(ball2, x, y)
    i +=1
    if i == 150: return i
    c.after(150,my_draw, i)
    

c.focus_set()
c.pack()

c.after(50,my_draw(i))



root.mainloop()