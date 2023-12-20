# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:02:19 2023

@author: S.Stycenkov
"""
# ввод координат в одну строчку через пробел
b = [int(i) for i in list(input().split())]

# расчет квадрата расстояния
t = (b[0]-b[2])**2 + (b[1]-b[3])**2

if t=5:
    print("YES")
else:
    print("NO")