# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:19:49 2022

@author: S.Stycenkov
"""


import pandas as pd
import matplotlib.pyplot as plt






df = pd.read_csv('C:\\files\marketdata\slv.csv', delimiter=',', dtype={'<DATE>': str, '<TIME>': str})

#df.set_index('<DATE>', inplace = True)
#print(df)

closeprice=df['<CLOSE>']
tradetime=df['<TIME>']
datamassive=df['<DATE>']


newdatamassive = datamassive + tradetime

realdata = pd.to_datetime(newdatamassive, format='%Y%m%d%H%M%S')



plt.rcParams['font.size'] = '8'
plt.figure(figsize=(12,4))
plt.ylabel('Цена, USD за тр.унцию', fontsize=10)
plt.grid(color = 'gray', linestyle = ':')
plt.title('Серебро (ticker: SILV)', fontsize=12)
plt.xlim(realdata[0], realdata[len(datamassive)-1])
plt.ylim(0.99*closeprice.min(),1.01*max(closeprice))

#print(realdata.head(20))
#print("MAX", closeprice.max())

plt.plot(realdata, closeprice, fillstyle='top')
plt.fill_between(realdata, closeprice, color="gray", alpha=0.1)
plt.show()