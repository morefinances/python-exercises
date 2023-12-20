# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 11:15:39 2022

@author: S.Stycenkov
"""

import requests
import json
import pandas as pd

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()

dictdata=json.dumps(data, sort_keys=True, indent=4)
dictdata2=json.loads(dictdata)

 
#print(dictdata2)
dataset=dictdata2['Time Series (5min)']
dfdata=pd.DataFrame.from_dict(dataset, orient='index')
closeprice=dfdata['4. close']
print(closeprice)

# print(extra)

# for i in r:
#     print(i)
#     x=input()
    

 
#df = pd.json_normalize(data)
#print(df)