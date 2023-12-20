# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:59:09 2023

@author: S.Stycenkov
"""
import random as rnd

print()
for i in range(100):
    a = '{:04d}'.format(i+1)
    a = str(rnd.randint(0,9)) + "/" + a[1] + "." + a[2] + ".." + a[3]
    print(a)
    if (i+1)%10==0:
        print()