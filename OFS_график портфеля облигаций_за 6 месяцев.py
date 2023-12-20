
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
import matplotlib.dates as mdates
from datetime import datetime

def findday():
    current_datetime = datetime.now()
    year = str(current_datetime.year - 2000)
    if current_datetime.day < 10:
        day = '0' + str(current_datetime.day)
    else:
        day = str(current_datetime.day)
    if (current_datetime.month - 6) < 10:
        month = '0' + str(current_datetime.month-6)
    else:
        month = str(current_datetime.month-6)
    find_date = year + month + day
    # print(find_date)
    # print(current_datetime.day)
    for i in range(len(datamassive) - 1):
        a = str(datamassive[i]).replace('.','')
        b = str(datamassive[i + 1]).replace('.','')
        aa = a[4:] + a[2:4] + a[:2]
        bb = b[4:] + b[2:4] + b[:2]
        
        if int(aa) <= int(find_date) and int(bb) > int(find_date):
            print(aa, '/', bb, i)
            return(i)
        # print (int(str(datamassive[i]).replace('.','')), '/', int(find_date), '/', int(str(datamassive[i]).replace('.','')) <= int(find_date))
        # if str(datamassive[i]).replace('.','') <= find_date and str(datamassive[i + 1]).replace('.','') > find_date:
            # abc = 0
            # print(str(datamassive[i]))
            # print(str(datamassive[i+1]))


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


df = pd.read_csv('C:\\files\\OFS_DAY.csv', delimiter=';')

#df.set_index('<DATE>', inplace = True)
#print(df)

list_column = df.columns.values.tolist ()
df['average'] = df[list_column[3:]].mean (axis= 1 )
closeprice=df['average']
datamassive=df['<DATE>'].astype(str)

daystring = findday()
yeardatamassive = datamassive[daystring:]

yearcloseprice = closeprice[daystring:]
# print(yearcloseprice)

plt.figure(figsize=(12,5))
plt.plot(yeardatamassive, yearcloseprice)

# plt.gcf().autofmt_xdate()
# myFmt = mdates.DateFormatter('%dd.%mm.%YY')
# plt.gca().xaxis.set_major_formatter(myFmt)
# plt.locator_params (axis='x', nbins= 10 )

plt.xticks(np.arange(0, 1002 - daystring, (1001 - daystring)/10))
# print(np.arange(daystring, 1001, 22))
# plt.ylabel('Цена', fontsize=10)

plt.grid(linestyle='-', linewidth=1, alpha=0.5)
# plt.grid(linestyle='-', which='both', linewidth=1, alpha=0.3)

margins = {                                            
    "left"   : 0.025,
    "bottom" : 0.060,
    "right"  : 0.990,
    "top"    : 0.990   
}

plt.subplots_adjust(**margins)   
plt.margins(x=0.01) #убрать отступы
plt.legend(title='полугодовая динамика котировок облигаций, входящих в RGBI')

filename = currenttime()


 

start_OFS = closeprice[daystring]
plt.text(1, start_OFS - 0.6, round(start_OFS,2), size=17, color = '#1F77B4')

# print(yearcloseprice)
finish_OFS = yearcloseprice[len(closeprice)-1]
# print(finish_OFS)
plt.text(len(yeardatamassive) - 8, finish_OFS + 0.5, round(finish_OFS,2), size=17, color = '#1F77B4')
#  #color='#11aa55'

result = 100*(finish_OFS-start_OFS)/start_OFS

if result > 0:
    plt.text(len(yeardatamassive)-60, finish_OFS + 3, "+" + str(round(result,2)) + " %", size=16, color = '#11aa55', weight='bold')
else:
    plt.text(len(yeardatamassive) - 10, 87.3, str(round(result,2)) + "%", size=16, color = 'k', alpha = 0.6, weight='bold')



maxloc = yearcloseprice.idxmax()
plt.text(maxloc + 3 - daystring, round(yearcloseprice.max(),2) - 0.2, round(yearcloseprice.max(),2), size=17, color = '#1F77B4')

minloc = yearcloseprice.idxmin()

plt.text(minloc - daystring - 10, round(yearcloseprice.min(),2) - 0.2, round(yearcloseprice.min(),2), size=17, color = '#1F77B4')

pointX = [0, len(yeardatamassive) - 1, minloc - daystring, maxloc - daystring]
pointY = [start_OFS, finish_OFS, round(yearcloseprice.min(),2), round(yearcloseprice.max(),2)]

plt.plot(pointX, pointY, 'o', color = 'b', ms = 6, alpha=0.6)




plt.savefig('C:\\files\\pctrs\\6MN_' + filename + '.png')
plt.savefig('C:\\files\\pctrs\\OFS_6MN_DAY.png')

plt.show()






# plt.plot(datamassive, RGBIcurve, color='k')
# plt.show()
 
 
  