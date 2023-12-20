# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:16:33 2023

@author: S.Stycenkov
"""
import random

k = random.randint(3, 15)
for ui in range(k):
    ac = ''
    n = random.randint(1, 100)
    for i in range(n):
        S = random.randint(0, 1)
        if S == 1:
            ac += "Р"
        else:
            ac += 'О'
    print(ac)
    s = ac
    # s = input()
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
    print(Max, '\n')
    