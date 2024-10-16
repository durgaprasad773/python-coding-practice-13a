m=int(input())
n=int(input())
res =""
for num in range(m,n+1):
    if num > 1:
        for i in range(2,num):
            if num % i ==0:
                break
        else:
            res = res + str(num) + " "
if (len(res) > 0):
    print(res)
else:
    print("No Prime Numbers Found")