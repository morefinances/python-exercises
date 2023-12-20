list1 = [[1, 7, 8, 15, 17, 1], [9, 7, 1102], [600, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

total_len = 0
total_sum = 0

for i in range(len(list1)):
    total_len += len(list1[i])
    for elem in list1[i]:
        total_sum += elem
    
print(total_len, total_sum)       
 