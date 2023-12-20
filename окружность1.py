# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:01:53 2023

@author: S.Stycenkov
"""

from tkinter import *
from tkinter import messagebox, scrolledtext  

def display_full_name():
    print(a_entry.get())
    print(b_entry.get())
    print(h.get())
    print(Q.get())
    

def myplot(x, y):
    maingraph.create_line(x, y, x+1, y, fill="black") 

def newx(x):
    return x + 250
    
def newy(y):
    return 250 - y

    
root = Tk()
ww = int(0.5*root.winfo_screenwidth())-410
wh = int(0.5*root.winfo_screenheight())-300
root.geometry('770x555+{}+{}'.format(ww,wh))

root.title("Циклоидальные кривые")


a_label = Label(text="R", font=("Courier New", 13, 'bold'))
a_label.place(x = 30, y = 20) 
a = StringVar(value=35)
a_entry = Spinbox(from_=0.0, to=200.0, increment=10, textvariable=a)
a_entry.place(x = 33, y = 42) 
a_entry.focus()

b_label = Label(text="r", font=("Courier New", 13, 'bold'))
b_label.place(x = 30, y = 80) 
b = StringVar(value=15)
b_entry = Spinbox(from_=1.0, to=100.0, increment=10, textvariable=b)
b_entry.place(x = 33, y = 102) 



h_label = Label(text="h", font=("Courier New", 13, 'bold'))
h_label.place(x = 30, y = 140) 
h = StringVar(value=3)
h_entry = Spinbox(from_=1.0, to=100.0, textvariable=h)
h_entry.place(x = 33, y = 162) 

Q_label = Label(text="Q", font=("Courier New", 13, 'bold'))
Q_label.place(x = 30, y = 200) 
Q = StringVar(value=5000)
Q_entry = Spinbox(from_=1000.0, to=10000.0, increment=1000, textvariable=Q)
Q_entry.place(x = 33, y = 222) 

c = Canvas(root, width=0, height=300, bg='gray')
c.place( x = 200, y = 25)
# c.pack()

maingraph = Canvas(root, width=500, height=500, bg='white')
maingraph.place( x = 230, y = 25)

for i in range(-200, 200):
    Y = (200**2-i**2)**0.5
    myplot(newx(i),newy(Y))
    myplot(newx(i),newy(-Y))
    print(newx(i), newy(Y))




message_button = Button(text="Расчет", command=display_full_name, font=("Courier New", 12),
                        height = 3, width = 13)
message_button.place(x = 33, y = 260)

root.mainloop()