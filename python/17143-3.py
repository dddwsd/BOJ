# 상 하 우 좌
dire = [-1,1,1,-1]
r,c,m = map(int,input().split())
shark,x_list = {}, {}
for i in range(1,m+1):
	y,x,s,d,z = list(map(int,input().split()))
	shark[i] = [s,d-1,z]
	if x-1 not in x_list:
		x_list[x-1] =  {}
	x_list[x-1][y-1] = i

def move(ax,ay,d,s):
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
for x in range(c):
	after = {}
	if x in x_list :
		temp = sorted(x_list[x].items())
		del x_list[x][temp[0][0]]
		result += shark[temp[0][1]][2]

	for x,item in x_list.items():
		for y,i in item.items():
			s,d,z = shark[i]
			ax,ay,ad = move(x,y,d,s)
			if ax not in after:
				after[ax] = {}
			if ay not in after[ax]:
				after[ax][ay] = i
				shark[i][1] = ad
			if ax in after and ay in after[ax]:
				if z > shark[after[ax][ay]][2]:
					after[ax][ay] = i
					shark[i][1] = ad
	x_list = after.copy()		
print(result)