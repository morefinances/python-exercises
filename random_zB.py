# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:45:04 2023

@author: S.Stycenkov
"""

import random as rd
a = rd.randint(0, 1000)
b = rd.randint(1, 20)
c = 0
print(f'\na:{a} b:{b}\n')
for i in range(0, a, b):
    print(i, end=" ")
    c += 1
print(f'\n\n#c={c}')