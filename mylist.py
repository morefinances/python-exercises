# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:24:18 2023

@author: S.Stycenkov
"""

def mylist(list_one):
    a = []
    for i in range(len(list_one)):
        if i%7 == 0:
           a.append(list_one[i]) 
    return a

n = [i for i in range(100)]
print(mylist(n))
