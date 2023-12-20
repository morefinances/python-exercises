import pandas as pd

df = pd.read_csv('C:\\files\marketdata\slv.csv', delimiter=',')

closeprice=df['<CLOSE>']
tradetime=df['<TIME>'].astype('str')
datamassive=df['<DATE>'].astype('str')

newdatamassive = datamassive + " " + tradetime

realdata = pd.to_datetime(newdatamassive, '%Y%m%d %H%M%S')

print(newdatamassive.head(5))
