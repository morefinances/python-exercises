# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:35:30 2023

@author: S.Stycenkov
"""

N = 210

print("\n| ", end ='')
for i in range(N):
    print('{:3d}'.format(i+1), " | ", end="")
    if (i + 1)%15==0 and i != (N - 1):
        print("\n| ", end ='')