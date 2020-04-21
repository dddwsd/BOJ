'''
n x n 
사용하는 말의 개수 k개

하나의 말 위에 다른 말을 올릴 수 있다.
체스판
1. 흰색
2. 빨간색
3. 파란색

k개의 말을 놓고 시작 : 1 ~ k번
이동방향도 정해져 있음 (상하좌우)

1부터 k까지 순서대로 이동
한 말이 이동할 때 위에 올려져 있는 말도 함께 이동.

말이 4개이상 쌓이게 되면 게임 종료

'''
n,k = map(int,input().split())
# 0 : 흰색 / 1 : 빨간색 / 2 : 파란색
check = [[[] for _ in range(n)] for _ in range(n)]

matrix = [list(map(int,input().split())) for _ in range(n)]
user = {}
# y,x,direc(1 : 우, 2 : 좌, 3 : 상, 4 : 하)
for i in range(k):
	y,x,direc = map(int,input().split())
	y,x = y-1,x-1
	user[i] = [x,y,direc-1]
	check[y][x].append(i)
	

cnt = 1
d = ((1,0),(-1,0),(0,-1),(0,1))
'''

이동 방식
A번 말이 이동하려는 칸
1. 흰 색 
- 그 칸으로 이동 
- 이미 말이 있으면 가장 위에 A번 올려놓는다
- A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위의 모든 말 같이 이동

2. 빨간색
- 말이 이동
- A번 말 위의 쌓여있는 모든 말의 순서를 바꾼다.

3. 파란색
- 방향을 반대로 하고 한 칸 이동한다.
- 방향을 반대로 한 후 이동하려는 칸이 파란색인 경우 이동하지 않고 방향만 반대로 바꾼다.

4. 이동하려는 곳이 체스판 밖일 경우
- 파란색과 동일하다
'''
def direc_reverse(direc):
	if direc == 0 : return 1
	elif direc == 1 : return 0
	elif direc == 2 : return 3
	else: return 2

def check_move(flag,x,y,ax,ay,index):
	# 흰
	if flag == 0:
		for user_id in check[y][x][index:]:
			user[user_id][0],user[user_id][1] = ax,ay
		check[ay][ax] += check[y][x][index:]
		check[y][x] = check[y][x][:index]
	# 빨
	elif flag == 1:
		check[ay][ax] += reversed(check[y][x][index:])
		for user_id in check[y][x][index:]:
			user[user_id][0],user[user_id][1] = ax,ay
		check[y][x] = check[y][x][:index]

def move(user_num,x,y,direc):
	index = check[y][x].index(user_num)
	dx,dy = d[direc]
	ax,ay = x+dx, y+dy
	if ax < 0 or ax >= n or ay < 0 or ay >= n:
		flag = 2
	else:
		flag = matrix[ay][ax]

	if flag == 2:
		# 방향 : 우 좌 상 하
		direc = direc_reverse(direc)
		dx,dy = d[direc]
		ax,ay = x+dx, y+dy
		if ax < 0 or ax >= n or ay < 0 or ay >= n or matrix[ay][ax] == 2:
			ax,ay = x,y
			return ax,ay,direc
	check_move(matrix[ay][ax],x,y,ax,ay,index)
	return ax,ay,direc

flag = 0
while True:
	for i in range(k):
		x,y,direc = user[i]
		x,y,direc = move(i,x,y,direc)
		user[i] = [x,y,direc]
		if len(check[y][x]) >= 4:
			flag = 1
			break
	if flag == 1:
		print(cnt)
		break
	if cnt > 1000:
		print(-1)
		break
	cnt += 1
	

