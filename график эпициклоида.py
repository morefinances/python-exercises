# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:31:52 2023

@author: S.Stycenkov
"""

import matplotlib.pyplot as plt
import math

plt.figure(figsize=(8,8))
plt.rcParams['font.size'] = '8'
plt.xlabel('', fontsize=10)
plt.ylabel('', fontsize=10)

R = 35
r = 10
h = 10
m = r / R

N = 2800 # 360 - для минимального

xx = [
      R * (m + 1) * math.cos(m * i * math.pi / 180) - h * math.cos((m + 1) * i * math.pi / 180)
      for i in range(N)
]

yy = [
      R * (m + 1) * math.sin(m * i * math.pi / 180) - h * math.sin((m + 1) * i * math.pi / 180) 
      for i in range(N)
]
# yy2 = [-(50**2-y**2)**0.5 for y in xx]
#print(xx)

plt.plot(xx, yy, ls='None', marker='o', ms=3, mfc='b', alpha=0.1, mew=0)
# plt.plot(xx, yy2, ls='None', marker='o', ms=3, mfc='b', alpha=0.5, mew=0)

plt.show()