
mynum = [
    5 * x + 3
    for x in range(20)
    if x % 2 == 1
]

print(*mynum, sep=" | ")
