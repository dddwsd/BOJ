n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

result = 1
point = set([(0,0)])
visited[0][0] = 1

d = [[-1,0],[1,0],[0,1],[0,-1]]
boundary = lambda x,y : 0 if 0<=x<m and 0<=y<n and matrix[y][x] =='1' and not visited[y][x] else  1
while True:
    temp = set([])
    while point:
        x,y = point.pop()
        for dx,dy in d:
            rx,ry = x+dx,y+dy
            if boundary(rx,ry) == 0:
                visited[y][x] = 1
                temp.add((rx,ry))
    result += 1
    if (m-1,n-1) in temp:
        break
    point = temp.copy()
         
print(result)