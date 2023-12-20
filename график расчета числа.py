# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:58:39 2023

@author: S.Stycenkov
"""

from random import uniform
import matplotlib.pyplot as plt

N = 5000

R = 100

def squareprof(a,b, R):
    return a**2 + b**2<=R**2


plt.figure(figsize=(35,20))



# x = [uniform(-R, R) for i in range(N)]
# y = [uniform(-R, R) for i in range(N)]

# plt.vlines(-R, -R, R, color='silver')
# plt.hlines(-R, -R, R, color='silver')
# plt.hlines(R, -R, R, color='silver')
# plt.plot(x,y, 'ro', color='c', markersize = 3)


# print(max(x), max(y))

yy=[]

 
total=0

for i in range(1, N + 1):
    x = uniform(-R, R)
    y = uniform(-R, R)
    if squareprof(x, y, R):
        total += 1
        yy.append(4*total/i)
        

    
xx = [i for i in range(len(yy))]



plt.plot(xx, yy, 'ro', color='c', markersize = 5)

plt.hlines(3.141592654, 0, len(yy), color='silver', lw=5)

# plt.plot(nonx,nony, 'ro', color='silver', markersize = 3)


# print(0.5*max(yy) + 0.5* min(yy))

plt.text(len(xx)/2, 0.5*max(yy) + 0.5* min(yy), 4*len(xx)/N, fontsize=38, color='white', backgroundcolor='deepskyblue')

plt.show()

# print(len(nonx), len(xx))