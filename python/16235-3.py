'''
n x n 땅
(r,c) = (y,x) 
(1,1) 부터 시작

가장 처음 양분 : 모든칸에 5

같은 칸에 여러 개의 나무가 심어져 있을 수 도 있다
나무 m 개
'''
from collections import deque
n,m,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
matrix = [[5]*n for _ in range(n)]
tree = [[{} for _ in range(n)] for _ in range(n)]
for _ in range(m):
	y,x,z = map(int,input().split())
	if z not in tree[y-1][x-1]:
		tree[y-1][x-1][z] = 1

d = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def solution(matrix,tree,a):
	temp = [[{} for _ in range(n)] for _ in range(n)]
	for y in range(n):
		for x in range(n):
			if not tree[y][x] :
				matrix[y][x] += a[y][x]
				continue
			die = 0
			spread = 0
			for age,num in sorted(tree[y][x].items()):
				cnt = matrix[y][x]//age
				if cnt >= num:
					matrix[y][x] -= age*num
					if age+1 not in temp[y][x]:
						temp[y][x][age+1] = 0
					temp[y][x][age+1] += num
					if (age+1) % 5 == 0:
						spread += num
				elif 1<= cnt < num:
					matrix[y][x] -= age*cnt
					if age+1 not in temp[y][x]:
						temp[y][x][age+1] = 0
					temp[y][x][age+1] += cnt
					die += (age//2)*(num-cnt)
					if (age+1) % 5 == 0:
						spread += cnt
				else:
					die += (age//2)*num
			if spread != 0:
				for dx,dy in d:
					ax,ay = x+dx, y+dy
					if 0<= ax < n and 0 <= ay < n:
						if 1 not in temp[ay][ax] :
							temp[ay][ax][1] = 0
						temp[ay][ax][1] += spread
			matrix[y][x] += a[y][x] + die
	return temp
			

'''
k년이 지난 후 상도의 땅에 살아있는 나무의 개수
'''
from pprint import pprint
for _ in range(k):	
	tree = solution(matrix,tree,a)

result = 0
for y in range(n):
	for x in range(n):
		result += sum(tree[y][x].values())
print(result)