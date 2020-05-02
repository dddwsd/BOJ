n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
result = [[[[0]*3 for _ in range(4)] for _ in range(m)] for _ in range(n)]
goal = []
wall = set([])
for y in range(n):
    for x in range(m):
        if matrix[y][x] == 'S':
            sx,sy = x,y
        elif matrix[y][x] == 'C':
            goal.append([x,y])
        elif matrix[y][x] == '#':
            wall.add((x,y))

d = [[-1,0],[1,0],[0,1],[0,-1]]

from collections import deque
def bfs(rset,gx,gy,stan):
    visited = [[[0]*4 for _ in range(m)] for _ in range(n)]
    temp = set([])
    while rset or temp:
        for x,y,dire,cnt in rset:
            if stan == cnt:
                temp.add((x,y,dire,cnt))
        rset -= temp
        stan += 1
        nxt = set([])
        while temp:
            x,y,dire,cnt = temp.pop()
            for rdire,(dx,dy) in enumerate(d):
                rx,ry = x+dx, y+dy
                if 0<=rx<m and 0<=ry<n and (rx,ry) not in wall and dire != rdire and not visited[ry][rx][rdire] :
                    visited[ry][rx][rdire] = 1
                    if rx == gx and ry == gy:
                        return cnt + 1
                    nxt.add((rx,ry,rdire,cnt+1))
        temp = nxt.copy()
    return -1

def solution(sx,sy,goal):
    cx1,cy1 = goal[0]
    cx2,cy2 = goal[1]
    points = set([(sx,sy,-1)])
    visited = [[[0]*4 for _ in range(m)] for _ in range(n)]
    cnt = 0
    r11,r12 = set(),set()
    rs1, rs2 = 0,0
    while True:
        temp = set([])
        while points:
            x,y,dire = points.pop()
            for rdire,(dx,dy) in enumerate(d):
                rx,ry = x+dx, y+dy
                if 0<=rx<m and 0<=ry<n and (rx,ry) not in wall and dire != rdire and not visited[ry][rx][rdire] :
                    visited[ry][rx][rdire] = 1
                    if rx == cx1 and ry == cy1:
                        if rs1 == 0:
                            rs1 = cnt+1
                        r11.add((rx,ry,rdire,cnt+1))
                    if rx == cx2 and ry == cy2:
                        if rs2 == 0:
                            rs2 = cnt+1
                        r12.add((rx,ry,rdire,cnt+1))
                    temp.add((rx,ry,rdire))
        if not temp :
            break
        points = temp.copy()
        cnt += 1
    r1, r2 = -1,-1
    if r11:
        r1 = bfs(r11,cx2,cy2,rs1)
    if r12:
        r2 = bfs(r12,cx1,cy1,rs2)

    if r1 == -1 and r2 == -1:
        return -1
    elif r1 == -1:
        return r2
    elif r2 == -1:
        return r1
    else:
        return min(r1,r2)
        
print(solution(sx,sy,goal))
