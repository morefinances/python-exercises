# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:58:39 2023

@author: S.Stycenkov
"""

from random import uniform
import matplotlib.pyplot as plt

N = 10000

R = 100

def squareprof(a,b, R):
    return a**2 + b**2<=R**2


plt.figure(figsize=(20,20))



x = [uniform(0, R) for i in range(N)]
y = [uniform(0, R) for i in range(N)]

plt.vlines(0, 0, R, color='silver')
plt.vlines(R, 0, R, color='silver')
plt.hlines(0, 0, R, color='silver')
plt.hlines(R, 0, R, color='silver')
# plt.plot(x,y, 'ro', color='c', markersize = 3)


# print(max(x), max(y))

xx=[]
yy=[]

nonx=[]
nony=[]

total=[]

for i in range(N):
    if squareprof(x[i], y[i], R):
        xx.append(x[i])
        yy.append(y[i])
    else:
        nonx.append(x[i])
        nony.append(y[i])
    
# plt.plot(total, 'ro', color='c', markersize = 5)
plt.plot(xx,yy, 'ro', color='c', markersize = 5)
plt.plot(nonx, nony, 'ro', color='silver', markersize = 5)

plt.text(R/2, R/2, 4*len(xx)/N, fontsize=35, color='black')

plt.show()

# print(len(nonx), len(xx))