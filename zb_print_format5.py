# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:30:45 2023

@author: S.Stycenkov
"""
a = 0
for i in range(500):
    if a == 0:
        print("| ", end = '')
    print('{:03d}'.format(i + 1), end = " | ")
    a += 1
    if (i + 1) % 10 == 0:
        print()
        a = 0