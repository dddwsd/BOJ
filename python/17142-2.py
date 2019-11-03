from itertools import combinations
from collections import deque

d = [[0,-1],[0,1],[-1,0],[1,0]]
def solution(full):
    global matrix,start,wall
    check = [[False]*n for _ in range(n)]
    for x,y in start:
        check[y][x] = True
    for x,y in wall:
        check[y][x] = True
    cnt = 0
    while full != 0:
        length = len(start)
        t_point = deque()
        for _ in range(length):
            x,y = start.popleft()
            for dx,dy in d:
                nx, ny = x + dx , y + dy
                if 0 <= nx < n and 0 <= ny < n and check[ny][nx] == False:
                    t_point.append([nx,ny])
                    check[ny][nx] = True
                    if matrix[ny][nx] == 0:
                        full -= 1
        if not t_point and full > 0 :
            return -1
        cnt +=1
        start = t_point
    return cnt

n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
point,wall,full,result = [],[],n*n,[]
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            full -= 1
            if matrix[i][j] == 2:
                point.append([j,i])
            if matrix[i][j] == 1:
                wall.append([j,i])

for start in list(combinations(point,m)):
    start = deque(start)
    val = solution(full)
    if val != -1:
        result.append(val)
if result:
    print(min(result))
else:
    print(-1)