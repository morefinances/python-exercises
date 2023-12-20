# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:12:28 2023

@author: S.Stycenkov
"""

import tkinter as tk
 
# Создается новое окно с заголовком "Введите домашний адрес"
window = tk.Tk()
window.title("Ввод переменных")
 
# Создается новая рамка `frm_form` для ярлыков с текстом и
# Однострочных полей для ввода информации об адресе.
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Помещает рамку в окно приложения.
frm_form.pack()
 
# Создает ярлык и текстовок поле для ввода имени.
lbl_a = tk.Label(master=frm_form, text="Переменная А:")
ent_a = tk.Entry(master=frm_form, width=50)
# Использует менеджер геометрии grid для размещения ярлыка и
# однострочного поля для ввода текста в первый и второй столбец
# первой строки сетки.
lbl_a.grid(row=0, column=0, sticky="e")
ent_a.grid(row=0, column=1)
  
# Создает ярлык и текстовок поле для ввода имени.
lbl_b = tk.Label(master=frm_form, text="Переменная B:")
ent_b = tk.Entry(master=frm_form, width=50)
# Использует менеджер геометрии grid для размещения ярлыка и
# однострочного поля для ввода текста в первый и второй столбец
# первой строки сетки.
lbl_b.grid(row=1, column=0, sticky="e")
ent_b.grid(row=1, column=1)   
  
  
 
# Создает новую рамку `frm_buttons` для размещения
# кнопок "Отправить" и "Очистить". Данная рамка заполняет
# все окно в горизонтальном направлении с
# отступами в 5 пикселей горизонтально и вертикально.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
 
# Создает кнопку "Отправить" и размещает ее
# справа от рамки `frm_buttons`.
btn_submit = tk.Button(master=frm_buttons, text="Отправить")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
 
# Создает кнопку "Очистить" и размещает ее
# справа от рамки `frm_buttons`.
btn_clear = tk.Button(master=frm_buttons, text="Очистить")
btn_clear.pack(side=tk.RIGHT, ipadx=10)
 
# Запуск приложения.
window.mainloop()