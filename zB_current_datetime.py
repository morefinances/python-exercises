# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:54:26 2023

@author: S.Stycenkov
"""

from datetime import datetime
current_datetime = datetime.now()
print(str(current_datetime.day) + "." + str(current_datetime.month) + "." + str(current_datetime.year)+"_" + str(current_datetime.hour) + ":" +  str(current_datetime.minute) + ":" + str(current_datetime.second)) 