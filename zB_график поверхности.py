# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:57:48 2023

@author: S.Stycenkov
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
ax = axes3d.Axes3D(plt.figure())
i = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(i, i)
Z = X**2 - Y**2
ax.plot_wireframe(X, Y, Z, rstride=20, cstride=20)
plt.show()