# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:05:11 2023

@author: S.Stycenkov
"""

import matplotlib.pyplot as plt
import squarify # pip install squarify (algorithm for treemap)
 
# Change color
squarify.plot(sizes=[13,22,35,5], label=["group A", "group B", "group C", "group D"], color=["red","green","blue", "grey"], alpha=.3 )
plt.axis('off')
plt.show()