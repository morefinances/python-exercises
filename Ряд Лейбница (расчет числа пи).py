# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:43:39 2023

@author: S.Stycenkov
"""

a = 1

N = int(input())

pi = 1

for i in range(1, N):
    if i%2 == 0:
        pi += 1 / ( 2 * i + 1)
    else:
        # print(i)
        pi -= 1 / ( 2 * i + 1)
        
print(4*pi)