'''
구슬탈출
직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은다음, 
빨간 구슬을 구멍을 통해 빼내는 게임

보드 세로 N 가로 M / 가장 바깥은 막혀있음 / 보드에는 구멍이 하나
빨간 구슬 1개 파란 구슬 1개 -> 파란 구슬이 구멍에 들어가면 안댄다

중력을 이용하여 굴림 -> 상하좌우 로 기울이기
각각의 동작에서 공은 동시에 움직임
빨간 구슬이 빠지면 -> 성공
파란 구슬이 빠지면 -> 실패
둘다 구멍에 빠져도 -> 실패

빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다
기울이는 동작을 그만하는 것은 더이상 구슬이 움직일 수 없을 때까지
-> 즉 벽에 만나야 기울임이 멈춘다.

입력
n : 세로 m : 가로 3~10
n개의 줄에 m길이의 문자열
'.' : 빈칸
'#' : 벽
'o' : 구멍
'R' : 빨간 구슬
'B' : 파란 구슬
모든 보드의 가장자리에는 모두 #이 있다 구멍의 개수는 한개

10 번이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1

해결책
n*m이 주어지면 y좌표 : 1 ~ n-2 , x좌표 :1~ m-2 움직일 수 있고
움직임 -> 벽을 만날때까지
상 ,하 ,좌 ,우
빨간공이 구멍에 들어가는 방법을 찾는다. max 10
들어가지 못하면 -1
들어가는 방법을 찾으면 그 순서대로 파란공을 진행시켜서 
순서안에 파란공이 들어가면 -1 아니면 횟수 출력
'''
from copy import deepcopy

n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
visited = [[[[0]*n for _ in range(m)] for _ in range(n)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'R':
            r_x,r_y = j,i
        if matrix[i][j] == "B":
            b_x,b_y = j,i
# r_x,r_y,b_x,b_y,이동거리를 queue에 넣어줌
visited[r_x][r_y][b_x][b_y] = 1
stack = []
stack.append((r_x,r_y,b_x,b_y,0))
dx = (0,-1,0,1)
dy = (1,0,-1,0)

def move(x,dt1,y,dt2,length):
    while matrix[y+dt2][x+dt1] != '#' and matrix[y][x] != 'O':
        x += dt1
        y += dt2
        length += 1
    return x,y,length

def find():
    while stack:
        rx,ry,bx,by,dist  = stack.pop(0)
        if dist > 10:
            break
        for i in range(4):
            mrx,mry,length1 = move(rx,dx[i],ry,dy[i],0)
            mbx,mby,length2 = move(bx,dx[i],by,dy[i],0)
            if matrix[mby][mbx] == 'O':
                continue
            if matrix[mry][mrx] == 'O':
                print(dist+1)
                return
            if mrx == mbx and mry == mby:
                if length1 > length2:
                    mrx -= dx[i]
                    mry -= dy[i]
                else:
                    mbx -= dx[i]
                    mby -= dy[i]
            if visited[mrx][mry][mbx][mby] == 0:
                visited[mrx][mry][mbx][mby] = 1
                stack.append((mrx,mry,mbx,mby,dist+1))
    print(-1)
            

find()

