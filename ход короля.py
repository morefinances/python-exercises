# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:43:12 2023

@author: S.Stycenkov
"""

x = [int(input()) for i in range(4)]

if abs(x[0]-x[2])<=1 and abs(x[1]-x[3])<=1:
    print("YES")
else:
    print("NO")
