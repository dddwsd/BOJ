'''
그 지역에 많은 비가 내렸을 때
물에 잠기지 않는 안전한 영역이 최대로 몇개가 만들어지는 지 조사

장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정

내리는 비의 양에 따른 모든 경우를 다 조사해보면 
물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우
'''
from collections import defaultdict
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
dic = defaultdict(set)
_max = 0
for y in range(n):
    for x in range(n):
        dic[matrix[y][x]].add((x,y))
        _max = max(_max,matrix[y][x])

d = [[-1,0],[1,0],[0,-1],[0,1]]
def bfs(points):
    cnt = 0
    while points:
        sx,sy = points.pop()
        area = set([(sx,sy)])
        while area:
            x,y = area.pop()
            for dx,dy in d:
                rx, ry = x+dx, y+dy
                if 0<=rx<n and 0<=ry<n and (rx,ry) in points:
                    points.remove((rx,ry))
                    area.add((rx,ry))
        cnt += 1
    return cnt

result = 0
for h in range(_max):
    points = set()
    for val in range(h+1,_max+1):
        points |= dic[val]
    result = max(result,bfs(points))
print(result)