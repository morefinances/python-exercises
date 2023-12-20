# -*- coding: utf-8 -*-
"""
Created on Tue May 23 10:26:38 2023

@author: S.Stycenkov
"""

x = float(input())/float(input())
if 18.5<x<=25: 
    y = "Оптимальная масса"
elif x<18.5:
    y = "Недостаточная масса"
else:
    y = "Избыточная масса"

print(y)

# альтернативное решение
# i = float(input()) / float(input()) ** 2
# print([['Оптималь', 'Недостаточ'][i < 18.5], 'Избыточ'][ i > 25] + 'ная масса')