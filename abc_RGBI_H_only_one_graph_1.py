
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

indexstart = 0

def renum(x):
    global indexstart
    if indexstart == 0:
        indexstart = x
        return 100
    else:
        a = 100*(x/indexstart)
        return a

def newdata(x):
    return (str(x)[:6] + str(x)[-2:])    


df = pd.read_csv('C:\\files\\OFS6_1.csv', delimiter=';')



df['rgbi_norm'] =  df['RGBI'].apply(renum)
indexstart = 0
df['aver_norm'] =  df['average_rgbi'].apply(renum)
df['date_norm'] = df['<DATE>'].astype(str) + " " + df['<TIME>'].astype(str)
# df['date_norm'] =  df['<DATE>'].apply(lambda x: str(x) + " ")
print(df['date_norm'])

ndate = [i for i in range(1001)]

# print(*ndate)

closeprice=df['rgbi_norm']
# datamassive=df['<DATE>']
datamassive = df['<DATE>'].apply(newdata)
aver_line = df['aver_norm']

# plt.xticks(np.arange(0, len(datamassive),10), datamassive)

plt.figure(figsize=(10,5))
plt.xticks(np.arange(0, 1001, 100))
# fig, axs = plt.subplots(nrows= 2 , ncols= 1 , figsize=(20,10), gridspec_kw={'height_ratios': [3, 1]})
plt.plot(ndate, closeprice, color="k", alpha=0.5)
plt.plot(ndate, aver_line)
plt.grid(linestyle='-', linewidth=1, alpha=0.5)
plt.margins(x=0.00)

# axs[1].bar(ndate, aver_line)
# axs[1].margins(x=0.00)

plt.show()


 
 
  