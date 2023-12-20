
import pandas as pd
import matplotlib.pyplot as plt

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
  

df = pd.read_csv('C:\\files\\OFS6.csv', delimiter=';')

#df.set_index('<DATE>', inplace = True)
#print(df)

# list_column = df.columns.values.tolist ()

# print(list_column[1:])

# df['average'] = df[list_column[1:]].mean (axis= 1 )

df['rgbi_norm'] =  df['RGBI'].apply(renum)
indexstart = 0
df['aver_norm'] =  df['average_rgbi'].apply(renum)
df['date_norm'] =  df['<DATE>'].apply(lambda x: str(x) + " ")
print(df)

ndate = [i for i in range(1001)]

# print(*ndate)

closeprice=df['rgbi_norm']
datamassive=df['date_norm']
aver_line = df['aver_norm']

fig, axs = plt.subplots(nrows= 2 , ncols= 1 , figsize=(20,10), gridspec_kw={'height_ratios': [3, 1]})
axs[0].plot(ndate, closeprice, color="k", alpha=0.5)
axs[0].plot(ndate, aver_line)
axs[0].grid(linestyle='-', linewidth=1, alpha=0.5)
axs[0].margins(x=0.00)


 

axs[1].bar(ndate, aver_line)
axs[1].margins(x=0.00)

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

 
 
  