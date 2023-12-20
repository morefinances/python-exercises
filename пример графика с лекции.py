# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:00:48 2023

@author: S.Stycenkov
"""
import matplotlib.pyplot as plt

def f_x(x):
   y = x ** 3 - 6 * x ** 2 +  x + 5
   return y

a = -2
b = 6
n = 100
h = (b-a)/(n-1)

x_list = [a + h * i for i in range(n)]

f_list = [f_x(x) for x in x_list]

line = plt.plot(x_list, f_list)
plt.setp(line, color="blue", linewidth=2)

plt.gca().spines["left"].set_position("zero")

plt.gca().spines["bottom"].set_position("zero")

plt.gca().spines["top"].set_visible(False)

plt.gca().spines["right"].set_visible(False)

plt.show()