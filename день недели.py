# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:58:16 2023

@author: S.Stycenkov
"""

import datetime as dtm

a = dtm.datetime.now().replace(microsecond=0)
print(a)
print(a.weekday())