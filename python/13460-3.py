'''
알고리즘
1. 벽 / 출구 / 빨간구슬 / 파란구슬 위치를 구함
1. 상하좌우이동 10번 (해당 라인 해당 방향에 벽을 만날떄까지)
2. 벽만나는 알고리즘 : 같은 라인 벽의 위치 - 공의위치를 확인
3. 구멍만나는 알고리즘 : 같은 라인일때 공의 위치 - 구멍의 위치 & 사이에 벽이 있는가
'''
def move(x,y,dx,dy,wall,goal):
	c = 0
	while (x+dx,y+dy) not in wall and [x,y] != goal:
		x += dx
		y += dy
		c += 1
	return x,y,c

d = [[-1,0],[1,0],[0,1],[0,-1]]
def solution(ball,check,wall,goal):
	while ball:
		rx,ry,bx,by,cnt = ball.pop(0)
		for dx,dy in d :
			arx,ary,arc = move(rx,ry,dx,dy,wall,goal)
			abx,aby,abc = move(bx,by,dx,dy,wall,goal)
			if [abx,aby] == goal:
				continue
			elif [arx,ary] == goal:
				print(cnt+1)
				return
			if cnt+1 == 10 :
				continue
			if arx == abx and ary == aby:
				if arc > abc:
					arx -= dx
					ary -= dy
				else:
					abx -= dx
					aby -= dy
			if check[ary][arx][aby][abx] == False:
				check[ary][arx][aby][abx] = True
				ball.append([arx,ary,abx,aby,cnt+1])
	print(-1)



n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
wall = set([])
for y in range(n):
    for x in range(m):
        if matrix[y][x] == "#":
            wall.add((x,y))
        if matrix[y][x] == 'R':
            rx, ry = x,y
        if matrix[y][x] == "B":
            bx, by = x,y
        if matrix[y][x] == "O":
            goal = [x,y]
check[ry][rx][by][bx] = True
ball = [[rx,ry,bx,by,0]]
solution(ball,check,wall,goal)