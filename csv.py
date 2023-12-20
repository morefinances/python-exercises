# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:33:39 2023

@author: S.Stycenkov
"""

import csv
with open('C:\\files\command.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows('t')