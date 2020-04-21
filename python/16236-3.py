'''
n x n 
물고기 : m
아기상어 : 1
한칸에는 물고기가 최대 1마리 존재한다.

아기상어 처음 크기 : 2
아기상어는 1초에 상하좌우로 움직인다.
- 자기보다 더 물고기 있으면 지나갈 수 없다
- 자신의 크기보다 작은 물고기만 먹을 수 있따
- 크기가 같으면 먹을 수 없지만 지나갈 수 있다

이동 방법
1. 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마상어에게 도움
2. 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
3. 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹는다.
	- 거리는 아기 상어가 있는 칸에서 물고기 칸까지 칸의 개수
	- (위, 왼) 순으로

물고기 먹으면 빈 칸이 된다.
자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1증가

엄마 상어에게 도움을 요청하지 않고 물고기를 잡아 먹을 수 있는가
'''
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
	for j in range(n):
		if matrix[i][j] == 9:
			sx,sy,ss = j,i,2

d = [[-1,0],[1,0],[0,1],[0,-1]]
def eat(sx,sy,ss):
	check = [[False]*n for _ in range(n)]
	check[sy][sx] = True
	point = set([(sx,sy)])
	cnt, flag = 0, 0
	rx,ry = n,n
	while True:
		cnt += 1
		route = set([])
		while point:
			x,y = point.pop()
			for dx,dy in d:
				ax,ay = x+dx, y+dy
				if 0 <= ax < n and 0 <= ay < n and check[ay][ax] == False:
					check[ay][ax] = True
					if matrix[ay][ax] == 0:
						route.add((ax,ay))
					elif matrix[ay][ax] < ss:
						flag = 1
						if ay < ry :
							ry, rx = ay, ax
						elif ay == ry and ax < rx :
							ry, rx = ay, ax
					elif matrix[ay][ax] == ss:
						route.add((ax,ay))
		if flag == 1:
			matrix[sy][sx] = 0
			matrix[ry][rx] = 9
			return rx,ry,cnt
		if route :
			point = route.copy()
		else:
			return -1,-1,-1

result = 0		
eat_fish = 0
while True:
	sx,sy, time = eat(sx,sy,ss)
	if time == -1:
		break
	eat_fish += 1
	result += time
	if eat_fish == ss:
		ss += 1
		eat_fish = 0
print(result)