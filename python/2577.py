a = int(input())
b = int(input())
c = int(input())

dic = {}
for i in range(0,10):
    dic[i] = 0
d = a*b*c
d = list(map(int,list(str(d))))
for i in d:
    dic[int(i)] += 1

for i in range(0,10):
    print("%d" %dic[i])