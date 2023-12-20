# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:33:07 2023

@author: S.Stycenkov

"""
import random as rnd
import colorama
from colorama import Fore, Style, Back

def mycolor(num):
    if num == 0:
        print(Fore.RED, end = "")
    elif num == 1:
        print(Fore.GREEN, end = "")
    elif num == 2:
        print(Fore.BLUE, end = "")
    elif num == 3:
        print(Fore.WHITE, end = "")
    elif num == 4:
        print(Fore.YELLOW, end = "")
    elif num == 5:
        print(Fore.MAGENTA, end = "")
    elif num == 6:
        print(Fore.CYAN, end = "")

# print(rnd.randint(0,9))
print()
colorama.init() 

for i in range(50):
    if i == 0:
        lastcolor = 0
    else:
        lastcolor = newcolor
    newcolor = rnd.randint(0, 6)
    if i<10:
        s_ = " –––>"
    else:
        s_ = " ––>"
    mycolor(6)
    print(i, s_, end = "")
    for _ in range(12):
        if (i+1)*(_ + 1)<30:
            mycolor(2)
        elif 30.00<=(i+1)*(_ + 1)<100:
            mycolor(3)
        elif 100.00<=(i+1)*(_ + 1)<300:
            mycolor(5)
        elif (i+1)*(_ + 1)>=500:
            mycolor(0)
        else:
            mycolor(1)
        print('{:4d}'.format((i+1)*(_ + 1)), "", sep=".0" + str(rnd.randint(0,9)), end="")
    print()