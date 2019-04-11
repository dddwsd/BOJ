from sys import stdin
from collections import deque
input = stdin.readline

for _ in range(int(input())):
    w, h = map(int, input().split())
    a = [list(input().strip()) for _ in range(h)]
    dist = [[0]*w for _ in range(h)]
    q = deque()
    sx, sy = 0, 0
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    def bfs():
        q.append((sx, sy, 0))
        dist[sx][sy] = 1
        
        while q:
            x, y, f = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    if f is 1:
                        continue
                    print(dist[x][y])
                    return
                if dist[nx][ny] or a[nx][ny] == '#':
                    continue
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny, f))
        print("IMPOSSIBLE")

    for i in range(h):
        for j in range(w):
            if a[i][j] == '*':
                q.append((i, j, 1))
                dist[i][j] = 1
            elif a[i][j] == '@':
                sx, sy = i, j
                a[i][j] = '.'
            else:
                dist[i][j] = 0

    bfs()