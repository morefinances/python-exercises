
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Nstring = 97.5 .min()
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


df = pd.read_csv('C:\\files\\OFS8_1.csv', delimiter=';')


df['rgbi_no'] =  df['RGBI'] #.apply(renum)
df['aver_no'] =  df['average_rgbi'] #.apply(renum)



closeprice=df['rgbi_no']
# datamassive=df['<DATE>']
datamassive = df['<DATE>'].apply(newdata)
aver_line = df['aver_no']


daystring = findday2()
monthdatamassive = datamassive[daystring:]
monthcloseprice = closeprice[daystring:]
monthaver = aver_line[daystring:]



indexstart = 0
nmonthaver  = monthaver.apply(renum)
indexstart = 0
nmonthcloseprice = monthcloseprice.apply(renum)
ndate = [i for i in range(1001-daystring)]

Nstring = nmonthaver.min() - 0.04
# print(Nstring)

days=datalist(monthdatamassive)
# datafondraw(monthdatamassive)

plt.figure(figsize=(10,4)) 
margins = {                                            
    "left"   : 0.05,
    "bottom" : 0.035,
    "right"  : 0.992,
    "top"    : 0.990   
}

plt.subplots_adjust(**margins)   

indexlist = monthdatamassive.index.tolist()
colorfon = 0
indexdate = 0
plt.text(indexdate, Nstring, days[indexdate][:6], size=8, color = 'k')
indexdate += 1
for i in range(len(monthdatamassive)-1):
    if monthdatamassive[indexlist[i]] == monthdatamassive[indexlist[i] + 1]:
        # plt.text(i, 92.8, 1, size=15, color = '#1F77B4')
        if colorfon == 1:
            plt.axvline (x=i, color='#E8F1F9', linewidth=2, alpha = 0.8)
            # print(i, ' / ', end ="")
    else:
        if colorfon == 1:
            plt.axvline (x=i, color='#E8F1F9', linewidth=2, alpha = 0.8)    
        plt.text(i, Nstring, days[indexdate][:6], size=8, color = 'k')
        indexdate += 1
        if colorfon == 0:
            colorfon = 1
        else:
            colorfon = 0
plt.axvline (x=len(monthdatamassive)-1, color='b', linewidth=2, alpha=0.1)
    
# print(datalist(monthdatamassive))

# plt.xticks(np.arange(0, len(datamassive),10), datamassive)


# print(len(days), '=days')
plt.xticks([])
plt.axvline (x=0, color='k', linestyle=':',  linewidth=1, alpha=0.3)
plt.axvline (x=len(monthdatamassive)-1, color='k', linestyle=':',  linewidth=1, alpha=0.3)



# plt.vxhline(x=0, color='#1F77B4', linestyle='--', linewidth=1)

# plt.xticks(np.arange(0, daystring, 100))
# fig, axs = plt.subplots(nrows= 2 , ncols= 1 , figsize=(20,10), gridspec_kw={'height_ratios': [3, 1]})
plt.plot(ndate, nmonthcloseprice, color="k")
plt.plot(ndate, nmonthaver)
plt.grid(linestyle='-', linewidth=1, alpha=0.5)
plt.margins(x=0.015)

plt.plot(0, 100, 'o', color = '#206497', ms = 3)

# print(len(closeprice))
# aa_one = nmonthcloseprice[len(closeprice)-1]
# aa_two = nmonthaver[len(closeprice)-1]
# print(aa_one-aa_two)
# print(100*(aa_one-aa_two)/aa_two, "%")

maxX = len(nmonthcloseprice)

plt.text(maxX - 16, nmonthcloseprice[len(closeprice)-1] + 0.1, round(nmonthcloseprice[len(closeprice)-1],2), size=10, color = 'k')

plt.text(maxX - 16, nmonthaver[len(closeprice)-1] - 0.2, round(nmonthaver[len(closeprice)-1],2), size=10, color = '#206497')

firstRGBI = round(closeprice[daystring],2)
lastRGBI = round(closeprice[len(closeprice)-1],2)
textRGBI = 'RGBI(0)=' + str(firstRGBI) + '   RGBI(N)=' + str(lastRGBI)

plt.text(maxX - 90, nmonthcloseprice.max(), textRGBI, size=10, color = 'k')

firstAV = round(aver_line[daystring],2)
lastAV = round(aver_line[len(closeprice)-1],2)
textAV = 'PrtB(0)=' + str(firstAV) + '    PrtB(N)=' + str(lastAV)

plt.text(maxX - 90, nmonthcloseprice.max() - 0.2, textAV, size=10, color = 'k')


filename = currenttime()
# plt.savefig('C:\\files\\pctrs\\1MN_' + filename + '.png')
plt.savefig('C:\\files\\pctrs\\PortfolioBonds_and_RGBI_1MN.png')

plt.show()


 
 
  