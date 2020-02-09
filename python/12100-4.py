'''
알고리즘
- matrix에서 0이 아닌 것들을 빼낸다 (one, two)
- one, two, cur = 0 으로 초기화
1. one == two
	- 두개를 더한 값을 t_matrix [cur]에 넣는다
	- one , two를 0으로 초기화
	- cur += 1
2. one != two
	- one을 t_matrix [cur]에 넣는다
	- one , two = two, matrix[?]
	- cur += 1


'''
def move_left(matrix,n):
	t_matrix = [[0]*n for y in range(n)]
	for y in range(n):
		one, two, cur = 0,0,0
		for x in range(n):
			if matrix[y][x] != 0:
				if one == 0 :
					one = matrix[y][x]
				elif two == 0:
					two = matrix[y][x]
					if one == two:
						t_matrix[y][cur] = one + two
						one,two = 0,0
						cur += 1
					else:
						t_matrix[y][cur] = one
						one,two = two,0
						cur += 1
		if two != 0:
			if one == two:
				t_matrix[y][cur] = one + two
			else:
				t_matrix[y][cur] = one
				t_matrix[y][cur+1] = two
		else:
			t_matrix[y][cur] = one
	return t_matrix			

def move_right(matrix,n):
	t_matrix = [[0]*n for y in range(n)]
	for y in range(n):
		one, two, cur = 0,0,n-1
		for x in range(n-1,-1,-1):
			if matrix[y][x] != 0:
				if one == 0 :
					one = matrix[y][x]
				elif two == 0:
					two = matrix[y][x]
					if one == two:
						t_matrix[y][cur] = one + two
						one,two = 0,0
						cur -= 1
					else:
						t_matrix[y][cur] = one
						one,two = two,0
						cur -= 1
		if two != 0:
			if one == two:
				t_matrix[y][cur] = one + two
			else:
				t_matrix[y][cur] = one
				t_matrix[y][cur-1] = two
		else:
			t_matrix[y][cur] = one
	return t_matrix		

def move_up(matrix,n):
	t_matrix = [[0]*n for y in range(n)]
	for x in range(n):
		one, two, cur = 0,0,0
		for y in range(n):
			if matrix[y][x] != 0:
				if one == 0 :
					one = matrix[y][x]
				elif two == 0:
					two = matrix[y][x]
					if one == two:
						t_matrix[cur][x] = one + two
						one,two = 0,0
						cur += 1
					else:
						t_matrix[cur][x] = one
						one,two = two,0
						cur += 1
		if two != 0:
			if one == two:
				t_matrix[cur][x] = one + two
			else:
				t_matrix[cur][x] = one
				t_matrix[cur+1][x] = two
		else:
			t_matrix[cur][x] = one
	return t_matrix		
	

def move_down(matrix,n):
	t_matrix = [[0]*n for y in range(n)]
	for x in range(n):
		one, two, cur = 0,0,n-1
		for y in range(n-1,-1,-1):
			if matrix[y][x] != 0:
				if one == 0 :
					one = matrix[y][x]
				elif two == 0:
					two = matrix[y][x]
					if one == two:
						t_matrix[cur][x] = one + two
						one,two = 0,0
						cur -= 1
					else:
						t_matrix[cur][x] = one
						one,two = two,0
						cur -= 1
		if two != 0:
			if one == two:
				t_matrix[cur][x] = one + two
			else:
				t_matrix[cur][x] = one
				t_matrix[cur-1][x] = two
		else:
			t_matrix[cur][x] = one
	return t_matrix			

def solution(matrix,n,cnt,result):
	if cnt == 5:
		for y in range(n):
			result[0] = max(result[0],max(matrix[y]))
		return 

	d = [[-1,0],[1,0],[0,-1],[0,1]]
	for dx,dy in d:
		if dx == -1:
			t_matrix = move_left(matrix,n)
		elif dx == 1:
			t_matrix = move_right(matrix,n)
		elif dy == -1 :
			t_matrix = move_up(matrix,n)
		elif dy == 1 :
			t_matrix = move_down(matrix,n)
		solution(t_matrix,n,cnt+1,result)
		

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
result = [0]
solution(matrix,n,0,result)
print(result[0])