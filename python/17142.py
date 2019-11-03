''''''
'''
바이러스 -> default : 비활성상태
활성상태 : 상하좌우로 인접한 모든 빈칸으로 동시에 복제 -> 1초가 걸린다
1. 상 : x,y-1
2. 하 : x,y+1
3. 좌 : x-1,y
4. 우 : x+1,y
check[i][j] = True -> 포인트에 포함 x

바이러스 M개를 활성상태(시작 포인트)로 변경하려 한다
연구소 NxN
빈칸(0) or 벽(1) or 바이러스를 놓을 수 있는 위치(2)

모든 빈칸!에 바이러스를 퍼뜨리는 최소 시간을 구하자
1. check배열 -> 벽은 True
2. point : 시작점의 집합
3. combination 함수 사용으로 시작위치 설정 -> start
4. 시작점에서 바이러스 퍼지기 시작
5. 바이러스가 빈칸으로 퍼질때 -> start에 포함
6. 바이러스가 비활성 바이러스에 퍼질떄 -> start에 포함시키지만  full은 차감x
'''
from itertools import combinations
from collections import deque
from pprint import pprint
d = [[0,-1],[0,1],[-1,0],[1,0]]
def solution(full):
    global matrix,start
    check = [[False] * n for _ in range(n)]
    for x,y in start:
        check[y][x] = True
    cnt = 0
    while full != 0:
        length = len(start)
        for _ in range(length):
            x,y = start.popleft()
            for dx,dy in d:
                nx, ny = x + dx , y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    temp = matrix[ny][nx]
                    if check[ny][nx] == False:
                        if temp == 1:
                            check[ny][nx] = True
                        else:
                            start.append([nx,ny])
                            check[ny][nx] = True
                            if temp == 0:
                                full -= 1
        if not start and full > 0 :
            return -1
        cnt +=1
    return cnt

n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
point,empty,full,result = [],[],n*n,[]
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            full = full-1
            if matrix[i][j] == 2:
                point.append([j,i])

for start in list(combinations(point,m)):
    start = deque(start)
    val = solution(full)
    if val != -1:
        result.append(val)
if result:
    print(min(result))
else:
    print(-1)