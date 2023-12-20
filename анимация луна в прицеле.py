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

def newx(x):
    return x+250

def newy(y):
    return 250 - y

ball = c.create_oval(newx(-150), newy(150), newx(-50), newy(50), fill='lightblue')
ball2 = c.create_oval(newx(-100), newy(-100), newx(100), newy(100))


# r = c.create_rectangle(100,100,300,300, fill='yellow',
                   # outline='green',
                   # width=3,
                   # activedash=(5, 4))

c.create_line(0, 250, 500, 250)
c.create_line(250, 0, 250, 500)

i = 0

def my_draw(i):
    c.move(ball, 3, 2)
    i +=1
    if i == 65: return i
    c.after(20,my_draw, i)
    

c.focus_set()
c.pack()

c.after(50,my_draw(i))



root.mainloop()