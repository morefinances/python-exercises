# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:33:07 2023

@author: S.Stycenkov

"""
import random as rnd

# print(rnd.randint(0,9))
print()

for i in range(50):
    if i<10:
        s_ = " –––>"
    else:
        s_ = " ––>"
    print(i, s_, end = "")
    for _ in range(12):
        print('{:4d}'.format((i+1)*(_ + 1)), "", sep=".0" + str(rnd.randint(0,9)), end="")
    print()