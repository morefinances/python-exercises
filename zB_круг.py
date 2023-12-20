# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:57:28 2023

@author: S.Stycenkov
"""

import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0, 2*np.pi, 0.01)
r = 4
plt.plot(r*np.sin(t), r*np.cos(t), lw=3)
plt.axis('equal')
plt.show()