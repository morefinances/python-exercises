# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 18:03:00 2023

@author: S.Stycenkov
"""

a = "0123456789"

b = "s.tr12d3"

txt = ""

for i in b:
    if i in a:
        txt += i

print(txt)