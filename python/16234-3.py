'''
n x n 
(c,r) -> A[r][c] 명이 살고 있다

인구이동 - 인구이동이 더 이상 없을 때 까지
1. 국경선을 공유하는 두 나라의 인구차이가 L명이상 R명 이하 하루동안 국경선 연다
2. 인구이동 시작
3. 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 연합이라 한다.
4. 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루는 칸의 개수)
5. 연합을 해체하고 국경선을 닫는다.

인구이동이 몇번 발생
'''
n,l,r = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
d = [[1,0],[-1,0],[0,1],[0,-1]]

def open_boundary(matrix,check,x,y):			
	flag = 0
	num = 1
	val = matrix[y][x]
	near_set = set([(x,y)])
	total_set = set([(x,y)])
	while near_set:
		x,y = near_set.pop()
		for dx,dy in d:
			ax,ay = x+dx, y+dy
			if 0<=ax<n and 0<=ay<n and check[ay][ax] == 0 and l<=abs(matrix[ay][ax]-matrix[y][x])<=r:
				check[ay][ax] = True
				num += 1
				val += matrix[ay][ax]
				near_set.add((ax,ay))
				total_set.add((ax,ay))
	if num > 1:
		flag = 1
		while total_set:
			x,y = total_set.pop()
			matrix[y][x] = val//num
	return flag

for cnt in range(2001):
	check = [[False]*n for _ in range(n)]
	flag = 0
	for y in range(n):
		for x in range(n):
			if check[y][x] == False:
				check[y][x] = True
				flag += open_boundary(matrix,check,x,y)
	if flag == 0:
		break
print(cnt)





