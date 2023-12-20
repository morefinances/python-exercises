# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 16:52:17 2023

@author: S.Stycenkov
"""

import random
import matplotlib.pyplot as plt
import math


def fin(X, xx, yy):
    for i in range(1, len(xx)):
        if X<xx[i]:
            return xx[i-1], xx[i], yy[i-1], yy[i]
            
N=10

a = [random.randint(-10,10) for i in range(N)]
b = [random.randint(10,100) for i in range(N)]

x=[0]
y=[0]

for i in range(1, len(a)):
    x.append(x[i-1] + b[i-1])
    y.append(y[i-1] + a[i-1])

print('x=', x)
print('y=' , y)

plt.figure(figsize=(20,10))
plt.plot(x,y, ls='None', marker='o', color='b', mfc='b', ms=5, alpha=0.2)






# print(fin(x[2]+1, x, y))

xA = [i for i in range(max(x))]


yA = [0]

for z in range(1, max(x)):
    A, B, C, D = fin(z, x, y)
    F = (D - C) * (z - A) / (B - A) + C
    # print(z, F) #(A,B,C,D)
    yA.append(F)



print(len(xA), len(yA), xA[-1], yA[-1])

plt.plot(xA, yA, color='b', mfc='b', ms=1, alpha=0.5)


wx = [0]
wy = [0]


print('max x= ', max(x), '| max y= ', max(y), '| min y= ', min(y))

wx.append(random.randint(int(0.1*max(x)), int(max(x)/2)))
wy.append(random.randint(min(y), max(y)))

wx.append(random.randint(int(max(x)/2), int(0.9*max(x))))
wy.append(random.randint(min(y), max(y)))

wx.append(x[-1])
wy.append(y[-1])


wA = [0]
totalY=[0]
for z in range(1, max(x)):
    A, B, C, D = fin(z, wx, wy)
    F = (D - C) * (z - A) / (B - A) + C
    # print(z, F) #(A,B,C,D)
    wA.append(F)
    totalY.append(yA[z] + wA[z])

# print(*wx, *wy)

plt.plot(wx, wy, ls='None', marker='o', color='g', mfc='b', ms=18, alpha=0.2)

plt.plot(xA, wA, color='b', mfc='b', ms=1, alpha=0.7)
plt.plot(xA, totalY, color='g', mfc='b', ms=10)


totalB = []
totalSM = [0]
for t in range(max(x)):
    totalB.append(0.5*totalY[t]*math.sin(t*3.141592654/180))
    if t==1 or t==0:
        totalSM.append(totalB[t])
    if t==2:
        totalSM.append(0.5*(totalB[t] + totalB[t-1]))
    if t>3:
        totalSM.append((totalB[t] + totalB[t-1] + totalB[t-2])/3)

print(len(totalSM))

# plt.plot(xA, totalB, color='k', mfc='b', ms=10)
plt.plot(xA, totalSM, color='g', mfc='b', ms=15)

plt.show()