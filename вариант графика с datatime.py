
import pandas as pd
import matplotlib.pyplot as plt






df = pd.read_csv('C:\\files\OFS.csv', delimiter=',')

#df.set_index('<DATE>', inplace = True)
#print(df)

closeprice=df['<CLOSE>']
tradetime=df['<TIME>'].astype(str)
datamassive=df['<DATE>'].astype(str)


newdatamassive = datamassive + tradetime

realdata = pd.to_datetime(newdatamassive, format='%Y%m%d%H%M%S')



plt.rcParams['font.size'] = '8'
plt.figure(figsize=(12,4))
plt.ylabel('Цена, USD за тр.унцию', fontsize=10)
plt.grid(color = 'gray', linestyle = ':')
plt.title('Серебро (ticker: SILV)', fontsize=12)
plt.xlim(realdata[0], realdata[len(datamassive)-1])
plt.ylim(0.99*closeprice.min(),1.01*max(closeprice))

print(realdata.head(20))
#print("MAX", closeprice.max())

plt.plot(realdata, closeprice, fillstyle='top')
plt.fill_between(realdata, closeprice, color="gray", alpha=0.1)
plt.show()



'''

#print(tradetime.head(5))

for i in range(len(datamassive)):
    day=int(str(datamassive[i])[6:8])
    month=int(str(datamassive[i])[4:6])
    year = int(str(datamassive[i])[0:4])
    hour = int(tradetime[i]/10000)
    min=int((tradetime[i]-hour*10000)/100)
    #print(hour, min, tradetime[i])
    datamassive[i]=datetime.datetime(year, month, day, hour, min)


plt.rcParams['font.size'] = '8'
plt.figure(figsize=(12,4))
plt.ylabel('Цена, USD за тр.унцию', fontsize=10)
plt.grid(color = 'gray', linestyle = ':')
plt.title('Серебро (ticker: SILV)', fontsize=12)
plt.xlim(datamassive[0], datamassive[len(datamassive)-1])
plt.ylim(0.99*closeprice.min(),1.01*max(closeprice))

print(datamassive.head(10))
print("MAX", closeprice.max())

plt.plot(datamassive, closeprice, fillstyle='top')
plt.fill_between(datamassive, closeprice, color="gray", alpha=0.1)
plt.show()


'''
