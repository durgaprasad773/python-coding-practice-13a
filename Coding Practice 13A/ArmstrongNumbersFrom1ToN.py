n=int(input())
for i in range(1,n+1):
    s = str(i)
    num = len(s)
    total = 0
    for j in s:
        total = total + (int(j) ** num)
    if total == int(s):
        print(total)
    