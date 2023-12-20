# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:01:53 2023

@author: S.Stycenkov
"""

from tkinter import *
from tkinter import messagebox, scrolledtext  
import math
# from time import sleep 

def maincircle():
    maingraph.create_oval(newx(-150), newy(-150), newx(150), newy(150), outline="black", width=2)

def txtins():
    if curvepoint.get()==0:
        textcurve="Эпициклоида — плоская кривая, образуемая фиксированной точкой окружности (r), катящейся по внешней стороне другой окружности (R) без скольжения. "
        textcurve2="Уравнения эпициклоиды:\n\nx = R * (1 + m) * cos(mt) – h * cos(t + mt) \ny = R * (1 – m) * sin(mt) + h * sin(t – mt)"
    else:
        textcurve="Гипоциклоида — плоская кривая, образуемая фиксированной точкой окружности (r), катящейся по внутренней стороне другой окружности (R) без скольжения. "
        textcurve2="Уравнения гипоциклоиды:\n\nx = R * (1 - m) * cos(mt) + h * cos(t + mt) \ny = R * (1 – m) * sin(mt) - h * sin(t – mt)"
    txt.configure(state ='normal')
    txt.delete(1.0, 'end')
    txt.insert(1.0, textcurve)
    txt.configure(state ='disabled')
    txt2.configure(state ='normal')
    txt2.delete(1.0, 'end')
    txt2.insert(1.0, textcurve2)
    ztxt == 1
    txt2.configure(state ='disabled')

def secondcircle(alfa, R, r, m):
    X=(R+r)*math.cos(m * alfa * math.pi / 180)
    Y=(R+r)*math.sin(m * alfa * math.pi / 180)
    maingraph.create_oval(newx(X-r), newy(Y-r), newx(X+r), newy(Y+r), outline="lightgray", width=1)

def unocircle(alfa, R, r, m):
    X=(R-r)*math.cos(m * alfa * math.pi / 180)
    Y=(R-r)*math.sin(m * alfa * math.pi / 180)
    maingraph.create_oval(newx(X-r), newy(Y-r), newx(X+r), newy(Y+r), outline="lightgray", width=1)
    
def demonstration():
    myclear()
    
    R = int(a_entry.get())
    r = int(b_entry.get())
    h = int(hs.get())
    if R != 0:
        m = r / R
    else:
        m = 1
    maingraph.create_line(newx(-250), newx(0), newx(252), newx(0))
    maingraph.create_line(newx(0), newx(-250), newx(0), newx(252))
    maingraph.create_oval(newx(-R), newx(-R), newx(R), newx(R), outline="gray", width=2)
    # maincircle()
    # i = 40
    for i in range(0, int(Q.get()), 20):
        if curvepoint.get()==0:
            secondcircle(i, R, r, m)
            xx = R * (m + 1) * math.cos(m * i * math.pi / 180) - h * math.cos((m + 1) * i * math.pi / 180)
            yy = R * (m + 1) * math.sin(m * i * math.pi / 180) - h * math.sin((m + 1) * i * math.pi / 180)   
        else:
            unocircle(i, R, r, m)
            xx = R * (1 - m) * math.cos(m * i * math.pi / 180) + h * math.cos((1 - m) * i * math.pi / 180)
            yy = R * (1 - m) * math.sin(m * i * math.pi / 180) - h * math.sin((1 - m) * i * math.pi / 180) 
        mypoint(newx(xx), newy(yy))
        # print(i, (m * i * math.pi / 180))
        # if (m * i * math.pi / 180)>= 2 * math.pi: break
        
    
def display_full_name():
    myclear()
    if ztxt == 0: txtins()
    # print(curvepoint.get())
    R = int(a_entry.get())
    r = int(b_entry.get())
    h = int(hs.get())
    if R != 0:
        m = r / R
    else:
        m = 1
    for i in range(int(Q.get())):
        if curvepoint.get()==0:
            xx = R * (m + 1) * math.cos(m * i * math.pi / 180) - h * math.cos((m + 1) * i * math.pi / 180)
            yy = R * (m + 1) * math.sin(m * i * math.pi / 180) - h * math.sin((m + 1) * i * math.pi / 180)
        else:
            xx = R * (1 - m) * math.cos(m * i * math.pi / 180) + h * math.cos((1 - m) * i * math.pi / 180)
            yy = R * (1 - m) * math.sin(m * i * math.pi / 180) - h * math.sin((1 - m) * i * math.pi / 180) 
        myplot(int(newx(xx)),int(newy(yy)))      

def myclear():
    maingraph.create_rectangle(0, 0, 502, 502, fill='white',width=0)

def myplot(x, y):
    maingraph.create_line(x, y, x+1, y, fill="black") 
    
def mypoint(x, y):
    # maingraph.create_line(x, y, x+1, y+1, fill="black")
    maingraph.create_rectangle(x, y, x+1, y+1, outline="blueviolet", width=2)


def newx(x):
    return x + 250
    
def newy(y):
    return 250 - y

def welcometxt():
    messagebox.showinfo('Добро пожаловать!', "Программа расчета трансцендентных циклоидальных кривых: эпициклоид и гипоциклоид.\n\nВерсия 1.0.2.\nСержиусПроджектПродакшн © 06.06.2023")
    
    
root = Tk()
ww = int(0.5*root.winfo_screenwidth())-330
wh = int(0.5*root.winfo_screenheight())-300
root.geometry('770x660+{}+{}'.format(ww,wh))

root.title("Циклоидальные кривые: эпициклоида и гипоциклоида.")

ztxt=0
welcometxt()

curvepoint = IntVar()
curvepoint.set(0)

epi_btn = Radiobutton(text="Эпициклоида", value=0, variable=curvepoint, font=("Courier New", 13), command=txtins)
epi_btn.place(x = 30, y = 20)

tro_btn = Radiobutton(text="Гипоциклоида", value=1, variable=curvepoint, font=("Courier New", 13), command=txtins)
tro_btn.place(x = 30, y = 50)




a_label = Label(text="R", font=("Courier New", 13, 'bold'))
a_label.place(x = 30, y = 80) 
a = StringVar(value=110)
a_entry = Spinbox(from_=0.0, to=200.0, increment=10, textvariable=a, state ='normal')
a_entry.place(x = 33, y = 102) 
a_entry.focus()

b_label = Label(text="r", font=("Courier New", 13, 'bold'))
b_label.place(x = 30, y = 120) 
b = StringVar(value=30)
b_entry = Spinbox(from_=1.0, to=100.0, increment=10, textvariable=b, state ='normal')
b_entry.place(x = 33, y = 142) 
# b_entry.configure()



h_label = Label(text="h", font=("Courier New", 13, 'bold'))
h_label.place(x = 30, y = 160) 
hs = StringVar(value=50)
h_entry = Spinbox(from_=1.0, to=100.0, increment=5, textvariable=hs, state = 'normal')
h_entry.place(x = 33, y = 182) 


Q_label = Label(text="Q", font=("Courier New", 13, 'bold'))
Q_label.place(x = 30, y = 200) 
Q = StringVar(value=5000)
Q_entry = Spinbox(from_=1000.0, to=20000.0, increment=1000, textvariable=Q, state ='normal')
Q_entry.place(x = 33, y = 222) 


c = Canvas(root, width=0, height=300, bg='gray')
c.place( x = 200, y = 25)


maingraph = Canvas(root, width=500, height=500, bg='white')
maingraph.place( x = 230, y = 25)


# кнопка
message_button = Button(text="Статика", command=display_full_name, font=("Courier New", 12),
                        height = 2, width = 13)
message_button.place(x = 33, y = 280)

button_two = Button(text="Динамика", command=demonstration, font=("Courier New", 12),
                        height = 2, width = 13)
button_two.place(x = 33, y = 350)



    
txt=Text(width=40, height=5, wrap=WORD, font=("Courier New", 10)) # текст, вернуться позже
txt.place(x = 30, y = 555)
# txt.configure(state ='disabled')

txt2=Text(width=43, height=5, wrap=WORD, font=("Courier New", 10)) # текст, вернуться позже
txt2.place(x = 380, y = 555)
# txt2.insert(1.0,'Уравнения эпициклоиды:\n\nx = R * (1 + m) * cos(mt) – h * cos(t + mt) \ny = R * (1 – m) * sin(mt) + h * sin(t – mt)')
# txt2.configure(state ='disabled')


root.mainloop()