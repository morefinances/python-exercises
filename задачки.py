# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 17:13:21 2023

@author: S.Stycenkov
"""

# количество нулей в хвосте факториала
import math

n = 207 #int(input())

print(math.factorial(n))
l=str(math.factorial(n))
print('количество нулей в числе', l.count('0'))

ind = 0
for i in range(len(l)):
    print(i, l[-1*(1+i)])
    if l[-1*(1+i)] == "0":
        ind += 1
    else:
        print('количество нулей в хвосте = ', i)
        break

