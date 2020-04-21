'''
matrix = M x N
N+1의 모든 칸에는 성이 있다.

성을 지키기 위해 궁수 3명 배치
- 각 턴마다 궁수는 하나의 적을 공격 + 모든 궁수는 동시에 공격
- 공격가능한 적은 거리가 D이하인 적중 가장 가까운 적
- 거리가 동일할 경우 가장 왼쪽에 있는 적
- 여러 궁수가 같은 적을 공격 가능
- 공격받은 적은 게임에서 제외
- 궁수의 공격이 끝나면 적 이동
- 적은 한칸 이동, 성이 있는 칸으ㄹ 이동한 경우에는 게임에서 제외
- 모든 적이 격자판에서 제외되면 게임 끝

궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산
(r1,c1) , (r2,c2) 사이의 거리 |r1-r2| + |c1-c2|
'''
from itertools import combinations


n, m, d = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
t_enemy = set([])
for y in range(n-1,-1,-1):
	for x in range(m):
		if matrix[y][x] == 1:
			t_enemy.add((x,y))
arc = [[i,n] for i in range(m)]
arc = combinations(arc,3)

def dist(x1,y1,x2,y2):
	return abs(x1-x2) + abs(y1-y2)
result = 0

from copy import deepcopy

for ar1,ar2,ar3 in arc:
	val = 0
	enemy = t_enemy.copy()
	# 궁수 위치에 따른 값 계산
	while enemy:
		remove = set([])
		d1,d2,d3 = d,d,d
		save1,save2,save3 = [],[],[]
		for ex,ey in enemy:
			t1 = dist(ex,ey,ar1[0],ar1[1])
			t2 = dist(ex,ey,ar2[0],ar2[1])
			t3 = dist(ex,ey,ar3[0],ar3[1])
			if not save1 and t1 <= d1:
				d1 = t1
				save1=[ex,ey]
			elif save1:
				if t1 < d1:
					d1 = t1
					save1=[ex,ey]
				elif t1 == d1 and ex < save1[0]:
					d1 = t1
					save1=[ex,ey]

			if not save2 and t2 <= d2:
				d2 = t2
				save2=[ex,ey]
			elif save2:
				if t2 < d2:
					d2 = t2
					save2=[ex,ey]
				elif t2 == d2 and ex < save2[0]:
					d2 = t2
					save2=[ex,ey]
			
			if not save3 and t3 <= d3:
				d3 = t3
				save3=[ex,ey]
			elif save3:
				if t3 < d3:
					d3 = t3
					save3=[ex,ey]
				elif t3 == d3 and ex < save3[0]:
					d3 = t3
					save3=[ex,ey]
	
		# set으로 함으로써 궁수가 같은 적 죽이게 하기.
		if save1:
			remove.add(tuple(save1))
		if save2:
			remove.add(tuple(save2))
		if save3:
			remove.add(tuple(save3))	
		val += len(remove)
		enemy -= remove
		remove = set([])
		# y값 1씩 상승시키기
		while enemy:
			ex,ey = enemy.pop()
			if ey+1 < n:
				remove.add((ex,ey+1))
		enemy = remove.copy()
	result = max(result,val)
print(result)

