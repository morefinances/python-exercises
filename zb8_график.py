# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:54:12 2023

@author: S.Stycenkov
"""

import numpy as np
import matplotlib.pyplot as plt
plt.subplot(111, polar=True)
phi = np.arange(0, 4*np.pi, 0.01)
rho = phi**2
plt.plot(phi, rho, lw=3)
plt.show()