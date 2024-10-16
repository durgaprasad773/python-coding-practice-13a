n=int(input())
for i in range(1,n+1):
    num = n
    row = ""
    for j  in range(1,n+1):
        row = row + str(num-j) +" "
    print(row)