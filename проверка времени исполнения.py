import datetime as dtm
import time

INN = str(input())

t1 = dtm.datetime.now()

print(t1)
if len(INN) != 12:
    print('Не 12 симполов!')

t2 = dtm.datetime.now()
print(t2)

for i in range(len(INN)):
    if INN[i].isdigit() == False:
        print('Присутствует лишний символ:', INN[i])

t3 = dtm.datetime.now()
print(t3)

print('Время обработки первого условия:')
print(t2-t1)
print('Время обработки второго условия:')
print(t3-t2)

# print('\n', t1, '\n', t2, '\n', t3)
# code_to_test = '''
# INN = input()

# if len(INN)!=12:
#     print('Введено не 12 символов')
# '''

# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print('Elapsed time: ', elapsed_time)

# code_to_test2 = '''

# for i in range(len(INN)):
#     print(INN[i])

# '''

# elapsed_time2 = timeit.timeit(code_to_test2, number=100)/100
# print('Elapsed time: ', elapsed_time2)
 

 