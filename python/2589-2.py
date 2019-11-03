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
d = [[0,1],[0,-1],[1,0],[-1,0]]
def find(matrix,visited):
    # matrix = (x,y) 형식으로 저장되어 있다
    # 상 : x, y+1 (단 y+1 < row)
    # 하 : x, y-1 (단 y-1 > -1)
    # 좌 : x-1, y (단 x-1 > -1)
    # 우 : x+1, y (단 x+1 < col)
    check = [[False]*col for _ in range(row)]
    check[visited[0][1]][visited[0][0]] = True
    cnt = 0
    while visited:
        x,y,dist = visited.pop(0)
        cnt = max(cnt,dist)
        for dx,dy in d:
            nx ,ny = x+dx,y+dy
            if 0<= nx < col and 0<= ny < row and matrix[ny][nx] == 'L' and check[ny][nx] == False:
                visited.append([nx,ny,dist+1])
                check[ny][nx] = True
    return cnt
    
row,col = map(int,input().split())
matrix = [ list(input()) for _ in range(row)]
print(matrix)
result = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] == 'L':
            result = max(result,find(matrix,[[j,i,0]]))
print(result)

    
