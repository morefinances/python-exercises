# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:58:39 2023

@author: S.Stycenkov
"""

from random import randint
import matplotlib.pyplot as plt

N = 1000

def squareprof(a,b, R):
    return a**2 + b**2<=R**2


plt.figure(figsize=(10,10))



x = [randint(-N, N) for i in range(N)]
y = [randint(-N, N) for i in range(N)]

plt.vlines(-N, -N, N, color='silver')
plt.vlines(N, -N, N, color='silver')
plt.hlines(-N, -N, N, color='silver')
plt.hlines(N, -N, N, color='silver')
# plt.plot(x,y, 'ro', color='c', markersize = 3)


print(max(x), max(y))

xx=[]
yy=[]

nonx=[]
nony=[]

for i in range(N):
    if squareprof(x[i], y[i], N):
        xx.append(x[i])
        yy.append(y[i])
    else:
        nonx.append(x[i])
        nony.append(y[i])

plt.plot(xx, yy, 'ro', color='c', markersize = 5)
# plt.plot(x,y, 'ro', color='silver', markersize = 2)
plt.plot(nonx,nony, 'ro', color='silver', markersize = 3)

plt.text(-N/2, 0, len(xx)/len(nonx), fontsize=25, color='gray')

plt.show()

print(len(nonx), len(xx))