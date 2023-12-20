# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:20:43 2023

@author: S.Stycenkov
"""
# import math

a, b = int(input()), int(input())

def exp(a, n):
    exp = 1
    # if n>0:
    #     print("n")
    # else:
    #     print("-n")
    for i in range(abs(n)):
        if n>0:
            exp *= a
        if n<0:
            exp /= a
    return exp

print(exp(a,b))