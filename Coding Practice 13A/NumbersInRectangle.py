m=int(input())
n=int(input())
num = 7
for i in range(m):
    row=""
    for j in range(n):
        row = row + str(num+j)+" "
    print(row)