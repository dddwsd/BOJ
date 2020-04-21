'''
matrix : r x c 
각 칸은 (r,c) = (행, 열) = (y, x)

칸에는 상어가 최대 한마리
상어 : 크기 , 속도


1초 동안 일어나는 일
1. 낚시왕 오른쪽으로 + 1
2. 가장 위에 있는 상어를 잡는다. -> 잡으면 격자판에서 사라진다.
3. 상어가 이동

상어의 이동
1. 상어는 속도만큼 이동
2. 이동하려는 칸이 범위를 벗어나면 방향을 바꿔서 남은 것 이동
3. 모든 상어가 이동을 마친 후에 한 칸에 두마리 상어가 있으면 큰 거만 남김

낚시왕이 잡은 상어 크기의 합.
'''

dire = [-1,1,1,-1]
r,c,m = map(int,input().split())
shark = {}
for i in range(1,m+1):
	y,x,s,d,z = list(map(int,input().split()))
	if x-1 not in shark:
		shark[x-1] = {}
	shark[x-1][y-1] = [i,s,d-1,z]


# 상 하 우 좌
def move(ax,ay,temp):
	d,s = temp[2],temp[1]
	mv = dire[d] * s
	if d == 0 or d == 1:
		if 0<= ay + mv < r:
			ay  = ay+mv
		else:
			d = 1
			ay = (abs(ay + mv)) % (2*r-2)
			if ay // (r-1) == 1:
				ay = (r-1) - ay%(r-1)
				d = 0
	else:
		if 0 <= ax + mv < c:
			ax = ax + mv
		else:
			ax = (abs(ax + mv)) % (2*c-2)
			d = 2
			if ax // (c-1) == 1:
				ax = (c-1) - ax%(c-1)
				d = 3
	return ax,ay,d

result = 0

# 2 , 1
# 2 , 3

for x in range(c):
	after = {}
	# eat
	if x in shark and shark[x]:
		temp = sorted(shark[x].items())
		del shark[x][temp[0][0]]
		result += temp[0][1][3]
	# move
	for x,item in shark.items():
		# x,{y:[i,s,d,z]}
		if not item:
			continue
		for y,temp in item.items():
			ax,ay,ad = move(x,y,temp)
			print("ax = {} ay = {} ad = {}".format(ax,ay,ad))
			if ax not in after:
				after[ax] = {}
			if ay not in after[ax]:
				after[ax][ay] = [temp[0],temp[1],ad,temp[3]]
			if ax in after and ay in after[ax]:
				if temp[3] > after[ax][ay][3]:
					after[ax][ay] = [temp[0],temp[1],ad,temp[3]]

	shark = after.copy()
		
print(result)
	

	


