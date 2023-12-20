# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:29:40 2023

@author: S.Stycenkov
"""
import datetime as dttm
import time
import matplotlib.pyplot as plt

a = dttm.datetime.now()
print('\nстарт работы скрипта:', a)
X, Y = [], []

for z in range(1, 8):
    X.append(z)
    print(z, '-'*z + ' / ', end = '')
    index = 0
    N = 10**z
    for i in range(N):
        b = str(i)
        # print(b[:1])
        for u in range(len(b)-1):
            if b[u:u+1] == b[u+1:u+2]:
                # print(b)
                index += 1
    Y.append(index/N)
    timenow = dttm.datetime.now()
    if timenow.second<10:
        hh = "0"
    else:
        hh =""
    if timenow.minute<10:
        h = "0"
    else:
        h = ""
    print(index/N, ' / ', str(timenow.hour) + ":" + h + str(timenow.minute) + ":" + hh + str(timenow.second))
print(*Y)
b = dttm.datetime.now()
print('\nзавершение работы скрипта:', b)
print('всего времени работы:', b-a, 'сек.')

plt.figure(figsize=(10,10))
plt.plot(X, Y, 'o-')
plt.grid(linestyle='-', linewidth=1, alpha=0.5)
plt.grid(which='minor', linestyle='--', linewidth=1, alpha=0.3)
plt.show()

for i in range(len(Y)-1):
    print(i, ": ", Y[i+1]-Y[i])