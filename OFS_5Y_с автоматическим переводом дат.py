
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def findday():
    current_datetime = datetime.now()
    year = str(current_datetime.year - 2001)
    if current_datetime.day < 10:
        day = '0' + str(current_datetime.day)
    else:
        day = str(current_datetime.day)
    if current_datetime.month < 10:
        month = '0' + str(current_datetime.month)
    else:
        month = str(current_datetime.month)
    find_date = year + month + day
    print(find_date)
    # print(find_date)
    for i in range(len(datamassive) - 1):
        a = str(datamassive[i]).replace('.','')
        b = str(datamassive[i + 1]).replace('.','')
        aa = a[4:] + a[2:4] + a[:2]
        bb = b[4:] + b[2:4] + b[:2]
        
        if int(aa) <= int(find_date) and int(bb) > int(find_date):
            return(i)


def newdata(x):
    return (str(x)[:6] + str(x)[-2:])

def currenttime():
    current_datetime = datetime.now()
    
    year = str(current_datetime.year)
    
    if current_datetime.day < 10:
        day = '0' + str(current_datetime.day)
    else:
        day = str(current_datetime.day)

    if current_datetime.month < 10:
        month = '0' + str(current_datetime.month)
    else:
        month = str(current_datetime.month)
        
    if current_datetime.hour < 10:
        hour = '0' + str(current_datetime.hour)
    else:
        hour = str(current_datetime.hour)
        
    if current_datetime.minute < 10:
        minute = '0' + str(current_datetime.minute)
    else:
        minute = str(current_datetime.minute)
        
    if current_datetime.second < 10:
        second = '0' + str(current_datetime.second)
    else:
        second = str(current_datetime.second)
        
    return day + month + year + '_' + hour + minute + second


df = pd.read_csv('C:\\files\\OFS_DAY.csv', delimiter=';') #OFS_DAY


list_column = df.columns.values.tolist ()
df['average'] = df[list_column[3:]].mean (axis= 1 )
closeprice=df['average']
# dtmassive=df['<DATE>'].astype(str)
datamassive = df['<DATE>'].apply(newdata)

# print(datamassive)


plt.figure(figsize=(15,5))
plt.plot(datamassive, closeprice, linewidth=3)

# plt.gcf().autofmt_xdate()
# myFmt = mdates.DateFormatter('%dd.%mm.%YY')
# plt.gca().xaxis.set_major_formatter(myFmt)
# plt.locator_params (axis='x', nbins= 10 )

plt.xticks(np.arange(0, 1001, 100))
# plt.ylabel('Цена', fontsize=10)

plt.grid(linestyle='-', linewidth=1, alpha=0.5)
# plt.grid(linestyle='-', which='both', linewidth=1, alpha=0.3)

margins = {                                            
    "left"   : 0.030,
    "bottom" : 0.060,
    "right"  : 0.992,
    "top"    : 0.990   
}

plt.subplots_adjust(**margins)   
plt.margins(x=0.01) #убрать отступы
plt.legend(title='5-летняя динамика котировок облигаций, входящих в RGBI')

filename = currenttime()



font = {' family ': 'Tahoma',
 'color ': ' red',
 'weight ': ' bold',
 'size ': 20
 }

start_OFS = closeprice[0]
plt.text(1, start_OFS - 3, round(start_OFS,2), size=17, color = '#1F77B4')

finish_OFS = closeprice[len(closeprice)-1]
plt.text(len(datamassive) - 63, finish_OFS - 4, round(finish_OFS,2), size=17, color = '#1F77B4')
 #color='#11aa55'

result = 100*(finish_OFS-start_OFS)/start_OFS

if result > 0:
    plt.text(len(datamassive)-60, finish_OFS + 3, "+" + str(round(result,2)) + " %", size=16, color = '#11aa55', weight='bold')
else:
    plt.text(len(datamassive) - 73, 110, str(round(result,2)) + "%", size=16, color = 'k', alpha = 0.6, weight='bold')





maxloc = closeprice.idxmax()
plt.text(maxloc + 10, round(closeprice.max(),2) - 1, round(closeprice.max(),2), size=17, color = '#1F77B4')

minloc = closeprice.idxmin()

plt.text(minloc + 10, round(closeprice.min(),2) - 0.6, round(closeprice.min(),2), size=17, color = '#1F77B4')

pointX = [0, len(datamassive) - 1, minloc, maxloc]
pointY = [start_OFS, finish_OFS, round(closeprice.min(),2), round(closeprice.max(),2)]

plt.plot(pointX, pointY, 'o', color = 'k', ms = 6)
plt.plot(pointX, pointY, 'o', color = 'w', ms = 3)

# print(findday(), '--')

dh = closeprice.max() - closeprice.min()
dh2 = dh/2
dh4 = dh/4
 
# print(dh)
median = closeprice.min() + dh2
stohast25 = closeprice.min() + dh4
stohast75 = closeprice.max() - dh4
stohast10 = closeprice.min() + dh/10
stohast90 = closeprice.max() - dh/10


plt.axhline(y=median, color='k', alpha = 0.5, linestyle='-', linewidth=1)
plt.text(len(datamassive)/2, median - 0.5, round(median,2), size=11, color = 'k')

plt.axhline(y=stohast25, color='#1F77B4', linestyle='--', linewidth=1)
plt.text(len(datamassive)/2, stohast25 - 0.5, round(stohast25,2), size=11, color = 'k')


plt.axhline(y=stohast75, color='#1F77B4', linestyle='--', linewidth=1)
plt.text(len(datamassive)/2, stohast75 - 0.5, round(stohast75,2), size=11, color = 'k')

plt.axhline(y=stohast10, color='#1F77B4', linestyle='--', linewidth=1)
plt.text(len(datamassive)/2, stohast90 - 0.5, round(stohast90,2), size=11, color = 'k')

plt.axhline(y=stohast90, color='#1F77B4', linestyle='--', linewidth=1)
plt.text(len(datamassive)/2, stohast10 - 0.5, round(stohast10,2), size=11, color = 'k')

plt.savefig('C:\\files\\pctrs\\5Y_' + filename + '.png')
plt.savefig('C:\\files\\pctrs\\OFS_ALL_DAY.png')

plt.show()






 
 
  