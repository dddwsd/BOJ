n,m  = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
land = set([])
water = set([])

for y in range(n):
    for x in range(m):
        if matrix[y][x] == 1:
            land.add((x,y))
        else:
            water.add((x,y))

land_dic = {}
d = [[-1,0],[1,0],[0,-1],[0,1]]
def find(x,y,land):
    inner = set([(x,y)])
    result = set([(x,y)])
    while inner:
        x,y = inner.pop()
        for dx, dy in d:
            rx,ry = x+dx, y+dy
            if 0<= rx < m and 0<= ry < n and matrix[ry][rx] == 1 and (rx,ry) not in result:
                inner.add((rx,ry))
                result.add((rx,ry))
    land -= result
    return result

cnt = 0 
while land:
    x,y = land.pop()
    land_dic[cnt] = find(x,y,land)
    cnt += 1

dist_dic = {}

def ck_hori(x,y1,y2):
    min_y = min(y1,y2)
    max_y = max(y1,y2)
    for y in range(min_y+1,max_y):
        if (x,y) not in water:
            return 1
    if abs(y1-y2)-1 >= 2:
        return 0
    return 1

def ck_vert(y,x1,x2):
    min_x = min(x1,x2)
    max_x = max(x1,x2)
    for x in range(min_x+1,max_x):
        if (x,y) not in water:
            return 1
    if abs(x1-x2)-1 >= 2:
        return 0
    return 1

def cal_dist(land1, land2):
    dist = (n+1)*(m+1)
    for x1,y1 in land_dic[land1]:
        for x2,y2 in land_dic[land2]:
            if x1 == x2 and ck_hori(x1,y1,y2) == 0:
                dist = min(dist,abs(y1-y2)-1)
            if y1 == y2 and ck_vert(y1,x1,x2) == 0:
                dist = min(dist,abs(x1-x2)-1)
    return dist

keys = land_dic.keys()
from itertools import combinations
for land1, land2 in combinations(keys,2):
    dist = cal_dist(land1,land2)
    if dist != (n+1)*(m+1):
        dist_dic[(land1,land2)] = dist

def ck_all(keys):
    parent = [0 for _ in range(cnt)]
    no = set([])
    val = 0
    for idx,(start, end) in enumerate(keys):
        if idx == 0:
            parent[start] = 1
            parent[end] = 1
            val += dist_dic[(start,end)]
        else:
            if parent[start] == 1 or parent[end] == 1:
                parent[start] = 1
                parent[end] = 1
                val += dist_dic[(start,end)]
            else:
                no.add((start,end))
    
    while no:
        start,end = no.pop()
        if parent[start] == 1 or parent[end] == 1:
            parent[start] = 1
            parent[end] = 1
            val += dist_dic[(start,end)]
    if parent == [1]*cnt:
        return 1,val
    return 0,-1

result = -1
for keys in combinations(dist_dic,cnt-1):
    flag,dist = ck_all(keys)
    if flag == 1:
        if result == -1:
            result = dist
        else:
            result = min(result,dist)
print(result)
