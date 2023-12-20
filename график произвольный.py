# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:31:52 2023

@author: S.Stycenkov
"""

import matplotlib.pyplot as plt
import math

plt.figure(figsize=(8,8))
plt.rcParams['font.size'] = '8'
plt.xlabel('x', fontsize=10)
plt.ylabel('y', fontsize=10)

R = 50

N = 360 # 360 - для минимального

xx = [R*math.cos(i*3.14152654/180) for i in range(N)]
yy = [R*math.sin(i*3.14152654/180) for i in range(N)]
# yy2 = [-(50**2-y**2)**0.5 for y in xx]
print(xx)

plt.plot(xx, yy, ls='None', marker='o', ms=3, mfc='b', alpha=0.5, mew=0)
# plt.plot(xx, yy2, ls='None', marker='o', ms=3, mfc='b', alpha=0.5, mew=0)

plt.show()