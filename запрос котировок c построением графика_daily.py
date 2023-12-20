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
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

# dictdata=json.dumps(data, sort_keys=True, indent=4)
# dictdata2=json.loads(dictdata)

 
# #print(dictdata2)
# dataset=dictdata2['Time Series (5min)']
dataset=data[list(data.keys())[1]]

dfdata=pd.DataFrame.from_dict(dataset, orient='index')
#print(dfdata)
closeprice=dfdata['4. close']
closeprice2=pd.to_numeric(closeprice)
dd = pd.Series(list(reversed(closeprice2)))

closeprice3=closeprice2
closeprice3['4. close']=dd.values
print(closeprice3)



#print(dd)

# listdata=dfdata.index

# #time=pd.Series([i for i in range(100)])

plt.figure(figsize=(12,4))
#plt.axes()
plt.plot(dd)
plt.yticks(np.arange(int(min(closeprice2)) - 1, int(max(closeprice2)) + 2, step = 5))
plt.xticks(np.arange(0, 110, step=20), list(dfdata.index))
axes.set_xticklabels(dfdata.index)
# #формат оси: ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
plt.show()
print(dfdata.index)
