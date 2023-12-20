n, k = int(input()), int(input())

m = [i + 1 for i in range(n)]

 

ind = 0     # индекс счета
indrun = 0  # бегунок
while len(m) > 1:
    while ind<= (k - 1):
        # print(ind, indrun)
        if ind == (k - 1):
            # print('удаляется: ' , m[indrun])
            m.pop(indrun)
            # print('===', ind, indrun)
            # print(m)
            # print()
            ind = 0
            indrun += 0
            if indrun >= len(m): indrun = 0
            break
        ind += 1
        indrun += 1
        # if ind >= len(m): ind = 0
        if indrun >= len(m): indrun = 0

print(*m)        

# альтернативные решения

# n = int(input())
# k = int(input())
 
# res = 0
# for i in range(1, n+1):
#     res = (res + k) % i
# print(res + 1)
# 
# 
# n = int(input())
# k = int(input())
# list = [i for i in range(1, n + 1)]

# while len(list) != 1:
#     for i in range(0, k-1):
#         list.append(list[i])
#     del list[0:k]

# print(*list)
    

# n = int(input())
# k = int(input())
# s = list(range(1, n + 1))

# i = 1
# while len(s) > 1:
#     if i % k == 0:
#         del s[0]
#     else:
#         s.append(s[0])
#         del s[0]        
#     i += 1
# print(s[0])