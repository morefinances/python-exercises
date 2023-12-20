N = 5
M = 6
A = [ [0]*M for i in range(N) ]

for i in range(N):
    for j in range(M):
        A[i][j] = 100*i + j*3

print(A)

print()

for i in range(len(A)):          
    for j in range(len(A[i])):   
        print(A[i][j], end = ' ')
    print()        

print()

for row in A:
    print('\t'.join(list(map(str, row))))