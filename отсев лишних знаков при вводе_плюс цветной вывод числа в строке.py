import random
from colorama import init, Fore, Style, Back

def onlynum(text):
    a = "0123456789"
    txt = ""
    for i in text:
        if i in a:
            txt += i
    return txt

# print(onlynum('12/3.5<!,fg3*'))

def random_long_txt(numb):
    s = "_?^~>]}=\|<[{;Zz:Yy9Xx8Ww7Vv6Uu5Tt4Ss3Rr2Qq1Pp0Oo/Nn.Mm-Ll,Kk+Jj*Ii)Hh(Gg'Ff&Ee%Dd$Cc#BbAa!@"
    long_txt = ""
    for i in range(numb):
        long_txt += random.choice(s)
    return long_txt

def colorprint(text):
    a = "0123456789"
    for i in text:
        if i in a:
            print(Back.WHITE, end="")
            print(Fore.BLUE + i, end="")
            print(Style.RESET_ALL, end="")
        else:
            print(i, end="")
               

for i in range(20):
    U = random_long_txt(30)
    du = onlynum(U)
    if du=="":
        du ="-- none --"
    colorprint(U)
    print("\t" + du)
    

