
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

indexstart = 0

def renum(x):
    global indexstart
    if indexstart == 0:
        indexstart = x
        return 100
    else:
        a = 100*(x/indexstart)
        return a


def datalist(list_one):
    a = []
    indexlist = list_one.index.tolist()
    for i in range(len(list_one)-1):
        if list_one[indexlist[i]] != list_one[indexlist[i] + 1]:
             a.append(list_one[indexlist[i]]) 
        # else:
            # a.append(str(0))
    a.append(list_one[indexlist[len(list_one) - 1]])
    return a



def newdata(x):
    return (str(x)[:6] + str(x)[-2:])    


def findday2():
    current_datetime = datetime.now()
    year = str(current_datetime.year-2000)
    if current_datetime.day < 10:
        day = '0' + str(current_datetime.day)
    else:
        day = str(current_datetime.day)
    if (current_datetime.month - 1) < 10:
        month = '0' + str(current_datetime.month-1)
    else:
        month = str(current_datetime.month-1)
    find_date = year + month + day
    # print(find_date)
    for i in range(len(datamassive) - 1):
        a = str(datamassive[i]).replace('.','')
        b = str(datamassive[i + 1]).replace('.','')
        aa = a[4:] + a[2:4] + a[:2]
        bb = b[4:] + b[2:4] + b[:2]
        
        if int(aa) < int(find_date) and int(bb) >= int(find_date):
            # print('-->', i, aa, bb)
            return(i + 1)


df = pd.read_csv('C:\\files\\OFS6_1.csv', delimiter=';')


df['rgbi_norm'] =  df['RGBI'].apply(renum)
indexstart = 0
df['aver_norm'] =  df['average_rgbi'].apply(renum)
df['date_norm'] = df['<DATE>'].astype(str) + " " + df['<TIME>'].astype(str)
# df['date_norm'] =  df['<DATE>'].apply(lambda x: str(x) + " ")




# print(*ndate)

closeprice=df['rgbi_norm']
# datamassive=df['<DATE>']
datamassive = df['<DATE>'].apply(newdata)
aver_line = df['aver_norm']

daystring = findday2()
monthdatamassive = datamassive[daystring:]
monthcloseprice = closeprice[daystring:]
monthaver = aver_line[daystring:]

ndate = [i for i in range(1001-daystring)]

print(len(ndate))
days=datalist(monthdatamassive)
# datafondraw(monthdatamassive)

plt.figure(figsize=(12,5)) 
indexlist = monthdatamassive.index.tolist()
colorfon = 0
for i in range(len(monthdatamassive)-1):
    if monthdatamassive[indexlist[i]] == monthdatamassive[indexlist[i] + 1]:
        # plt.text(i, 92.8, 1, size=15, color = '#1F77B4')
        if colorfon == 1:
            plt.axvline (x=i, color='k', linewidth=2, alpha=0.1)
            print(i, ' / ', end ="")
    else:
        if colorfon == 0:
            colorfon = 1
        else:
            colorfon = 0
    
# print(datalist(monthdatamassive))

# plt.xticks(np.arange(0, len(datamassive),10), datamassive)


print(len(days))
plt.xticks([])
plt.axvline (x=0, color='k', linestyle=':',  linewidth=1, alpha=0.3)
plt.axvline (x=len(monthdatamassive)-1, color='k', linestyle=':',  linewidth=1, alpha=0.3)



# plt.vxhline(x=0, color='#1F77B4', linestyle='--', linewidth=1)

# plt.xticks(np.arange(0, daystring, 100))
# fig, axs = plt.subplots(nrows= 2 , ncols= 1 , figsize=(20,10), gridspec_kw={'height_ratios': [3, 1]})
plt.plot(ndate, monthcloseprice, color="k", alpha=0.5)
plt.plot(ndate, monthaver)
plt.grid(linestyle='-', linewidth=1, alpha=0.5)
plt.margins(x=0.01)

plt.text(0, 92.8, "100", size=15, color = '#1F77B4')


plt.show()


 
 
  