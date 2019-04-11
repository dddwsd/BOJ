tc = int(input())

x = {}
for i in range(0,tc):
    a,b = map(int,input().split())
    if a in x:
        x[a].append(b)
    else:
        x[a] = []
        x[a].append(b)

key = sorted(x)

for i in key:
    list1 = x[i]
    list1.sort()
    for j in list1:
        print(i,j) 