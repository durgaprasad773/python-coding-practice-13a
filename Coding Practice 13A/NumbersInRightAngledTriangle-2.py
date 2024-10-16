n=int(input())
for i in range(1,n+1):
    row=""
    space ="  " * (n-i)
    for j in range(1,i+1):
        row = str(j)+" " + row
    print(space + row)