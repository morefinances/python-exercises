# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:26:07 2023

@author: S.Stycenkov
"""
N = int(input())

a, b = 0, 1
if N!=0:
    sch = 0
else:
    sch = 1
sch2 = 0

for i in range(N):
    a, b = b, a + b
    sch += 1
    if a == N:
        sch2 = 1
        break

if N == 0:
    rez = 0
else:
    rez = -1

if sch2 == 1:
    print(sch)
else:
    print(rez)