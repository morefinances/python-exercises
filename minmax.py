# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:07:50 2023

@author: S.Stycenkov
"""

import random
print()

m = [random.randint(-1000, 1000) for i in range(15)]

# m = [int(x) for x in input().split()]
max = m[1]
min = m[1]

print(*m)

ind = 0
indm = 0
for i, y in enumerate(m):
    if y < min:
        min = y
        indm = i
    if y > max:
        max = y
        ind = i
print(ind, max)
print(indm, min)
