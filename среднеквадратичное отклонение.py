# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:00:47 2023

@author: S.Stycenkov
"""

N = -1
summ = 0
sq = 0

m = []

while N != 0:
    N=int(input())
    if N !=0:
        summ += N
        m.append(N)

ssum = summ / len(m)

for i in m:
    sq += (i - ssum)**2 

final = (sq / (len(m)-1))**0.5

print(final)
    