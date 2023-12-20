# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 13:56:01 2023

@author: S.Stycenkov
"""

firstword = ['Первая', 'Вторая', 'Третья', 'Четвертая']
quat = ' четверть: '
result = [0 for i in range(4)]

numstr= int(input())
coord = [[] for i in range(numstr)]

for i in range(numstr):
    coord[i] = input().split()
    if int(coord[i][0])>0 and int(coord[i][1])>0: result[0] +=1
    if int(coord[i][0])<0 and int(coord[i][1])>0: result[1] +=1
    if int(coord[i][0])<0 and int(coord[i][1])<0: result[2] +=1
    if int(coord[i][0])>0 and int(coord[i][1])<0: result[3] +=1

for i in range(4):
    print(firstword[i], quat, result[i], sep='')

# вариант разбивки по 2 переменным:
# x, y = map(int, input().split())

