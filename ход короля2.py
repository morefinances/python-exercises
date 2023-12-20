# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:17:11 2023

@author: S.Stycenkov
"""

b = [int(i) for i in list(input().split())]
 
t = (b[0]-b[2])**2 + (b[1]-b[3])**2

if 1<=t<=2:
    print("YES")
else:
    print("NO")