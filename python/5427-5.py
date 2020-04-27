'''
건물 일부에 불이 났고 상근이 출구향해 run

불은 동서남북
벽에는 불 붙지 x

벽을 통과 x
불이 옮겨진 칸 or 이제 불이 붙으려는 칸으로 이동할 수 없다
상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.

. : 빈 공간
# : 벽
@ : 상근이의 시작 위치
* : 불

탈출할 수 없을 때 impossible

1. 불 이동
2. 상근이 이동
'''
from collections import deque
tc = int(input())
d = [[-1,0],[1,0],[0,-1],[0,1]]

for _ in range(tc):
    w,h = map(int,input().split())
    matrix = [list(input()) for _ in range(h)]
    fire = set([])
    for y in range(h):
        for x in range(w):
            if matrix[y][x] == '*':
                fire.add((x,y))
            if matrix[y][x] == '@':
                sx,sy = x,y
                matrix[y][x] = '.'

    bound = lambda x,y : 1 if 0<=x<w and 0<=y<h and matrix[y][x] == '.' else 0

    def upgrade_fire(fire,matrix):
        temp = set([])
        while fire:
            x,y = fire.pop()
            for dx,dy in d:
                rx,ry = x+dx, y+dy
                if bound(rx,ry):
                    matrix[ry][rx] = '*'
                    temp.add((rx,ry))
        return temp

    def bfs(fire,matrix):
        cnt = 0
        visited = [[0]*w for _ in range(h)]
        visited[sy][sx] = 1
        points = set([(sx,sy)])

        while True:
            fire = upgrade_fire(fire,matrix)
            temp = set([])
            while points:
                x,y = points.pop()
                if x == 0 or y == 0 or x == w-1 or y == h-1:
                    return cnt+1
                for dx,dy in d:
                    rx,ry = x+dx,y+dy
                    if bound(rx,ry) and visited[ry][rx] == 0:
                        visited[ry][rx] = 1
                        temp.add((rx,ry))
            if not temp:
                return "IMPOSSIBLE"
            points = temp.copy()
            cnt += 1
    print(bfs(fire,matrix))