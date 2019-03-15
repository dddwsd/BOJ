n = int(input())
a = list(map(int,input().split()))
a.sort()
sum = 0
for i in range(0,n):
    sum = sum + a[i]/a[n-1] *100
sum = sum / n
print(sum)
