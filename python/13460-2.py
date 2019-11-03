''''''
'''
직사각형 보드
빨간구슬 & 파란구슬 1개씩
빨간 구슬을 구멍을 통해 빼내는 게임

세로 N / 가로 M
보드에 구멍이 1개
파란 구슬이 구멍에 들어가면 안된다.

상하좌우 기울이기 가능 -> 더이상 구슬이 움직이지 않을 때 까지
두개의 공이 동시에 움직인다
1. 빨간 구슬이 빠지면 성공
2. 파란 구슬이 빠지면 실패
3. 동시에 구멍에 빠져도 실패
'''
'''
입력
1. N M
2. N개줄 M길이의 문자열
. : 빈칸
# : 벽
O : 구멍
R : 빨간구슬
B : 파란구슬
'''
'''
알고리즘
1. 벽 / 출구 / 빨간구슬 / 파란구슬 위치를 구함
1. 상하좌우이동 10번 (해당 라인 해당 방향에 벽을 만날떄까지)
2. 벽만나는 알고리즘 : 같은 라인 벽의 위치 - 공의위치를 확인
3. 구멍만나는 알고리즘 : 같은 라인일때 공의 위치 - 구멍의 위치 & 사이에 벽이 있는가
'''
from collections import deque

d = [[-1,0],[1,0],[0,1],[0,-1]]

def move(x,y,dx,dy,c):
    while [x+dx,y+dy] not in wall and [x,y] != goal:
        x += dx
        y += dy
        c += 1
    return x,y,c

def solution(ball,check):
    while ball:
        r_x,r_y,b_x,b_y,cnt = ball.popleft()
        for dx,dy in d:
            arx,ary,arc = move(r_x,r_y,dx,dy,0)
            abx,aby,abc = move(b_x,b_y,dx,dy,0)
            if [abx,aby] == goal:
                continue
            if [arx,ary] == goal:
                print(cnt+1)
                return
            if arx == abx and ary == aby:
                if arc > abc:
                    arx -= dx
                    ary -= dy
                else:
                    abx -= dx
                    aby -= dy
            if cnt+1 < 10 and check[ary][arx][aby][abx] == False:
                check[ary][arx][aby][abx] = True
                ball.append([arx,ary,abx,aby,cnt+1])
    print(-1)

n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
wall = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "#":
            wall.append([j,i])
        if matrix[i][j] == 'R':
            r_x, r_y = j,i
        if matrix[i][j] == "B":
            b_x, b_y = j,i
        if matrix[i][j] == "O":
            goal = [j,i]
check[r_y][r_x][b_y][b_x] = True
ball = deque([[r_x,r_y,b_x,b_y,0]])
solution(ball,check)




