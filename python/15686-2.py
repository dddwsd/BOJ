'''
n x n 도시

빈칸    : 0
집과    : 1
치킨집  : 2

(r,c) - (y,x) : (1,1)로 부터 시작

치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
dist = |r1 - r2| + |c1 - c2|

치킨집의 개수는 최대 M개
도시의 치킨 거리가 가장 작게 될지
'''
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
chicken = set()
houses = set()

for y in range(n):
    for x in range(n):
        if matrix[y][x] == 1:
            houses.add((y,x))
        elif matrix[y][x] == 2:
            chicken.add((y,x))

from itertools import combinations
result = n*n*n*n
for cks in list(combinations(chicken,m)):
    val = 0
    for house in houses:
        mini = n*n
        for ck in cks:
            mini = min(mini,abs(ck[0]-house[0]) + abs(ck[1]-house[1]))
        val += mini
    result = min(result,val)
print(result)
        

    




