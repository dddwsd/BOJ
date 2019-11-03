'''
미로 : n x m
(1). 빈방 : 자유롭게 다닐 수 있지만
(2). 벽   : 부수지 않으면 이동할 수 없다.

운영진 : 여러명
항상 모두 같은 방에 있음 -> 여러 명이 다른 방에 있을 수는 없다.
어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 방 -> 미로 밖은 안댐

벽은 평소에는 이동 x
-> 알고스팟의 무기 AOJ를 이용해 벽을 부술 수 있다
-> 벽을 부수면 = 빈 방

(1,1)에 있는 운영진이 (n,m)으로 이동하려면 벽을 최소 몇개 부셔야 하는가?
'''
'''
입력
1. M , N 
2. 0은 빈방 / 1은 벽
'''
from pprint import pprint
d = [[1,0],[-1,0],[0,1],[0,-1]]
def solution(matrix,check,point):
    wall = []
    crush = 0
    while True:
        x,y = point.pop(0)
        if x == m-1 and y == n-1:
            return crush
        for dx,dy in d:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and check[ny][nx] == False:
                if matrix[ny][nx] == 1:
                    wall.append([nx,ny])
                else:
                    point.append([nx,ny])
                check[ny][nx] = True
        if not point and wall:
            # 막혀있을 때
            point = wall
            wall = []
            crush += 1

m, n = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(n)]
check = [[False]*m for _ in range(n)]
check[0][0] = True
result = solution(matrix,check,[[0,0]])
print(result)