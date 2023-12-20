
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
import matplotlib.dates as mdates


indexstart = 0

def renum(x):
    global indexstart
    if indexstart == 0:
        indexstart = x
        return 100
    else:
        a = 100*(x/indexstart)
        # indexstart = x
        return a


df = pd.read_csv('C:\\files\\OFS5.csv', delimiter=';')

#df.set_index('<DATE>', inplace = True)
#print(df)

list_column = df.columns.values.tolist ()
df['average'] = df[list_column[3:]].mean (axis= 1 )
# closeprice=df['average']
RGBIcurve=df['RGBI']
datamassive=df['<DATE>']

df['rgbi'] =  df['RGBI'].apply(renum)
indexstart = 0
closeprice = df['rgbi']
df['av'] =  df['average'].apply(renum)
AVERAGE_CURVE = df['av']

print(df)


plt.figure(figsize=(12,5))
plt.plot(datamassive, closeprice, color='k', alpha=0.5)

# plt.gcf().autofmt_xdate()
# myFmt = mdates.DateFormatter('%dd.%mm.%YY')
# plt.gca().xaxis.set_major_formatter(myFmt)
# plt.locator_params (axis='x', nbins= 10 )

plt.xticks(np.arange(0, 1001, 100))
# plt.ylabel('Цена', fontsize=10)

plt.grid(linestyle='-', linewidth=1, alpha=0.5)
# plt.grid(linestyle='-', which='both', linewidth=1, alpha=0.3)

margins = {                                            
    "left"   : 0.040,
    "bottom" : 0.060,
    "right"  : 0.990,
    "top"    : 0.990   
}

plt.subplots_adjust(**margins)   
plt.margins(x=0.00) #убрать отступы
plt.legend(title='сравнение динамики индекса  RGBI и портфеля входящих в него облигаций')
plt.plot(datamassive, AVERAGE_CURVE)
plt.show()

# plt.plot(datamassive, RGBIcurve, color='k')
# plt.show()
 
 
  