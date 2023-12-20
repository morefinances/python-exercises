# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 09:12:47 2022

@author: S.Stycenkov
"""

a = [[] for i in range(100)]


for i in range(len(a)):
    a[i]=[0 for i in range(100)]
    #print(a[i])
    
print("---")
print(a[0][99])