n=int(input())

for i in range(n):
    res=""
    num= (n-i)
    for j in range(1,num+1):
        res = res + str(j)+" "
    print(res)