# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:00:44 2023

@author: S.Stycenkov
"""

txt = input()

ind = 0

for i in range(len(txt) - 1):
    if txt[i] == txt [i + 1]:
        ind = 1
        break
print("YES" if ind == 1 else "NO")
    