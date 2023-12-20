# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:49:42 2023

@author: S.Stycenkov
"""

l = list("abbbccccddefxx")

print(l)

m = list(set(l))
m.sort()
print(m)

print(len(l))
for i in range(len(m)):
    print(m[i], l.count(m[i]))