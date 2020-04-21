'''
바이러스 : 활성화 / 비활성화
맨 처음 : 모든 바이러스 비활성 상태

활성 상태인 바이러스는 
1초 : 상하좌우로 인접한 모든 빈 칸으로 동시에 복제
승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.

연구소 크기 
N x N
0 : 빈칸
1 : 벽
2 : 바이러스

활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간
'''

from itertools import combinations
d = [[1,0],[-1,0],[0,1],[0,-1]]
n,m = map(int,input().split())
matrix,empty,wall,virus = [],set([]),set([]),set([])
for y in range(n):
	temp = list(map(int,input().split()))
	matrix.append(temp)
	for x in range(n):
		if temp[x] == 0:
			empty.add((x,y))
		elif temp[x] == 1:
			wall.add((x,y))
		else:
			virus.add((x,y))

'''
알고리즘 - bfs
1. combination을 통해 바이러스의 위치를 지정
2. 해당위치에서 시작하여 한칸씩 넓힘
3-1. 넓힌 칸이 벽이나 visit에 속하면 continue
3-2. 넓힌 칸이 빈칸이면 flag = 1설정 & set 과 visit에 넣어줌
3-3. 넓힌 칸이 바이러스면 set과 visit에 넣어줌
4. set에 아무것도 있지 않다면 무한루프 정지
5. empty + virus - visit == 0 이면 result갱신
6. empty + virus - visit != 0 이면 -1
'''

def find(point,empty,wall,virus,result):
	cnt = 0
	output = 0
	visit = point.copy()
	while True:
		temp = set([])
		flag = 0
		while point:
			x,y = point.pop()
			for dx,dy in d:
				ax,ay = x+dx, y+dy
				if ax<0 or ax>=n or ay<0 or ay>= n:
					continue
				elif (ax,ay) in wall or (ax,ay) in visit:
					continue
				elif (ax,ay) in empty:
					flag = 1
				temp.add((ax,ay))
				visit.add((ax,ay))
		if not temp:
			break
		point = temp.copy()
		cnt += 1
		if flag == 1:
			output = cnt
		
	if visit & empty == empty:
		if result[0] == -1:
			result[0] = output
		else:
			result[0] = min(result[0],output)



result = [-1]
for start_point in list(combinations(virus,m)):
	find(set(start_point),empty.copy(),wall,virus.copy(),result)
print(result[0])

	
	
		
