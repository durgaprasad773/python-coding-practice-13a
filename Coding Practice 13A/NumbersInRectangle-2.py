m=int(input())
n=int(input())
num=1
for i in range(m):
    res=""
    for j in range(n):
        res = res + str(num)+" "
        num=num+1
    print(res)