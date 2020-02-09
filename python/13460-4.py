def move(x,y,c,ox,oy,wall,dx,dy):
	while (x+dx,y+dy) not in wall and (x,y) != (ox,oy):
		x += dx
		y += dy
		c += 1
	return x,y,c

def solution(stack,wall,check,ox,oy):
	d = [[-1,0],[1,0],[0,1],[0,-1]]
	while stack:
		bx,by,rx,ry,cnt = stack.pop(0)
		for dx,dy in d:
			arx,ary,arc = move(rx,ry,0,ox,oy,wall,dx,dy)
			abx,aby,abc = move(bx,by,0,ox,oy,wall,dx,dy)
			if abx == ox and aby == oy:
				continue
			elif arx == ox and ary == oy:
				print(cnt+1)
				return
			elif cnt == 9:
				continue
			elif arx == abx and ary == aby :
				if arc > abc :
					arx -= dx
					ary -= dy
				else:
					abx -= dx
					aby -= dy
			if check[ary][arx][aby][abx] == False:
				check[ary][arx][aby][abx] = True
				stack.append([abx,aby,arx,ary,cnt+1])
	print(-1)



n, m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
wall = set([])
for y in range(n) : 
	for x in range(m):
		if matrix[y][x] == '#':
			wall.add((x,y))
		elif matrix[y][x] == 'O':
			ox,oy = x,y
		elif matrix[y][x] == 'B':
			bx,by = x,y
		elif matrix[y][x] == "R":
			rx,ry = x,y

stack = [[bx,by,rx,ry,0]]
solution(stack,wall,check,ox,oy)
			
