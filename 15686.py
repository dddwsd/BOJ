# 크기가 N*N인 도시
# 빈 칸/ 치킨집 / 집
# (y,x) = (r,c)
# 치킨거리 = 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨거리는 모든 집의 치킨거리의 합
# (r1,c1) ~ (r2,c2) : |r1-r2| + |c1-c2|
# 치킨 집 중에서 최대 M개를 + 도시의 치킨거리가 가장 작게
from itertools import *

n,m = map(int,input().split())
matrix = [[0]*n for _ in range(n)]
house = []
chicken = set()
for i in range(n):
    list1 = list(map(int,input().split()))
    matrix[i] = list1
    for j in range(n):
        if list1[j] == 1:
            house.append((j,i))
        elif list1[j] == 2:
            chicken.add((j,i))

check = list(combinations(chicken,m))
total = n**n
# 치킨집을 알고 -> 집마다 치킨집의 거리의 최소를 더하면된다.

for c_point in check:
    min_house = [2*n for _ in range(len(house))]
    for i in range(len(c_point)):
        for j in range(len(house)):
            x = house[j][0] ; y = house[j][1]
            temp = abs(x-c_point[i][0]) + abs(y-c_point[i][1])
            if temp < min_house[j]:
                min_house[j] = temp
    if sum(min_house) < total:
        total = sum(min_house)


print(total)


