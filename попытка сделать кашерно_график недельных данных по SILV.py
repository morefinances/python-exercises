import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.dates as mdates
import datetime





df = pd.read_csv('C:\\files\marketdata\slv.csv', delimiter=',')

closeprice=df['<CLOSE>']
tradetime=df['<TIME>'].astype(str)
datamassive=df['<DATE>'].astype(str)

newdatamassive = datamassive + tradetime

realdata = pd.to_datetime(newdatamassive, format='%Y%m%d%H%M%S')

print(realdata.head(5))
