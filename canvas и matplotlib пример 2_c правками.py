# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:34:41 2023

@author: S.Stycenkov
"""

from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from random import choice
import numpy as np

def circle(x):
    return (100**2-(x**2))**0.5


 
def print_hello():
    print('hello')

def new_smile():
    print(':-)')

  
    

window = Tk() 

canvas1 = None

window.title('Plotting in Tkinter') 
window.geometry("700x700") 

btn = Button(
    master = window, 
    text = 'Generate scatter chart', 
    command = print_hello, 
    padx = 5, pady = 5
)
btn.pack()

btn2 = Button(
    master = window, 
    text = 'Close scatter chart', 
    command = new_smile, 
    padx = 5, pady = 5
)
btn2.pack()

fig = Figure(figsize=(10, 10), dpi=100)
ax = fig.add_subplot(111) 

# fill_arrs() 
X = np.arange(-100, 100, 0.01)
Y = [circle(i) for i in X]
Y2 = [-circle(i) for i in X]
ax.scatter(X, Y, s = 1)   
ax.scatter(X, Y2, s = 1)  

canvas1 = FigureCanvasTkAgg(fig, master = window)
canvas1.draw()
canvas1.get_tk_widget().pack(side=TOP, fill=NONE, expand=0)
# window.after(10, None)

window.mainloop()