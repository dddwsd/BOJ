from copy import deepcopy
'''
n*n 크기의 땅
각 땅에는 나라가 하나씩 존재
r행 c열 나라 -> A[r][c]명이 살고 있음

인구이동
아래 방법에 의해 인구 이동이 없을때까지 지속
1. 국경선을 공유하는 두 나라의 인구차이가 L <=  <= R 이면 국경선을 하루 연다
2. 국경선 열리면 인구이동 시작
3. 인접한 칸만을 이용해 이동할 수 있으면, 그나라를 오늘 하루 동안 '연합'이라함
4. 연합 각 칸의 인구수 (연합의 인구수)/(연합을 이루고 있는 칸의 개수)
5. 연합 해체 , 국경선 닫는다

몇 번의 인구이동 발생?
'''
n,l,r = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

'''
해결방안
1. 국경선이 열리는 나라들의 모임을 set으로 저장 -> bfs
2. set들이 다 저장되었으면 합들을 가지고 인구이동
3. set을 없앤다
4. 1,2,3을 반복
5. 인구이동이 발생하지 않을때 출력
'''
cnt = 0

def BFS(stack):
    global visited
    global flag
    global result
    while stack:
        x,y = stack.pop()
        #상
        if y+1 < n and visited[y+1][x] == 0 :
            if l<=abs(matrix[y+1][x] - matrix[y][x])<=r:
                flag = 1
                visited[y+1][x] = 2
                stack.add((x,y+1))
                result.add((x,y+1))
        #하
        if y-1 >= 0 and visited[y-1][x] == 0 :
            if l<=abs(matrix[y-1][x] - matrix[y][x])<=r:
                flag = 1
                visited[y-1][x] = 2
                stack.add((x,y-1))
                result.add((x,y-1))
        #좌
        if x-1 >=0 and visited[y][x-1] == 0 :
            if l<=abs(matrix[y][x-1] - matrix[y][x])<=r:
                flag = 1
                visited[y][x-1] = 2
                stack.add((x-1,y))
                result.add((x-1,y))
        #우
        if x+1 < n and visited[y][x+1] == 0 :
            if l<=abs(matrix[y][x+1] - matrix[y][x])<=r:
                flag = 1
                visited[y][x+1] = 2
                stack.add((x+1,y))
                result.add((x+1,y))

def change(x,y,result,matrix):
    temp = 0
    for x,y in result:
        temp += matrix[y][x]
    value = int(temp/len(result))
    for x,y in result:
        matrix[y][x] = value
        visited[y][x] = -1

while True:
    visited = [[0]*n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            stack = set()
            result = set()
            if visited[i][j] == 0 :
                visited[i][j] = 1
                result.add((j,i))
                stack.add((j,i))
                BFS(stack)
                if len(result) != 1:
                    change(j,i,result,matrix)   
    if flag == 0:
        break
    else:
        cnt += 1
print(cnt)
            
            




    
