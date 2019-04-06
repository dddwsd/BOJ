# 빈 공간과 벽으로 이루어진 건물에 갇힘
# 건물의 일부에는 불이 났고,
# 상근이는 출구를 향해 뛰고 있다

# 매 초마다 불은 동서남북으로 펴져나간다
# 벽에는 불이 붙지 x
# 상근이는 동서남북 인접한 칸으로 이동할 수 있으며 1초가 걸림
# 상근이는 벽을 통과할 수 없고 
# 불이 붙거나 붙으려는 칸으로 이동x
# 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동 가능
# 얼마나 빨리 빌딩을 탈출할 수 있는지

#입력
# tc
# w,h
# h개줄의 w개의 문자
# . : 빈공간
# # : 벽
# @ : 시작위치
# * : 불

# 출력
# 가장빠른 시간 / 탈출할 수 없을 경우 IMPOSSIBLE
from pprint import *
dx = (-1,0,1,0)
dy = (0,1,0,-1)
temp_x = 0
temp_y = 0
def find(stack_f,stack_p):
    while stack_f | stack_p:
        # 불이 이동하고 사람이 따라옴
        # 사람이 있는 위치에 불이 올 수 있음
        # 불이 있는 위치로 사람은 갈 수 없음
        stack_f2 = set()
        stack_p2 = set()
        #print(stack)
        for x,y in stack_f:
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if nx<0 or nx>=w or  ny <0 or ny>=h:
                    continue            
                if matrix[ny][nx] == '#' or dist[ny][nx] != 0:
                    continue
                dist[ny][nx] = -1
                stack_f2.add((nx,ny))
        for x,y in stack_p:
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if nx<0 or nx>=w or  ny <0 or ny>=h:
                    print(dist[y][x])
                    return
                if matrix[ny][nx] == '#' or dist[ny][nx] != 0:
                    continue
                dist[ny][nx] = dist[y][x] +1
                stack_p2.add((nx,ny))        
        stack_f = stack_f2
        stack_p = stack_p2
    print("IMPOSSIBLE")
    return 

for _ in range(int(input())):
    w,h = map(int,input().split())
    matrix = [list(input().strip()) for _ in range(h)]
    dist = [[0]*w for _ in range(h)]
    stack_f = set()
    stack_p = set()
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '*':
                stack_f.add((j,i))
                dist[i][j] = -1
            elif matrix[i][j] == '@':
                stack_p.add((j,i))
                dist[i][j] = 1
            else:
                dist[i][j] = 0
    find(stack_f,stack_p)