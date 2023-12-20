# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:43:39 2023

@author: S.Stycenkov
"""

a = 1

N = int(input())

pi = 1

for i in range(1, N):
    pi *= ( (2*i)**2 ) / ( (2*i - 1) * (2*i + 1) )
    # print(i, pi)

print(2*pi)