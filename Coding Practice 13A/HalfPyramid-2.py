n=int(input())
num=1
for i in range(1,n+1):
    res=""
    for j in range(1,i+1):
        res = res + str(num)+" "
        num=num+1
    print(res)