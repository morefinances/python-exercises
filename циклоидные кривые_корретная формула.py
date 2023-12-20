# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:01:53 2023

@author: S.Stycenkov
"""

from tkinter import *
from tkinter import messagebox, scrolledtext  
import math

def display_full_name():
    myclear()
    R = int(a_entry.get())
    r = int(b_entry.get())
    h = int(hs.get())
    if R != 0:
        m = r / R
    else:
        m = 1
    for i in range(int(Q.get())):
        # xx = R * (1 - m) * math.cos(m * i * math.pi / 180) + h * math.cos((1 - m) * i * math.pi / 180)
        xx = R * (m + 1) * math.cos(m * i * math.pi / 180) - h * math.cos((m + 1) * i * math.pi / 180)
        # yy = R * (1 - m) * math.sin(m * i * math.pi / 180) - h * math.sin((1 - m) * i * math.pi / 180) 
        yy = R * (m + 1) * math.sin(m * i * math.pi / 180) - h * math.sin((m + 1) * i * math.pi / 180)
        myplot(int(newx(xx)),int(newy(yy)))      

def myclear():
    maingraph.create_rectangle(0, 0, 502, 502,
                   fill='white',
                   width=0)

def myplot(x, y):
    maingraph.create_line(x, y, x+1, y, fill="black") 

def newx(x):
    return x + 250
    
def newy(y):
    return 250 - y

    
root = Tk()
ww = int(0.5*root.winfo_screenwidth())-410
wh = int(0.5*root.winfo_screenheight())-300
root.geometry('770x650+{}+{}'.format(ww,wh))

root.title("Циклоидальные кривые: эпициклоида")


a_label = Label(text="R", font=("Courier New", 13, 'bold'))
a_label.place(x = 30, y = 20) 
a = StringVar(value=110)
a_entry = Spinbox(from_=0.0, to=200.0, increment=10, textvariable=a)
a_entry.place(x = 33, y = 42) 
a_entry.focus()

b_label = Label(text="r", font=("Courier New", 13, 'bold'))
b_label.place(x = 30, y = 80) 
b = StringVar(value=70)
b_entry = Spinbox(from_=1.0, to=100.0, increment=10, textvariable=b)
b_entry.place(x = 33, y = 102) 



h_label = Label(text="h", font=("Courier New", 13, 'bold'))
h_label.place(x = 30, y = 140) 
hs = StringVar(value=50)
h_entry = Spinbox(from_=1.0, to=100.0, increment=5, textvariable=hs)
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

# for i in range(0, 1000):
#     X = 220 * math.cos(i * math.pi / 180)
#     Y = 220 * math.sin(i * math.pi / 180)
#     myplot(newx(X),newy(Y))

# кнопка
message_button = Button(text="Расчет", command=display_full_name, font=("Courier New", 12),
                        height = 2, width = 13)
message_button.place(x = 33, y = 260)


txt=Text(width=40, height=4, wrap=WORD, font=("Courier New", 10)) # текст, вернуться позже
txt.place(x = 30, y = 555)
txt.insert(1.0,'Эпициклоида — плоская кривая, образуемая фиксированной точкой окружности (r), катящейся по внешней стороне другой окружности (R) без скольжения. ')
txt.configure(state ='disabled')

txt2=Text(width=43, height=4, wrap=WORD, font=("Courier New", 10)) # текст, вернуться позже
txt2.place(x = 380, y = 555)
txt2.insert(1.0,'Уравнения эпициклоиды:\n\nx = R * (1 + m) * cos(mt) – h * cos(t + mt) \ny = R * (1 – m) * sin(mt) + h * sin(t – mt)')
txt2.configure(state ='disabled')


root.mainloop()