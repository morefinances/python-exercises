from colorama import Fore, Style, Back
import random

def mycolor(num):
    if num == 0:
        print(Fore.RED, end = "")
    elif num == 1:
        print(Fore.GREEN, end = "")
    elif num == 2:
        print(Fore.BLUE, end = "")
    elif num == 3:
        print(Fore.WHITE, end = "")
    elif num == 4:
        print(Fore.YELLOW, end = "")
    elif num == 5:
        print(Fore.MAGENTA, end = "")
    elif num == 6:
        print(Fore.CYAN, end = "")

stext = ""

for i in range(1000):
    newcolor = random.randint(0, 6)
    newnumber = random.randint(0, 9)
    stext += str(newnumber)
    mycolor(newcolor)
    print(newnumber, end="")

print(Style.RESET_ALL)
print(len(stext))
print("")

#for i in range(10):
for i in range(11, 101, 11):
    #print(i)
    print(str(i), ": ", stext.count(str(i)))