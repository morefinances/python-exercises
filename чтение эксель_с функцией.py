import pandas as pd

def my_txt(text):
    txt = ""
    for i in range(len(text)):
        if text[i] == "/":
            break
        if text[i] == " ":
            txt += ""
        else:
            txt += text[i]
    return txt


file = "C:\\files\\result.xls"
xl = pd.read_excel(file)
for i in range(len(xl['Участник'])):
    #print(['Участник'][i])
    print(my_txt(xl['Участник'][i]))