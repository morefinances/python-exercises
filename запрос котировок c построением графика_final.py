# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 11:15:39 2022

@author: S.Stycenkov
"""

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
closeprice2=pd.to_numeric(closeprice)
dd=list(reversed(closeprice))

clprlist=list(closeprice)

listdata=dfdata.index

#time=pd.Series([i for i in range(100)])

plt.figure(figsize=(12,4))
#plt.axes()
plt.plot(closeprice2)
plt.yticks(np.arange(139.5,143, step=0.5))
plt.xticks(np.arange(0,110,step=20))
#формат оси: ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
plt.show()
print(data)
