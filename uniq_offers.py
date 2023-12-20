# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:47:37 2023

@author: S.Stycenkov
"""

import pandas as pd

file = "C:\\files\\tickers_for_work.csv"
offers = pd.read_csv(file, delimiter=';')


uniq_offers = []

for i in range(len(offers.columns)):
    if "." not in offers.columns[i]:
        uniq_offers.append(offers.columns[i])

print(uniq_offers)