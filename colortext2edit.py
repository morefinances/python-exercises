
import colorama
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

colorama.init() 
for i in range(20):
    
    if i == 0:
        lastcolor = 0
    else:
        lastcolor = newcolor
    
    newcolor = random.randint(0, 6)
    
    if newcolor == lastcolor:
        while newcolor == lastcolor:
            # print('rerand:' + '-'*20)
            newcolor = random.randint(0, 6)
            # print(str(lastcolor) + " // " + str(newcolor))
    
    mycolor(newcolor)
    print(str(lastcolor) + " // " + str(newcolor) + ' ' + '-'*20)

        
        
        

# print(Fore.GREEN + '='*50)
# print(a[1] + '~'*50, end="")
# print('color text')

# print(Style.RESET_ALL, end="")


               

