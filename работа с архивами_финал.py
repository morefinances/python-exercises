from zipfile import ZipFile
import os

# рабочая директория
# обязательно в 2 переменных
name1 = 'C:/fls/'
name2 = 'C:/fls/'    

# чтение архива 
get_filz = os.listdir(name1)


# разархивирование
with ZipFile(name1 + get_filz[0], mode="r") as archive:
    aname=[]
    for file in archive.namelist():
        aname.append(file)
    aaname=aname[0].split('/')
    archive.extract(aname[0], name2)
    archive.close()

# переменная со всеми поддиректориями
for i in range(4):
    name2 +=  aaname[i] + '/'

# перенос файла
get_files = os.listdir(name2)
os.replace(name2 + get_files[0], name1 + get_files[0])

# удаление пустых папок
for m in range(4, 0, -1):
    t = ""
    for u in range(m):
        t += aaname[u] + '/'
    os.rmdir(name1 + t)


# удаление изначального архива
os.remove(name1 + get_filz[0])

print("Хорошего рабочего дня, колллеги! :-)")