# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:42:43 2023

@author: S.Stycenkov
"""
import datetime as dtm

t1 = dtm.datetime.now()
lasttime = dtm.datetime.now()

print(t1)

Nexp = 5
maxnumb = -1 + 10**Nexp
totalsum = 0

halfA = [ i for i in range(10**Nexp)]
halfB = [ i for i in range(10**Nexp)]

for ii in halfA:
    i = str(ii)
    sum_a = 0
    for u in range(len(i)):
        sum_a += int(i[u])
    for jj in halfB:
        j = str(jj)
        sum_b = 0
        for x in range(len(j)):
            sum_b += int(j[x])
            if sum_b>sum_a:
                break
        if sum_a == sum_b:
            totalsum += 1
    if ii % 100 == 0: 
        print('{:05d}'.format(ii),  ': ', end='')
        time = dtm.datetime.now()
        print('{:12d}'.format(totalsum), ' / ', time - lasttime)
        lasttime = time
        
    # print(ii,': ',sum_a)
t2 = dtm.datetime.now()
print(t2)
print('totalsum = ', totalsum)
print('Время работы скрипта:', t2-t1)