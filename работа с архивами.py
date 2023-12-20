# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:49:58 2023

@author: S.Stycenkov
"""

from zipfile import ZipFile
import os
# import shutil

with ZipFile("C:/files/marketdata/33016446540.zip", mode="r") as archive:
    # archive.printdir()
    # archive.extractall()
    aname=[]
    for file in archive.namelist():
        # print(file) 
        aname.append(file)
    aaname=aname[0].split('/')
    archive.extract(aname[0], "C:/files/")
    archive.close()

name1 = 'C:/files/'
name2 = 'C:/files/'    

for i in range(4):
    name2 +=  aaname[i] + '/'
print(name2)

# print(path.exists(source_path))

get_files = os.listdir(name2)
print(get_files)

os.replace(name2 + get_files[0], name1 + get_files[0])


for m in range(4, 0, -1):
    t = ""
    for u in range(m):
        t += aaname[u] + '/'
    os.rmdir(name1 + t)
    print(t)
# os.rmdir('C:/files/' + aaname[0] + '/' + aaname[1] + '/' + aaname[2] + '/' + aaname[3] + '/' )
# os.rmdir('C:/files/' + aaname[0] + '/' + aaname[1] + '/' + aaname[2] + '/' )
# os.rmdir('C:/files/' + aaname[0] + '/' + aaname[1] + '/' )
# os.rmdir('C:/files/' + aaname[0] + '/' )
    
# archive.extract(aname[0], "C:/files/")
# разархивировать всё
# archive.extractall('C:/files/marketdata/')


# myzip = ZipFile.open('C:\\files\marketdata\33016446540.zip', mode='r')
# # myzip = ZipFile('C:/files/marketdata/33016446540.zip', "w")
# print(myzip.infolist())
# myzip.close()

# C:/files/marketdata/33016446540.xlsx'

#  текущий каталог
# print(os.getcwd())