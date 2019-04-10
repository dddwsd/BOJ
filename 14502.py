# 연구소 크기 N*M
# 연구소는 빈 칸 + 벽
# 일부 칸은 바이러스가 존재 -> 상하좌우로 퍼져나간다
# 새로 세울 수 있는 벽의 개수는 3개 -> 꼭 3개 세워야 한다
# 0 : 빈칸 / 1 : 벽 / 2 : 바이러스
# 안전영역의 크기 최대값 구하기

# 해결 방법
# 벽을 설치해놓고 -> 바이러스를 퍼트리며 그중에 최대 확인
# 
from itertools import combinations
import pprint
import copy

n,m = map(int,input().split())
matrix = [[] for _ in range(n)]
visited = [[0]*m for _ in range(n)]
virus = set()
empty = set()
for i in range(n):
    list1 = list(map(int,input().split()))
    matrix[i] = list1
    for j in range(m):
        if list1[j] == 2:
            virus.add((j,i))
        if list1[j] == 0:
            empty.add((j,i))
check = []
check = list(combinations(empty,3))
ch = set([(-1,0),(1,0),(0,-1),(0,1)])
max_num = 0
while check:
    x,y,z = check.pop()
    matrix[x[1]][x[0]] = 1
    matrix[y[1]][y[0]] = 1
    matrix[z[1]][z[0]] = 1
    def find(matrix,visited,virus):
        t_matrix = copy.deepcopy(matrix)
        t_visited = copy.deepcopy(visited)
        t_virus = copy.deepcopy(virus)
        while t_virus:
            t_virus2 = set()
            for v_x,v_y in t_virus:
                for dx,dy in ch:
                    r_x,r_y = v_x+dx,v_y+dy
                    if r_x>=0 and r_x<m and r_y >= 0 and r_y <n and t_matrix[r_y][r_x] == 0 and t_visited[r_y][r_x] == 0:
                        t_visited[r_y][r_x] = 1
                        t_matrix[r_y][r_x] = 2
                        t_virus2.add((r_x,r_y))
            t_virus = t_virus2
        cnt = 0
        for i in range(n):
            cnt+=t_matrix[i].count(0)

        return cnt


    ck = find(matrix,visited,virus)
    matrix[x[1]][x[0]] = 0
    matrix[y[1]][y[0]] = 0
    matrix[z[1]][z[0]] = 0
    if max_num < ck:
        max_num = ck
print(max_num)
        









