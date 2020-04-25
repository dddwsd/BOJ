'''
Two Pointer Algorithm
'''

n = int(input())
matrix = [list(input()) for _ in range(n)]
altitude = [list(map(int,input().split())) for _ in range(n)]

rest = sorted(sum(altitude,[]))

sx,sy = 0,0
_min, _max = 10000000, -1
house = set([])

length = 0

for y in range(n):
    for x in range(n):
        if matrix[y][x] != '.':
            if matrix[y][x] =='P':
                sx, sy = x, y
            house.add((x,y))
            length += 1
            _min = min(_min,altitude[y][x]) 
            _max = max(_max,altitude[y][x])

d = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def bfs(lower,upper):
    points = set([(sx,sy)])
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    while points:
        x,y = points.pop()
        for dx, dy in d:
            rx, ry = x+dx, y+dy
            if 0<=rx<n and 0<=ry<n and not visited[ry][rx] and lower<=altitude[ry][rx]<=upper:
                if (rx,ry) in house:
                    cnt += 1
                    if cnt == length:
                        return 1
                visited[ry][rx] = 1
                points.add((rx,ry))
    return 0

left = 0
left_bound = rest.index(_min)+1
right = rest.index(_max)
right_bound = n*n

result = 10000000000
while left != left_bound and right != right_bound:
    if bfs(rest[left],rest[right]):
        result = min(result,rest[right]-rest[left])
        left += 1
    else:
        right += 1
        
print(result)