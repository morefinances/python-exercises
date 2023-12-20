# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:43:11 2023

@author: S.Stycenkov
"""

x = [int(input()) for i in range(4)]

if x[2]-x[0] != 0:
    t = (x[3]-x[1])/(x[2]-x[0])

if x[0]==x[2] or x[1]==x[3] or abs(t)==1:
    print("YES")
else:
    print("NO")