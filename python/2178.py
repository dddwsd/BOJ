# N * M 배열
# 1 : 이동할 수 있는 칸 / 0 : 이동할 수 없는 칸
# (1,1) -> (N,M) 최소칸수
# 서로 인접한 칸으로만 이동할 수 있다
# 칸 셀때는 시작 위치 + 도착위치 포함

# 입력
# 첫째줄 N,M 2~100
# 다음N개줄 M개의 정수 미로로 주어진다
# 각각의 수들은 붙어서 입력으로 주어진다

# 출력
# 최소칸수 / 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다

n,m = map(int,input().split())
matrix = [[] for _ in range(n)]
for i in range(n):
    temp = input()
    for j in range(m):
        matrix[i].append(int(temp[j]))
visited = [[0 for _ in range(m)] for _ in range(n)]
result = []
result.append([0,0])
n = n - 1
m = m - 1
cnt = 1

def find():
    global cnt
    global visited
    global result
    while True:
        result2 = []
        cnt+=1
        for x,y in result:
            #상
            if y+1 <= n and visited[y+1][x] == 0 and matrix[y+1][x] == 1:
                if x == m and y+1 == n:
                    print(cnt)
                    return
                visited[y+1][x] =1
                result2.append([x,y+1])
            #하
            if y-1 >= 0 and visited[y-1][x] == 0 and matrix[y-1][x] == 1:
                if x == m and y-1 == n:
                    print(cnt)
                    return
                visited[y-1][x] = 1
                result2.append([x,y-1])
            #좌
            if x-1 >= 0 and visited[y][x-1] == 0 and matrix[y][x-1] == 1:
                if x-1 == m and y == n:
                    print(cnt)
                    return
                visited[y][x-1] = 1
                result2.append([x-1,y])
            #우
            if x+1 <= m and visited[y][x+1] == 0 and matrix[y][x+1] == 1:
                if x+1 == m and y == n :
                    print(cnt)
                    return
                visited[y][x+1] =1
                result2.append([x+1,y])
        result = result2


find()
