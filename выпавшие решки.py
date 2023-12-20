# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:56:18 2023

@author: S.Stycenkov
"""

s = input()
Max = 0
ind = 0
mm = 0
for i in range(len(s)):
    # print(s[i], ind, mm, end="\t")
    if s[i] == "Р": 
        if ind == 0:
            ind = 1
            mm = 1
        else:
            mm += 1
    if s[i] == "О" and ind==1:
        ind = 0
        if mm>Max: Max = mm     
        mm = 0
    if i==len(s)-1: 
        if mm>Max: Max = mm 
    # print("/", s[i], ind, mm, end="\n")
print(Max)

# s = input().split('О')
# print(len(max(s)))

# в одну строку
# print(len(max(input().split('О'))))