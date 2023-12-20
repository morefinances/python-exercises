# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:31:07 2023

@author: S.Stycenkov
"""

from tkinter import *
import math

# math.cos(m * i * math.pi / 180)

root = Tk()
c = Canvas(width=500, height=500, bg='white')

ww = int(0.5*root.winfo_screenwidth())-250
wh = int(0.5*root.winfo_screenheight())-250
root.geometry('500x500+{}+{}'.format(ww,wh))

def newx(x):
    return x + 250

def newy(y):
    return 250 - y

def circle_coord(A, B):
    Xone, Yone = A - 25, B + 25
    Xtwo, Ytwo = A + 25, B  - 25    
    return newx(Xone), newy(Yone), newx(Xtwo), newy(Ytwo)

def delta_coord(R, r, i):
    X1 = (R + r) * math.cos(i * math.pi / 180)
    X2 = (R + r) * math.cos((i + 1) * math.pi / 180)
    Y1 = (R + r) * math.cos(i * math.pi / 180)
    Y2 = (R + r) * math.cos((i + 1) * math.pi / 180)
    print (int(X2-X1), int(Y2-Y1))
    return int(X2-X1), int(Y2-Y1)

def delta_coordX(R, r, i, xx):
    X1 = (R + r) * math.cos(i * math.pi / 180)
    X2 = (R + r) * math.cos((i + 1) * math.pi / 180)
    print (int(X2-X1))
    return int(X2-X1)

def delta_coordY(R, r, i, yy):
    Y1 = (R + r) * math.sin(i * math.pi / 180)
    Y2 = (R + r) * math.sin((i + 1) * math.pi / 180)
    print (int(Y2-Y1))
    return int(Y2-Y1)
    

ball = c.create_oval(circle_coord(125,0), fill='lightblue')
ball2 = c.create_oval(newx(-100), newy(-100), newx(100), newy(100))


# r = c.create_rectangle(100,100,300,300, fill='yellow',
                   # outline='green',
                   # width=3,
                   # activedash=(5, 4))

c.create_line(0, 250, 500, 250)
c.create_line(250, 0, 250, 500)



def my_draw(i, R, r, xx, yy):
    print(i)
    X2 = (R + r) * math.cos((i + 1) * math.pi / 180)
    print(X2, int(X2-xx))
    Y2 = (R + r) * math.sin((i + 1) * math.pi / 180)    
    print(Y2, int(Y2-yy))
    c.move(ball, int(X2-xx), int(Y2-yy))
    xx = X2
    yy = Y2
    
    i += 1 
    if i == 10: return
    c.after(50, my_draw(i, R, r, xx, yy))
    

c.focus_set()
c.pack()

i = 0
xx = 125
yy = 0
R  = 100
r = 50
c.after(50,my_draw(i, R, r, xx, yy))
# print(delta_coord(100,50,i))


root.mainloop()