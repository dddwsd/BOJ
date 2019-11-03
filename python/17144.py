''''''
'''
RxC 격자판 -> 각 칸의 미세먼지양 실시간 모니터링

공기청정기 항상 왼쪽열 -> (x,0) & 크기 = 2
r,c에 있는 미세먼지양은 Arc
'''
'''
입력
1. r,c,t -> y,x,시간
2. r줄에 걸쳐서 Arc가 주어진다
(공기청정기는 -1 / 가장 윗행, 가장 아랫행과 2칸이상 떨어져있다)

출력
t초가 지난 후 방에 남아있는 미세먼지의 양을 출력
'''
'''
1. 미세먼지 확산 -> 모든칸에서 동시에 일어난다.
- (r,c)에 있는 미세먼지는 인접한 4방향으로 확산
- 인접한 방향에 공기청정기가 있거나 칸이 없으면 그 방향으로는 확산 x
- 확산되는 양은 Arc/5이고 소수점은 버린다
- (r,c)에 남은 미세먼지의 양은 Arc - (Ard/5) * 확산된 방향개수
'''
d = [[0,1],[0,-1],[-1,0],[1,0]]
def spread(point,a1y,a2y):
    t_matrix = [[0]*c for _ in range(r)]
    t_matrix[a1y][0],t_matrix[a2y][0] = -1,-1
    while point:
        x,y,val = point.popleft()
        cnt = 0
        for dx,dy in d:
            nx, ny = x + dx , y + dy
            if 0<= nx < c and 0<= ny < r and t_matrix[ny][nx] != -1:
                cnt += 1
                t_matrix[ny][nx] += int(val/5)
        t_matrix[y][x] += (val - int(val/5)*cnt)
    for i in range(r):
        for j in range(c):
            if t_matrix[i][j] > 0:
                point.append([j,i,t_matrix[i][j]])


'''
2. 공기청정기 작동
- 바람이 나온다 
- 바람이 불면 미세먼지가 바람의 방향대로 한칸씩 이동
- 공기청정기에서 부는 바람은 미세먼지가 없는 바람 
- 공기청정기로 들어간 미세먼지는 모두 정화된다.
'''
def move(point,ran,ch,a1y,a2y):
    start,end,dx,dy = ran[0],ran[1],ch[0],ch[1]
    temp = []
    for i in range(len(point)):
        x,y,val = point[i]
        if start[0] <= x <= end[0] and start[1] <= y <= end[1]:
            x += dx
            y += dy
            if x == 0 and (y == a1y or y == a2y):
                temp.append(i)
                continue
        point[i][0],point[i][1] = x,y
    for i in reversed(temp):
        del point[i]
'''
- 위쪽 공기청정기 : 반시계방향
(0,a1y-1) ~ (0,0) : y+1
(1,0) ~ (c-1,0) : x-1
(c-1,1) ~ (c-1,a1y) : y-1
(c-2,a1y) ~ (1,a1y) : x+1
- 아래쪽 공기청정기 : 시계방향
(0,a2y+1) ~ (0,r-1) : y-1
(1,r-1) ~ (c-1,r-1) : x-1
(c-1,r-2) ~ (c-1,a2y) : y+1
(c-2,a2y) ~ (1,a2y) : x+1
'''
def clean(point,a1y,a2y):
    up =   [[[0,0],[0,a1y-1]],[[1,0],[c-1,0]],[[c-1,1],[c-1,a1y]],[[1,a1y],[c-2,a1y]]]
    ch_u = [[0,1],[-1,0],[0,-1],[1,0]]
    down = [[[0,a2y+1],[0,r-1]],[[1,r-1],[c-1,r-1]],[[c-1,a2y],[c-1,r-2]],[[1,a2y],[c-2,a2y]]]
    ch_d = [[0,-1],[-1,0],[0,1],[1,0]]
    for i in range(4):
        move(point,up[i],ch_u[i],a1y,a2y)
        move(point,down[i],ch_d[i],a1y,a2y)

def solution(point,a1y,a2y,t):
    for _ in range(t):
        spread(point,a1y,a2y)
        clean(point,a1y,a2y)
    result = 0
    for item in point:
        result += item[2]
    print(result)

from collections import deque
r,c,t = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(r)]
a1y,a2y=0,0
point = deque()
flag = 0
for i in range(r):
    for j in range(c):
        if matrix[i][j] == -1:
            if a1y == 0:
                a1y = i
            else:
                a2y = i
            continue
        if matrix[i][j] > 0 :
            point.append([j,i,matrix[i][j]])
solution(point,a1y,a2y,t)
