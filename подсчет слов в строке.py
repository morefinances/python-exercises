# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:49:42 2023

@author: S.Stycenkov
"""

import pandas as pd

data_string = 'The Python Software Foundation (PSF) is a 501(c)(3) non-profit corporation that holds the intellectual property rights behind the Python programming language. We manage the open source licensing for Python version 2.1 and later and own and protect the trademarks associated with Python. We also run the North American PyCon conference annually, support other Python conferences around the world, and fund fund Python related development with our grants program and by funding special projects.'

# делается циклом, убирая в т.ч. цифры
data_string=data_string.replace('.', '')
data_string=data_string.replace(',', '')
data_string=data_string.replace('(', '')
data_string=data_string.replace(')', '')

word = data_string.split()
word.sort()

print(word)
print(len(word))

m = list(set(word))

# m.sort()
print(m)

print(len(m))
print()

mn = [0 for i in range(len(m))]
print(mn)

mnn = {'A': m, 'B': mn}

mdata=pd.DataFrame(mnn)
# print(mdata)

for i in range(len(m)):
    mdata['B'][i] = word.count(mdata['A'][i])
    print(mdata['B'][i], ':', mdata['A'][i])

print(mdata[mdata['B']>=2])