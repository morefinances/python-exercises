# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:35:34 2023

@author: S.Stycenkov
"""

import random
from colorama import init, Back

init()

def myint(x):
    return elem-int(elem)==0
    

# y=random.random()
#print(Back.CYAN + str(int(100*y)/10) + Back.RESET)

u = [int(100*random.random())/10 for i in range(100)]
for elem in u:
    if elem-int(elem)==0: 
        print(Back.CYAN, myint(elem), Back.RESET, end=" ")
    else:
        print(elem-int(elem)==0, end=" ")
    print("\t", elem, elem-int(elem), ":", sep="\t")
    