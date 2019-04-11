n,m,h = map(int,input().split())
matrix = [[0]*n for _ in range(h)]
for i in range(m):
    a,b = map(int,input().split())
    # b번 세로선과 b+1번 세로선을 a번 점선위치에서 연결하겠다.    
    if b <= n-1:
        matrix[a-1][b-1] = 1


def check():
    for i in range(n):
        pos1 = i
        for j in range(h):
            if matrix[j][pos1] == 1 :
                pos1+=1
            elif matrix[j][pos1-1] == 1:
                pos1-=1
        if i != pos1:
            return False
    return True
        
ck=4
def DFS(cnt,x,y):
    global ck
    global matrix
    if cnt >= ck:
        return
    if check() == True:
        ck = cnt
        return
    if cnt == 3:
        return 
    for i in range(y,h):
        pos = x
        while True:
            if pos >= n-1:
                break
            if matrix[i][pos] != 0:
                pos += 2
                continue
            matrix[i][pos] = 1
            DFS(cnt+1,pos+2,i)
            matrix[i][pos] = 0
            pos +=1
        x = 0

DFS(0,0,0)
if ck > 3:
    print(-1)
else:
    print(ck)