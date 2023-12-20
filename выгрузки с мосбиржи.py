# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 16:25:09 2023

@author: S.Stycenkov
"""

import requests
import datetime
import pathlib
import apimoex
import pandas as pd

TICK = "SNGSP5"

with requests.Session() as session:
         data = apimoex.get_board_history(session, 'SBER',)
         df = pd.DataFrame(data)
         print(df)
         # to_csv("С:/files/qq2.txt".format(TICK))