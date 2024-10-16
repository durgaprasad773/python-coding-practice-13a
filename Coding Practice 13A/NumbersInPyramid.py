m=int(input())
n=int(input())

for i in range(1,n+1):
    num = m
    space = " " * (n-i)
    row=""
    for j in range(1,i+1):
        row = row + str(num)+" "
        num = num + 1
    print(space + row)