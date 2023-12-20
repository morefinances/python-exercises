# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:05:11 2023

@author: S.Stycenkov
"""

import matplotlib.pyplot as plt
import squarify # pip install squarify (algorithm for treemap)
 
 
 


# Change color
size_one = [43588329451, 9279307154, 7024189810, 6546090798, 3464378551, 3385643940, 3207664984, 3117265120, 2990553134, 2667701042, 2342680814, 2159204627, 2047272350, 2016556954, 1973535230, 1959003447, 1913514231, 1882979609, 1851749763, 1794734348, 1777258706, 1621673162, 1607975994, 1600672415, 1598520472, 1423587959, 1348120797, 1315026382, 1311379851, 1309218230, 1301699268, 1223499404, 1190249804, 1183485317, 1133718771, 1123559672, 1014301605, 957025355, 854120354, 767882893, 764057424, 748761777, 702123875, 633431000, 615280881, 556443633, 531417551, 504392055, 469156478, 434431874
]

label_one = ["SBER", "LKOH", "GAZP", "VTBR", "TRMK", "GMKN", "SBERP", "TCSG", "FEES", "YNDX", "MGNT", "SNGSP", "TRNFP", "MTLR", "FESH", "ROSN", "RNFT", "MTSS", "PLZL", "VKCO", "TATN", "NLMK", "ALRS", "RUAL", "FLOT", "FIVE", "MAGN", "GEMC", "CHMF", "NVTK", "AFKS", "SGZH", "PHOR", "GLTR", "SMLT", "OZON", "MOEX", "SPBE", "SIBN", "MRKP", "UPRO", "SNGS", "IRAO", "AFLT", "BELU", "RASP", "ELFV", "MRKS", "NMTP", "GTRK"]

squarify.plot(sizes=size_one, label=label_one, color=["red","green","blue", "grey", "red","green","blue", "grey", "red","green","blue"], alpha=.3 )

plt.axis('off')
plt.show()
 