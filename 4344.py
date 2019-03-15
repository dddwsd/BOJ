c = int(input())
for i in range(0,c):
    a = list(map(int,input().split()))
    n = a[0]
    del a[0]
    avg = sum(a,0)/n
    ck = 0
    for j in range(0,n):
        if avg < a[j]:
            ck = ck + 1
    answer = ck/n*100
    
    print("%0.3f" %round(answer,3),end='')
    print("%")