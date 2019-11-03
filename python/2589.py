'''
지도 : 직사각형
각칸 : 육지(L) & 바다(W)
이동 : 상 하 좌 우 -> 한칸에 1시간
보물 : 최단거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다
최단거리 -> 같은 곳을 두번지나거나 멀리 돌아가서는 안된다.
'''

'''
입력 
1. 세로 가로
2. 지도가 주어짐
(각 칸 사이 빈칸 없다)
'''

'''
출력
1. 최단거리로 이동하는 시간
'''

'''
풀이
1. 각 점마다의 최대 길이를 구한다
2. 끝났을때 최대 값들 중 제일 큰 값을 구한다.
3. -1이 아닌 인접한 칸으로 번져 나갈떄 0이 아니라면 번지지 않는다.

'''
from collections import deque

def find(matrix,visited):
    # point = (x,y) 형식으로 저장되어 있다
    # 상 : x, y+1 (단 y+1 < row)
    # 하 : x, y-1 (단 y-1 > -1)
    # 좌 : x-1, y (단 x-1 > -1)
    # 우 : x+1, y (단 x+1 < col)
    check = [[False]*col for _ in range(row)]
    check[visited[0][1]][visited[0][0]] = True
    cnt = 0
    while visited:
        x,y,dist = visited.popleft()
        cnt = max(cnt,dist)
        if y+1 < row and matrix[y+1][x] == 'L' and check[y+1][x] == False:
            visited.append([x,y+1,dist+1])
            check[y+1][x] = True
        if y-1 > -1 and matrix[y-1][x] == 'L' and check[y-1][x] == False:
            visited.append([x,y-1,dist+1])
            check[y-1][x] = True
        if x+1 < col and matrix[y][x+1] == 'L' and check[y][x+1] == False:
            visited.append([x+1,y,dist+1])
            check[y][x+1] = True
        if x-1 > -1 and matrix[y][x-1] == 'L' and check[y][x-1] == False:
            visited.append([x-1,y,dist+1])
            check[y][x-1] = True
    return cnt
    


row,col = map(int,input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
result = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] == 'L':
            result = max(result,find(matrix,deque([[j,i,0]])))
print(result)

    
