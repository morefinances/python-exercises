# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 12:23:35 2023

@author: S.Stycenkov
"""

from tkinter import *
root = Tk()
c = Canvas(width=300, height=300, 
           bg='white')
c.focus_set()
c.pack()
 
ball = c.create_oval(140, 140, 160, 160, 
                     fill='green')
c.bind('<Up>', 
       lambda event: c.move(ball, 0, -2))
c.bind('<Down>', 
       lambda event: c.move(ball, 0, 2))
c.bind('<Left>', 
       lambda event: c.move(ball, -2, 0))
c.bind('<Right>', 
       lambda event: c.move(ball, 2, 0))
 
root.mainloop()