
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import datetime as dtm

 


def newdata2(x):
    y = str(x)
    ndata = str(y[:2]) + "." + str(y[2:4]) + "." + str(y[-4:])
    # print(x, y, ndata)
    return ndata

 
 
df = pd.read_csv('C:\\files\\PortfolioRGBI_M10_N.csv', delimiter=',')
print(df['<DATE>'])
print(df)