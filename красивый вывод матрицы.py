# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:57:17 2023

@author: S.Stycenkov
"""

a=[[1, 15, 2],
   [3, 18, 0],
   [-1, 22, 17]]

for row in a:
    print('\t'.join([str(elem) for elem in row]))