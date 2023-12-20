
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
        indexstart = x
        return a




df = pd.read_csv('C:\\files\\abc2.csv', delimiter=';')

#df.set_index('<DATE>', inplace = True)
#print(df)

list_column = df.columns.values.tolist ()

print(list_column[1:])

df['average'] = df[list_column[1:]].mean (axis= 1 )

df['ab'] =  df['SU26224RMFS4'].apply(renum)
print(df)

closeprice=df['ab']
datamassive=df['<DATE>']
aver_line = df['average']

fig, axs = plt.subplots(nrows= 2 , ncols= 1 , figsize=(10,10), gridspec_kw={'height_ratios': [2, 1]})
axs[0].plot(datamassive, closeprice)
axs[0].grid(linestyle='-', linewidth=1, alpha=0.5)


# plt.figure(figsize=(5,5))

# plt.plot(datamassive, closeprice)

axs[1].bar(datamassive, aver_line)

# # plt.gcf().autofmt_xdate()
# # myFmt = mdates.DateFormatter('%dd.%mm.%YY')
# # plt.gca().xaxis.set_major_formatter(myFmt)
# # plt.locator_params (axis='x', nbins= 10 )

# plt.xticks(np.arange(0, 1001, 100))
# plt.ylabel('Цена', fontsize=10)

# plt.grid(linestyle='-', linewidth=1, alpha=0.5)
# # plt.grid(linestyle='-', which='both', linewidth=1, alpha=0.3)

# margins = {                                            
#     "left"   : 0.040,
#     "bottom" : 0.060,
#     "right"  : 0.990,
#     "top"    : 0.990   
# }

# plt.subplots_adjust(**margins)   
# plt.margins(x=0.00) #убрать отступы
# plt.legend(title='динамика по бумаге SU26207RMFS9')

plt.show()

 
 
  