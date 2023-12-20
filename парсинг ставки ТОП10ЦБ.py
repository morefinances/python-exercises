# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:11:05 2023

@author: S.Stycenkov
"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL_TEMPLATE = "https://www.cbr.ru/statistics/avgprocstav/"
r = requests.get(URL_TEMPLATE)
# print(r.text)

soup = bs(r.text, "html.parser")
vacancies_names = soup.find_all('table', class_='data')

for name in vacancies_names:
    print(name.text[2:80])
     