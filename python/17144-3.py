'''
(r,c) = (y,x)

공기청정기 항상 왼쪽 열 - 크기 두행 

1초 동안 일어난 일
1. 미세먼지 확산
	- (r,c)에 있는 미세먼지 상하좌우 확산
	- 인접한 방향에 공기청정기 or 칸이 없으면 확산 x
	- 확산되는 양 : int(A[r][c]/5)
	- 남은 미세먼지 양 A[r][c] - int(A[r][c]/5) * (확산된 방향)

2. 공기청정기 작동
	- 바람 나옴
	- 위쪽은 반시계 아래쪽은 시계방향
	- 바람이 불면 미세먼지가 바람의 방향대로 한칸 이동
	- 공기청정기로 들어간 미세먼지는 모두 정화된다.
'''
r,c,t = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(r)]
dust = set([])
cleaner = []
for y in range(r):
	for x in range(c):
		if matrix[y][x] == -1:
			cleaner.append(y)

d = [[-1,0],[1,0],[0,1],[0,-1]]

def spread(matrix,cleaner):
	t_matrix = [[0]*c for _ in range(r)]
	for y in range(r):
		for x in range(c):
			if matrix[y][x] > 0:
				val = matrix[y][x]//5
				if val == 0 : 
					t_matrix[y][x] += matrix[y][x]
					continue
				cnt = 0
				for dx, dy in d:
					ax, ay = x+dx, y+dy
					if ax == 0 and ay in cleaner:
						continue
					elif 0 <= ax < c and 0 <= ay < r:
						cnt += 1
						t_matrix[ay][ax] += val
				t_matrix[y][x] += matrix[y][x] - val*cnt
				
	return t_matrix

def clean(matrix,cleaner):
	cy1,cy2 = cleaner
	for y in range(cy1-1,0,-1):
		matrix[y][0] = matrix[y-1][0]
	for y in range(cy2+1,r-1):
		matrix[y][0] = matrix[y+1][0]

	matrix[0][0:c-1] = matrix[0][1:c]
	matrix[r-1][0:c-1] = matrix[r-1][1:c]
	
	for y in range(cy1):
		matrix[y][c-1] = matrix[y+1][c-1]
	for y in range(r-1,cy2,-1):
		matrix[y][c-1] = matrix[y-1][c-1]
	matrix[cy1][2:c] = matrix[cy1][1:c-1]
	matrix[cy2][2:c] = matrix[cy2][1:c-1]

	matrix[cy1][1] = 0
	matrix[cy2][1] = 0
	

	

from pprint import pprint
for _ in range(t):
	matrix = spread(matrix,cleaner)
	clean(matrix,cleaner)

result = 0
for item in matrix:
	result += sum(item)
print(result)

