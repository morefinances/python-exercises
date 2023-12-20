# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 12:34:29 2023

@author: S.Stycenkov
"""

from tkinter import *

tk = Tk()
c = Canvas(tk, width=640, height=640, bg='white')
c.pack()

# сохраняем номер соданной фигуры в переменную
my_favorite_oval = c.create_oval(0, 0, 50, 50, fill='blue')

def moveBall():
    # передвигаем наш овал на 10 пикселей по обеим осям
    c.move(my_favorite_oval, 10, 10)
    # повторяем через 100 мс (1 секунда)
    c.after(100, moveBall)

# спустя 1 секунду (100 мс) после запуска выполнить moveBall
c.after(100, moveBall)

mainloop()