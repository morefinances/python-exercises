# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:59:58 2023

@author: S.Stycenkov
"""

# исключаем повторы

import random as rnd
import copy

txt = []
distribution = []

txt.append("qwertyuiopasdfghjklzxcvbnm")
distribution.append(0.35)

txt.append("QWERTYUIOPASDFGHJKLZXCVBNM")
distribution.append(0.3)

txt.append("1234567890")
distribution.append(0.2)

txt.append("!@#$%^&*()_-|{}")
distribution.append(0.15)

numb = int(input())
print()



for _ in range(20):
    data = rnd.choices(txt, weights=distribution, k=numb)
    passw = ""
    for i in range(len(data)):
        endind = True
        while endind:
            u = rnd.randint(0, len(data[i])-1)
            if str(data[i][u]) not in passw:
                endind = False
        passw += str(data[i][u])
        
    print('{:2d}'.format(_ + 1), ': ', passw, sep = '')
