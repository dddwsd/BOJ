import sys
a,b = map(int,input().split())
#M=[list(map(lambda x: ord(x)-65,input())) for i in range(a)]
total = []
for i in range(0,a):
    total.append(sys.stdin.readline().rstrip())
    # rstrip()을 사용함으로써 \n제거

result = []

result.append([total[0][0],0,0])

max_len = 0

while True:
    
    alp,x,y = result.pop()

    max_len = max(max_len,len(alp))


    if x-1 >= 0 and total[x-1][y] not in alp:
        result.append([alp + total[x-1][y],x-1,y])

    if x+1 < a and total[x+1][y] not in alp:
        result.append([alp + total[x+1][y],x+1,y])

    if y-1 >= 0 and total[x][y-1] not in alp:
        result.append([alp + total[x][y-1],x,y-1])

    if y+1 < b and total[x][y+1] not in alp:
        result.append([alp + total[x][y+1],x,y+1])
    if not result:
        break    

print(max_len)
    




