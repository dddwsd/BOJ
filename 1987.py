import sys

def move(x,y):
    global result
    global check
    if x < 0 or x >= a or y < 0 or y >= b:
        return
    asc = ord(total[x][y])-65
    if alpha[asc] == 1:
        return
    alpha[asc] = 1
    check += 1
    move(x-1,y)
    move(x+1,y)
    move(x,y-1)
    move(x,y+1)
    if result < check:
        result = check
    check -= 1
    alpha[asc] = 0



a,b = map(int,input().split())
total = []
for i in range(0,a):
    total.append(sys.stdin.readline())
    
alpha = [0 for i in range(26)]
# A 는 65 -> 0이 되어야 하므로 -65
result = 0
check = 0
move(0,0)
print(result)