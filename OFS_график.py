
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
import matplotlib.dates as mdates





df = pd.read_csv('C:\\files\\OFS.csv', delimiter=';')

#df.set_index('<DATE>', inplace = True)
#print(df)

print(df)
closeprice=df['SU26207RMFS9']
datamassive=df['<DATE>']



plt.figure(figsize=(12,5))
plt.plot(datamassive, closeprice)
# plt.gcf().autofmt_xdate()
# myFmt = mdates.DateFormatter('%dd.%mm.%YY')
# plt.gca().xaxis.set_major_formatter(myFmt)
# plt.locator_params (axis='x', nbins= 10 )

plt.xticks(np.arange(0, 1000, 200))
plt.ylabel('Цена', fontsize=10)

# myFmt = mdates.DateFormatter('%dd.%mm.%YY')

# plt.gcf().autofmt_xdate()
# plt.gca().xaxis.set_major_formatter(myFmt)
# plt.locator_params (axis='x', nbins= 10 )
plt.show()

 
# newdatamassive = datamassive + tradetime

# realdata = pd.to_datetime(newdatamassive, format='%Y%m%d%H%M%S')



# plt.rcParams['font.size'] = '8'
# plt.figure(figsize=(12,4))
# plt.ylabel('Цена, USD за тр.унцию', fontsize=10)
# plt.grid(color = 'gray', linestyle = ':')
# plt.title('Серебро (ticker: SILV)', fontsize=12)
# plt.xlim(realdata[0], realdata[len(datamassive)-1])
# plt.ylim(0.99*closeprice.min(),1.01*max(closeprice))

# print(realdata.head(20))
# #print("MAX", closeprice.max())

# plt.plot(realdata, closeprice, fillstyle='top')
# plt.fill_between(realdata, closeprice, color="gray", alpha=0.1)
# plt.show()



# '''

# #print(tradetime.head(5))

# for i in range(len(datamassive)):
#     day=int(str(datamassive[i])[6:8])
#     month=int(str(datamassive[i])[4:6])
#     year = int(str(datamassive[i])[0:4])
#     hour = int(tradetime[i]/10000)
#     min=int((tradetime[i]-hour*10000)/100)
#     #print(hour, min, tradetime[i])
#     datamassive[i]=datetime.datetime(year, month, day, hour, min)


# plt.rcParams['font.size'] = '8'
# plt.figure(figsize=(12,4))
# plt.ylabel('Цена, USD за тр.унцию', fontsize=10)
# plt.grid(color = 'gray', linestyle = ':')
# plt.title('Серебро (ticker: SILV)', fontsize=12)
# plt.xlim(datamassive[0], datamassive[len(datamassive)-1])
# plt.ylim(0.99*closeprice.min(),1.01*max(closeprice))

# print(datamassive.head(10))
# print("MAX", closeprice.max())

# plt.plot(datamassive, closeprice, fillstyle='top')
# plt.fill_between(datamassive, closeprice, color="gray", alpha=0.1)
# plt.show()


# '''
