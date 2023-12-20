# r1 = ['a', 'aa', 'ab', 'bb']
# r2 = list(enumerate(r1, start = 1))
# print(r2[2])

#----------------------------

# lst = [5, 3, 1, 0, 9, 7]
# lst_num = list(enumerate(lst, 0))
# print(*lst_num)

# tup_max = max(lst_num, key=lambda i : i[1])
# tup_min = min(lst_num, key=lambda i : i[1])

# print(f'Индекс максимума: {tup_max[0]}, Max число {tup_max[1]}')
# print(f'Индекс минимума: {tup_min[0]}, Min число {tup_min[1]}')

#----------------------------

lst = [5, 3, 1, 0, 9, 7]
n1=enumerate(lst)
print(len(lst))
