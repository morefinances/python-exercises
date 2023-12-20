# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:44:56 2023

@author: S.Stycenkov
"""

import numpy as np
import matplotlib.pyplot as plt


rg = np.random.Generator(np.random.PCG64(5))

means = (0.5, 0.9)
covar = [
    [1., 0.6],
    [0.6, 1.]
]
data = rg.multivariate_normal(means, covar, 5000)
plt.figure(figsize=(10,10))
plt.grid(which='major') #основная метка
plt.grid(which='minor', linestyle=':')


plt.scatter(data[:,0], data[:,1], marker='o', s=1)
plt.show()