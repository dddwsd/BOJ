'''
원숭이 -> 말

말의 움직임 유심히 살펴보고 그대로 따라하기로
말은 말

말은 격자판에서 체스의 나이트와 같은 이동방식을 가진다.
말은 장애물을 뛰어넘을 수 있따

원숭이는 k번만 말처럼 움직일 수 있고, 그 외에는 인접한 칸으로만 움직일 수 있다.
격자판 맨 왼쪽 위에서 맨 오른 아래까지 가야한다.
최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 프로그램

원숭이는 장애물을 통과할 수 없다
0 : 평지 / 1 : 장애물
'''
from collections import deque

num = int(input())
w,h = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(h)]
dist = [[[0]*(num+1) for _ in range(w)] for _ in range(h)]

points = deque([[0,0,num]])
result = 0

d = [[-1,0],[1,0],[0,-1],[0,1]]
hd = [[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,-1],[-2,1]]
boundary = lambda x,y,k : 0 if 0<= x < w and 0 <= y < h \
    and matrix[y][x] == 0 and dist[y][x][k] == 0 else 1

def find(points,dist):
    while points:
        x,y,k = points.popleft()
        if x == w-1 and y == h-1:
            return dist[y][x][k]
        # 말처럼 움직이는거
        if k > 0:
            for dx,dy in hd:
                rx,ry,rk = x+dx,y+dy,k-1
                if boundary(rx,ry,rk) == 0:
                    dist[ry][rx][rk] = dist[y][x][k] + 1
                    points.append([rx,ry,rk])
        # 인접한 칸 움직이는거
        for dx, dy in d:
            rx, ry = x+dx, y+dy
            if boundary(rx, ry, k) == 0:
                dist[ry][rx][k] = dist[y][x][k] + 1
                points.append([rx,ry,k])
    return -1

print(find(points,dist))
    



