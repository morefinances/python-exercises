# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 09:12:47 2022

@author: S.Stycenkov
"""

a = [[] for i in range(10)]


for i in range(len(a)):
    a[i]=[[] for i in range(10)]
    for k in range(len(a[i])):
        a[i][k]=[0 for i in range(10)]
    print(a[i])

    
print("---")
print(a)