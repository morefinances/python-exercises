# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:31:52 2023

@author: S.Stycenkov
"""

import matplotlib.pyplot as plt
import math

def myint(x):
    return x - int(x) == 0



R = 10
r = 10
h = 10




a = [[0] * 15 for i in range(15)] 


x = 0
xx = 0

for R in range(10, 25): #(5, 100, 5):
    for r in range(5, 20):
        m = r / R
        N=10000
        if R/r != 1 and R/r != 2 and R/r != 1.5 and R/r != 3 and R/r != 4/3:
            plt.figure(figsize=(8,8))
            plt.rcParams['font.size'] = '8'
            plt.xlabel('', fontsize=10)
            plt.ylabel('', fontsize=10)
            # plt.text(0,0, str(R) + ":" + str(r))
            zz = [
                R * (m + 1) * math.cos(m * i * math.pi / 180) - h * math.cos((m + 1) * i * math.pi / 180)
                for i in range(N)
                ]
            yy = [
                R * (m + 1) * math.sin(m * i * math.pi / 180) - h * math.sin((m + 1) * i * math.pi / 180)
                for i in range(N)
                ]
            # print(*zz)
            # print(*yy)
            plt.plot(zz, yy, ls='None', marker='o', ms=3, mfc='b', alpha=0.1, mew=0)
            plt.show()