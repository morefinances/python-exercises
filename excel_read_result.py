import pandas as pd

def my_txt(text):
    txt = ""
    for i in range(len(text)):
        if text[i] == "/":
            break
        if text[i] == '"':
            txt += ""
        else:
            txt += text[i]
    return txt

def type_format_client(text):
    for i in range(len(text)):
        if text[i] == "/":
            return "F"
            break
    return "U"

file = "C:\\files\\result.xls"
xl = pd.read_excel(file)
for i in range(len(xl['Участник'])):
    str_xl = xl['Участник'][i]
    print("[" + type_format_client(str_xl) + "] " + my_txt(str_xl).rstrip(" "))

#del_zero_end('123452 ')