# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:12:17 2023

@author: S.Stycenkov
"""

import random

# x = [int(e) for e in input().split()]

x = [random.randint(0,99) for i in range(100)]
print(x)

y = list(set(x))
print(y)

final = []
uno = []

for elem in y:
    if x.count(elem)>1:
        final.append(elem)
    else:
        uno.append(elem)

print(*final) 
print(len(final))
print()
print(*uno)
print(len(uno))
