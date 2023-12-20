# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:48:43 2023

@author: S.Stycenkov
"""
import numpy as np
import matplotlib.pyplot as plt


def circle(x):
    return (100**2-(x**2))**0.5
def CX(x):
    return x



plt.figure(figsize=(12,12))
plt.grid(linestyle='-', linewidth=1, alpha=0.5)
plt.margins(x=0.01, y = 0.01)

# X = [i for i in range(-100, 100)]
X = np.arange(-100, 100, 0.01)

Y = [circle(i) for i in X]
Y2 = [-circle(i) for i in X]

print(circle(0))
print(100**.5)

plt.plot(X, Y, 'o', color = '#1F77B4', ms = 2)
plt.plot(X, Y2, 'o', color = '#1F77B4', ms = 2)

plt.show()