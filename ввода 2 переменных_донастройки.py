# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:01:53 2023

@author: S.Stycenkov
"""

from tkinter import *
from tkinter import messagebox, scrolledtext  

def display_full_name():
    # messagebox.showinfo("Результат:", a.get() + " " + b.get())  -- изначальный вариант
    # messagebox.showinfo("Результат:", 'М = ' + str(int(a.get()) * int(b.get()))) -- промежуточный
    # txt.configure(state ='normal')
    # txt.insert(INSERT, 'Результат200:')
    print()

    
root = Tk()
# root.geometry('430x250')
# root.place(x = 80, y = 42) 
# root.geometry(f"+{(root.winfo_screenwidth())//2}+{(root.winfo_screenheight())//2}")
wm = int(0.5*root.winfo_screenwidth())-210
wh = int(0.5*root.winfo_screenheight())-225
print(root.geometry('430x550+{}+{}'.format(wm,wh)))
# print(root.winfo_screenwidth())
# print(root.winfo_screenheight())

root.title("Ввод данных")
# root.attributes("-alpha", 0.9)
# root.iconbitmap(default="C:\Users\S.Stycenkov\Documents\alfac\favicon.ico")

a_label = Label(text="Ввод данных 1 (variable A):", font=("Courier New", 13, 'bold'))
a_label.place(x = 80, y = 20) 
a = StringVar()
a_entry = Entry(textvariable=a, font=("Courier New", 13), width=26)
a_entry.place(x = 80, y = 42) 
a_entry.focus()

b_label = Label(text="Ввод данных 2 (variable В):", font=("Courier New", 13, 'bold'))
b_label.place(x = 80, y = 80) 
b = StringVar()
b_entry = Entry(textvariable=b, font=("Courier New", 13), width=26)
b_entry.place(x = 80, y = 110) 


c_label = Label(text=".."*33, font=("Arial", 12))
c_label.place(x = 80, y = 230) 
# c = StringVar()

# txt = scrolledtext.ScrolledText(root, width=33, height=10) 
# txt.place(x = 80, y = 300)
# txt.insert(INSERT, 'Результат:')
# txt.configure(state ='disabled')

txt=Text(width=33, height=10, wrap=WORD) # текст, вернуться позже
txt.place(x = 80, y = 300)
txt.configure(state ='disabled')

# txt.geometry('200x100')



message_button = Button(text="Расчет", command=display_full_name, font=("Courier New", 12))
message_button.place(x = 180, y = 160)
# message_button.grid(row=5, column=1)

root.mainloop()