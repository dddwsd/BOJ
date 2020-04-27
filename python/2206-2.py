'''
matrix : n x m 

0 : 이동할 수 있는 곳
1 : 이동할 수 없는 벽

(1,1) -> (n,m)

최단 경로

시작하는 칸 + 끝나는 칸

한개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면 한개까지 가능
'''

n,m = map(int,input().split())

matrix = [list(input()) for _ in range(n)]
visited = [[[0,0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
sx,sy = 0,0
ex,ey = m-1,n-1

from collections import deque
def bfs():
    d = [[-1,0],[1,0],[0,1],[0,-1]]
    points = deque([[sx,sy,0,0]])

    while points: 
        x,y,_type,cnt = points.popleft()
        if x == ex and y == ey:
            return cnt+1
        for dx,dy in d:
            rx, ry = x+dx, y+dy
            if 0<=rx<m and 0<=ry<n:
                if matrix[ry][rx] == '0':
                    if visited[ry][rx][_type] == 0 :
                        visited[ry][rx][_type] = 1
                        points.append([rx,ry,_type,cnt+1])
                else:
                    if _type == 0 :
                        if visited[ry][rx][_type+1] == 0: 
                            visited[ry][rx][_type+1] = 1
                            points.append([rx,ry,_type+1,cnt+1])
    return -1



print(bfs())




