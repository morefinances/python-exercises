# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:23:16 2023

@author: S.Stycenkov
"""

N = int(input())

# n = [i for i in range(1,N+1)]

m = []

for i in range(1, N):
    if 2**i <= N:
        m = [i, 2**i]
print(*m)
        