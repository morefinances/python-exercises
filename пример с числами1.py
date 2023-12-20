# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:05:31 2023

@author: S.Stycenkov
"""

print(*[i for i in range(int(input()),int(input()) - 1, -1) if i%2 != 0])