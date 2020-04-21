n,l,r = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
d = [[-1,0],[1,0],[0,1],[0,-1]]

def find_point(matrix,point):
	flag = 1
	for y in range(n):
		for x in range(n):
			for dx, dy in [[1,0],[0,1]]:
				ax, ay = x+dx, y+dy
				if 0<=ay<n and 0<=ax<n and l<=abs(matrix[ay][ax] - matrix[y][x])<=r:
					point.add((ax,ay))
					point.add((x,y))
					flag = 0
	return flag

def open_boundary(matrix,point):
	check = [[False]*n for _ in range(n)]
	while point:
		x,y = point.pop()
		near_point = set([(x,y)])
		total_point = set([(x,y)])
		check[y][x] = True
		num = 1
		val = matrix[y][x]
		while near_point:
			x,y = near_point.pop()
			for dx, dy in d:
				ax, ay = x+dx, y+dy
				if (ax,ay) in point and check[ay][ax] == False and l<= abs(matrix[ay][ax]-matrix[y][x]) <=r:
					check[ay][ax] = True
					near_point.add((ax,ay))
					total_point.add((ax,ay))
					num += 1
					val += matrix[ay][ax]
		point -= total_point
		while total_point:
			x,y = total_point.pop()
			matrix[y][x] = val//num

for result in range(2001):
	point = set([])
	if find_point(matrix,point) == 1:
		break
	print(point)
	open_boundary(matrix,point)
print(result)
