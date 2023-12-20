# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:30:44 2023

@author: S.Stycenkov
"""

def mysum(start, finish):
    _sum = 0
    for i in range(start, finish + 1):
        _sum += i
    return _sum
        
print(mysum(10, 12))