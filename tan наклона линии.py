# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:42:45 2023

@author: S.Stycenkov
"""

x = [int(input()) for i in range(4)]

if x[2]-x[0] != 0:
    t = (x[3]-x[1])/(x[2]-x[0])
    print(t)
