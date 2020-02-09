'''
이동 - 보드위의 전체 블록 상하좌우 (더 이상 이동할 수 없을 때 까지)
같은 값의 두 블록이 충돌하면 하나로 합쳐지게 된다.
한번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.

똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다.

최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램
'''
'''
알고리즘
1. matrix를 상하좌우로 다 움직여 본다.
	- 왼   : x = 0   부터 +1
	- 오른 : x = n-1 부터 -1
	- 위   : y = 0   부터 +1
	- 아래 : y = n-1 부터 -1
움직일 때 발생하는 경우
(1). 합쳐짐
(2). 현재 위치가 0일 경우 다음 것이 밀려서 들어옴
(3). 그대로 유지
3. 5번 돌린 것들의 matrix에서 최대값을 구하여 비교 후 갱신
'''

'''
도전!
t_matrix 초기화를 matrix의 0이아닌 것들로 초기화하고 
그다음에 옆으로 밀기

'''


from pprint import pprint

def move_left(matrix,n):
	t_matrix = [[matrix[y][x] for x in range(n)] for y in range(n)]
	for y in range(n):
		cur = 0 
		for x in range(1,n):
			if t_matrix[y][x] != 0:
				if t_matrix[y][cur] == 0:
					t_matrix[y][cur] = t_matrix[y][x]
					t_matrix[y][x] = 0
				else:
					if t_matrix[y][cur] == t_matrix[y][x]:
						t_matrix[y][cur] += t_matrix[y][x]
						t_matrix[y][x] = 0
						cur += 1
					else:
						cur += 1
						if t_matrix[y][cur] == 0:
							t_matrix[y][cur] = t_matrix[y][x]
							t_matrix[y][x] = 0
	return t_matrix			

def move_right(matrix,n):
	t_matrix = [[matrix[y][x] for x in range(n)] for y in range(n)]
	for y in range(n):
		cur = n-1
		for x in range(n-2,-1,-1):
			if t_matrix[y][x] != 0:
				if t_matrix[y][cur] == 0:
					t_matrix[y][cur] = t_matrix[y][x]
					t_matrix[y][x] = 0
				else:
					if t_matrix[y][cur] == t_matrix[y][x]:
						t_matrix[y][cur] += t_matrix[y][x]
						t_matrix[y][x] = 0
						cur -= 1
					else:
						cur -= 1
						if t_matrix[y][cur] == 0:
							t_matrix[y][cur] = t_matrix[y][x]
							t_matrix[y][x] = 0
	return t_matrix

def move_up(matrix,n):
	'''print("---------------------------------")
	print("up")'''
	t_matrix = [[matrix[y][x] for x in range(n)] for y in range(n)]
	for x in range(n):
		cur = 0 
		for y in range(1,n):
			if t_matrix[y][x] != 0:
				if t_matrix[cur][x] == 0:
					t_matrix[cur][x] = t_matrix[y][x]
					t_matrix[y][x] = 0
				else:
					if t_matrix[cur][x] == t_matrix[y][x]:
						t_matrix[cur][x] += t_matrix[y][x]
						t_matrix[y][x] = 0
						cur += 1
					else:
						cur += 1
						if t_matrix[cur][x] == 0:
							t_matrix[cur][x] = t_matrix[y][x]
							t_matrix[y][x] = 0
	return t_matrix
	

def move_down(matrix,n):
	'''print("---------------------------------")
	print("down")'''
	t_matrix = [[matrix[y][x] for x in range(n)] for y in range(n)]
	for x in range(n):
		cur = n-1 
		for y in range(n-2,-1,-1):
			if t_matrix[y][x] != 0:
				if t_matrix[cur][x] == 0:
					t_matrix[cur][x] = t_matrix[y][x]
					t_matrix[y][x] = 0
				else:
					if t_matrix[cur][x] == t_matrix[y][x]:
						t_matrix[cur][x] += t_matrix[y][x]
						t_matrix[y][x] = 0
						cur -= 1
					else:
						cur -= 1
						if t_matrix[cur][x] == 0:
							t_matrix[cur][x] = t_matrix[y][x]
							t_matrix[y][x] = 0
	return t_matrix

def solution(matrix,n,cnt,result):
	if cnt == 5:
		pprint(matrix)
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