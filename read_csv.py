# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:18:08 2023

@author: S.Stycenkov
"""

import csv
with open('C:\\files\ontrade.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)