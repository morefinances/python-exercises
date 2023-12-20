# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:54:22 2023

@author: S.Stycenkov
"""

import matplotlib.pyplot as plt
import csv

X = []
Y = []

with open('C:\\files\\OFS.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=';')
    
    for ROWS in plotting:
        X.append(float(ROWS[1]))
        Y.append(float(ROWS[3]))

plt.plot(X, Y)
plt.title('Line Graph using CSV')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()