from zipfile import ZipFile
import os
 
from zipfile import ZipFile
import os

print("Hello, это SergioProjectCompany. Файл обработки архивов версия 1.2")
print("Наши расценки без изменений: 1 задача = 1 курник :), обращайтесь. \n\n")


# рабочая директория
# обязательно в 2 переменных
name1 = 'C:/files_archive/'
name3 = 'C:/files_final/'    



# чтение архива 
get_filz = os.listdir(name1)

for bb in range(len(get_filz)):
    name2 = 'C:/files_archive/'
    print('Идёт обработка файла :', get_filz[bb])
    # разархивирование
    with ZipFile(name1 + get_filz[bb], mode="r") as archive:
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
    os.replace(name2 + get_files[0], name3 + get_files[0])
    # удаление пустых папок
    for m in range(4, 0, -1):
        t = ""
        for u in range(m):
            t += aaname[u] + '/'
        os.rmdir(name1 + t)
    # удаление изначального архива
    os.remove(name1 + get_filz[bb])
    print('Файл ' + get_filz[bb] + ' обработан \n')

print('Фууф, на сегодня всё.\n')

print("Хорошего рабочего дня, колллеги! :-)")
