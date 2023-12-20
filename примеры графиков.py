# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:54:27 2022

"""

import matplotlib.pyplot as plt

#рисует линию
#plt.plot((0, 1, 2, 3, 4, 5, 6, 7), (0, 3, 1, 2, 1, 5, 4, 0))

#рисует множество точек
#plt.scatter([0, 1, 2, 3, 4 , 5], [0, 1, 2, 3, 4 , 5], s=100)

sc=0
for i in range(1000):
    n = i ** 2
    if n%31==0:
        plt.scatter(i, n, s=12, marker="s", linewidth=0, c="b", alpha=0.9)
        print(sc+1, ": ", "\t", i)
        sc += 1

plt.show()


