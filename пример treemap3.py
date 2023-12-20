# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:05:11 2023

@author: S.Stycenkov
"""

import matplotlib.pyplot as plt
import squarify # pip install squarify (algorithm for treemap)
from tkinter import *
 
root = Tk()
# root.geometry('430x250')
# root.place(x = 80, y = 42) 
# root.geometry(f"+{(root.winfo_screenwidth())//2}+{(root.winfo_screenheight())//2}")
wm = int(0.5*root.winfo_screenwidth())-210
wh = int(0.5*root.winfo_screenheight())-230
root.title("treemap")
root.geometry('445x555+{}+{}'.format(wm,wh))

c = Canvas(root, width=100, height=100, bg='white')
c.place( x = 0, y = 0)

root.mainloop()

# Change color
size_one = [43588329451, 9279307154, 7024189810, 6546090798, 3464378551, 3385643940, 3207664984, 3117265120, 2990553134, 2667701042, 2342680814, 2159204627, 2047272350, 2016556954, 1973535230, 1959003447, 1913514231, 1882979609, 1851749763, 1794734348, 1777258706, 1621673162, 1607975994, 1600672415, 1598520472, 1423587959, 1348120797, 1315026382, 1311379851, 1309218230]

label_one = ["SBER", "LKOH", "GAZP", "VTBR", "TRMK", "GMKN", "SBERP", "TCSG", "FEES", "YNDX", "MGNT", "SNGSP", "TRNFP", "MTLR", "FESH", "ROSN", "RNFT", "MTSS", "PLZL", "VKCO", "TATN", "NLMK", "ALRS", "RUAL", "FLOT", "FIVE", "MAGN", "GEMC", "CHMF", "NVTK"]

squarify.plot(sizes=size_one, label=label_one, color=["red","green","blue", "grey", "red","green","blue", "grey", "red","green","blue"], alpha=.3 )

plt.axis('off')
plt.show()