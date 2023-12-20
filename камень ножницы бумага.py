# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:32:25 2023

@author: S.Stycenkov
"""

def KNB(Timur, Ruslan): 
    winT="Тимур"
    winR="Руслан"
    winN="ничья"
    if Timur==Ruslan:
        return winN
    if Timur == 3 * Ruslan:
        return winT
    if Ruslan == 3 * Timur:
        return winR
    if Ruslan<Timur:
        return winR
    else:
        return winT

Timur = int(input('Выбор Тимура: 1 - камень, 2 - ножницы, 3 - бумага: '))
Ruslan = int(input('Выбор Руслана: 1 - камень, 2 - ножницы, 3 - бумага: '))

print(KNB(Timur, Ruslan))

# ____________________
# x, y = input(), input()
# var = ['камень', 'ножницы', 'бумага']
# ans = ['ничья', 'Руслан', 'Тимур']
# print(ans[var.index(x) - var.index(y)])

# ________________________

# print(['ничья', 'Тимур', 'Руслан'][input().count('а') - input().count('а')])