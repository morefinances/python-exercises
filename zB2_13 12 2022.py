'''
import pandas as pd

import matplotlib.pyplot as plt


data = {
    "quant": [400, 200, 500, 100, 200, 500],
    "duration": [10, 20, 30, 40, 50, 60]
}

df=pd.DataFrame(data)

print(df['duration'])

plt.xlabel('quant')
plt.ylabel('duration')
plt.scatter(x=data['duration'], y=data['quant'])
plt.show()


import pandas as pd
mydata= pd.Series([2,-5, 8, -9, 12,-15])
print(mydata)

#mydata[[0,2,3]]=0
print(mydata[mydata > 0 ])

for i in range(len(mydata)):
    if mydata[i] < 0:
        print(mydata[i])


#график с 3 вариантами гистограммы
import pandas as pd
import matplotlib.pyplot as plt
import math

#генерация массива значений
my1 = [ x for x in range(1,3000) ]
my2= [ 25*math.cos(x*3.141592654/180)*(x**2) for x in my1 ]
mydataX = pd.Series(my1)
mydataY = pd.Series(my2)
#print(mydataY[mydataY%3 > 0])

#plt.plot(my1, my2)
#plt.show()



#plt.hist(mydataY, color="steelblue", label="one")
#plt.show()

plt.hist(mydataY,  alpha=0.5, stacked=True)
plt.show()

plt.hist(mydataY, bins=50,  alpha=0.5, histtype='stepfilled', color="steelblue", edgecolor='none')
plt.show()

plt.hist(mydataY, bins=50, histtype='step')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import math

#генерация массива значений
my1 = [ x for x in range(1,500) ]
my2= [ 3*math.cos(x*3.141592654/180)*(x**0.5) for x in my1 ]
mydataX = pd.Series(my1)
mydataY = pd.Series(my2)
#print(mydataY[mydataY%3 > 0])

#plt.plot(my1, my2)
#plt.show()



#plt.hist(mydataY, color="steelblue", label="one")
#plt.show()

#plt.hist(mydataY,  alpha=0.5, stacked=True)
#plt.show()

plt.figure(figsize=(10,6))
plt.xlabel('ось икс')
plt.ylabel('ось игрек')
plt.grid(color = 'gray',
        linestyle = ':') #axis = 'x' - только икс
plt.title('Распределение')

plt.hist(mydataY, bins=50,  alpha=0.5, histtype='stepfilled', color="steelblue", edgecolor='none')
plt.show()

#plt.hist(mydataY, bins=50, histtype='step')
#plt.show()





import pandas as pd
import matplotlib.pyplot as plt
import math

#генерация массива значений
my1 = [ x for x in range(1,5000) ]
my2= [ 3*math.sin(x/1000)*math.cos(x/200) for x in my1 ]
mydataX = pd.Series(my1)
mydataY = pd.Series(my2)

plt.figure(figsize=(10,6))
plt.xlabel('ось икс')
plt.ylabel('ось игрек')
plt.grid(color = 'gray',
        linestyle = ':') #axis = 'x' - только икс

plt.title('Распределение')

#plt.hist(mydataY, bins=50,  alpha=0.5, histtype='stepfilled', color="steelblue", edgecolor='none')
plt.plot(my1, my2)
plt.show()




import pandas as pd
mydata= pd.Series([2,-5.1, 8, -9.3, 12,-15])
print(mydata)

#mydata[[0,2,3]]=0
print(mydata[mydata < 0 ])

for i in range(len(mydata)):
    if mydata[i] < 0:
        print(mydata[i])

for i in range(5):
    print(df.iloc[i][7])
    print("-----"*5)


for i in range(len(datamassive)):
    if int(str(datamassive[i])[5:6])<10:
        month="0" + str(datamassive[i])[5:6]
    else:
        month = str(datamassive[i])[5:6]
    if int(str(datamassive[i])[7:8])<10:
        day="0"+str(datamassive[i])[7:8]
    else:
        day=str(datamassive[i])[7:8]
    datamassive[i]= str(datamassive[i])[0:4] + "-" + month + "-" + day








#---- начало скрипта
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import datetime





df = pd.read_csv('C:\\files\marketdata\slv.csv', delimiter=',')

#df.set_index('<DATE>', inplace = True)
#print(df)

closeprice=df['<CLOSE>']
tradetime=df['<TIME>']
datamassive=df['<DATE>']


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
#plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(12,4))
#plt.xlabel('Даты')
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

print(datetime.strptime(datamassive[0], '%m/%d/%y'))


#корректyй перевод формат дат
from datetime import datetime

a = 20221128
c = 163000
print(a, c)
print(str(a) + " " +str(c))

b=datetime.strptime(str(a) + " " +str(c),"%Y%m%d %H%M%S")
#b=datetime.strptime(str(c),"%H%M%S")
print(b)


'''
