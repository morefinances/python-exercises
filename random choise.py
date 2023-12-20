import random as rd

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@%&_abcdefghijklmnopqrstuvwxyz1234567890'

a=''
# a=list(s)
# rd.shuffle(a)
for n in range(10):
    print (n + 1, end=": ")
    for i in range(10):
        a += rd.choice(s)
    print(a)
    a = ''