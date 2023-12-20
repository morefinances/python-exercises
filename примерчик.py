a=12
xx=[i for i in range(100)]
# print(*xx)

for i in range(90): 
    if i%2 == 0 and i>10:
        xx.remove(i)
print(*xx)