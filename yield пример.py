# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:00:30 2023

@author: S.Stycenkov
"""

def numbers_range(n):
    for i in range(n):
        yield i


a = numbers_range(int(input()))
print(a[1])
