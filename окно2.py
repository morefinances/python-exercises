# -*- coding: utf-8 -*-
"""
Created on Fri May 26 14:49:18 2023

@author: S.Stycenkov
"""

from tkinter import *
#исходный код

if __name__ == '__main__':
  #выполнение кода до загрузки
  root = Tk()
  root.title('Заголовок') #заголовок
  lbl1 = Label(root, text='Текст сообщения')
  lbl1.place(x=10,y=10)
  lbl1.grid(column=0, row=0)
  root.mainloop() #отображение окна
