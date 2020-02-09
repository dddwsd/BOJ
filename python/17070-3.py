'''
(r,c) = (행,열) = (y,x) - 각 번호는 1부터 시작

파이프 초기
- (1,1), (1,x2)

파이프 기존 방향에 따른 이동방향
1. 가로로 놓여진 경우
	(1). 오른 - 밀기
	(2). 오른아래 대각 - 밀고 회전
2. 세로로 놓여진 경우
	(1). 아래 - 밀기
	(2). 오른아래 대각 - 밀고 회전
3. 대각선으로 놓여진 경우
	(1). 오른 - 밀고 회전
	(2). 아래 - 밀고 화전
	(3). 오른아래 대각 - 밀기
'''
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
result = [[[0,0,0] for _ in range(n)] for _ in range(n)]
# result[y2][x2][dire]
# dire 
# 0 : 가로 / 1 : 세로 / 2 : 대각
result[0][1][0] = 1
for x in range(2,n):
	if matrix[0][x] == 1:
		break
	result[0][x][0] = 1

print(sum(result[0][1]))

for y in range(1,n):
	for x in range(1,n):
		# 가로
		if matrix[y][x] == 0:
			result[y][x][0] = result[y][x-1][0] + result[y][x-1][2]
		# 세로
		if matrix[y][x] == 0:
			result[y][x][1] = result[y-1][x][1] + result[y-1][x][2]
		# 대각선
		if matrix[y][x] == 0 and matrix[y][x-1] == 0 and matrix[y-1][x] == 0:
			result[y][x][2] = sum(result[y-1][x-1])

print(sum(result[n-1][n-1]))