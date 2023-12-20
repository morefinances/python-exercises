# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:58:39 2023

@author: S.Stycenkov
"""

from random import randint
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))

for i in range(100):
    x = [randint(0,100), randint(0,100)]
    y = [randint(0,100), randint(0,100)]
    plt.plot(x,y)

print(x, y)