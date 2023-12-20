# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:27:22 2023

@author: S.Stycenkov
"""
k = int(input())
for i in range(k):
    print([(u + 1) for u in range(i+1)])
    
# альтернатива
# [print(list(range(1, x + 2))) for x in range(int(input()))]


# n = int(input())
# for i in range(1, n + 1):
#     print(list(range(1, i + 1)))


# print(*[list(range(1, i + 1)) for i in range(1, int(input()) + 1)], sep="\n")