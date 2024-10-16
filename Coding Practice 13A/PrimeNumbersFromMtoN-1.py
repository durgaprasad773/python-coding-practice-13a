m=int(input())
n=int(input())
for num in range(m,n+1):
    if num > 1:
        for i in range(2,num):
            if num % i ==0:
                break
        else:
            print(num)