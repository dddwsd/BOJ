'''
반지름 : 1 ~ N 
크기가 작아지는 순으로 바닥에 놓여 있고 중심은 모두 같다

원판의 반지름이 i이면, 그 원판을 i번째 원판이라고 한다.

각각의 원판에는 M개의 정수가 적혀있고,
i번째 원판에 적힌 j번째 수의 위치는 (i,j)로 표현한다.

수의 위치 - 조건
- (i,1)은 (i,2),(i,M)과 인접하다
- (i,M)은 (i,M-1), (i,1)과 인접
- (i,j)는 (i,j-1),(i,j+1)과 인접하다. (2<=j<=M-1)
- (i,j)는 (2,j)와 인접하다
- (N,j)는 (N-1,j)와 인접하다
- (i,j)는 (i-1,j),(i+1,j)와 인접하다.  (2<=i<=N-1)

원판 회전 : T번
사용변수 : xi, di, ki
1. 번호가 xi의 배수인 원판을 di 방향으로 ki칸 회전시킨다.
- di : 0 - 시계 / 1 - 반시계
2. 인접하면서 수가 같은 것들을 모두 찾는다
- 있는 경우 : 원판에서 인접하면서 같은 수를 모두 지운다
- 없는 경우 : 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.

T번 회전 후 원판에 적힌 수의 합
'''


def find(x):
	x_list, cnt = [], 1
	while True:
		if x*cnt <= n:
			x_list.append((x*cnt)-1)
		else:
			return x_list
		cnt += 1

def rotate(matrix, x_list, d, k):
	for y in x_list:
		temp = [0]*m
		for i in range(m):
			if d == 0:
				temp[(i+k) % m] = matrix[y][i]
			else:
				temp[i-k] = matrix[y][i]
		matrix[y] = temp.copy()

def check(matrix):
	remove,total,cnt = [],0,0
	for y in range(n):
		total += sum(matrix[y])
		for x in range(m):
			if matrix[y][x] != 0:
				cnt += 1
				if y != 0:
					if matrix[y][x] == matrix[y-1][x]:
						remove.extend([[x, y], [x, y-1]])
				if y != n-1:
					if matrix[y][x] == matrix[y+1][x]:
						remove.extend([[x, y], [x, y+1]])
				if matrix[y][x] == matrix[y][(x+1)%m]:
					remove.extend([[x, y], [(x+1)%m, y]])
				if matrix[y][x] == matrix[y][x-1]:
					remove.extend([[x, y], [x-1, y]])
	if remove:
		for x,y in remove:
			matrix[y][x] = 0
	else:
		if cnt != 0:
			aver = total/cnt
			for y in range(n):
				for x in range(m):
					if matrix[y][x] != 0:
						if matrix[y][x] > aver:
							matrix[y][x] -= 1
						elif matrix[y][x] < aver:
							matrix[y][x] += 1
				
n, m, t = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
for _ in range(t):
	x, d, k = map(int, input().split())
	x_list = find(x)
	rotate(matrix, x_list, d, k)
	check(matrix)
result = 0
for y in range(n):
	result += sum(matrix[y])
print(result)
