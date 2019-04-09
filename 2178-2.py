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
result = set([(0,0)])
n = n - 1;m = m - 1;cnt = 1

def find():
    global cnt
    global visited
    global result
    while True:
        result2 = set()
        cnt+=1
        for x,y in result:
            #상
            case1 = y+1;case2 = y-1;case3 = x-1;case4 = x+1
            if case1 <= n and visited[case1][x] == 0 and matrix[case1][x] == 1:
                if x == m and case1 == n:
                    print(cnt)
                    return
                visited[case1][x] =1
                result2.add((x,case1))
            #하
            if case2 >= 0 and visited[case2][x] == 0 and matrix[case2][x] == 1:
                if x == m and case2 == n:
                    print(cnt)
                    return
                visited[case2][x] = 1
                result2.add((x,case2))
            #좌
            if case3 >= 0 and visited[y][case3] == 0 and matrix[y][case3] == 1:
                if case3 == m and y == n:
                    print(cnt)
                    return
                visited[y][case3] = 1
                result2.add((case3,y))
            #우
            if case4 <= m and visited[y][case4] == 0 and matrix[y][case4] == 1:
                if case4 == m and y == n :
                    print(cnt)
                    return
                visited[y][case4] =1
                result2.add((case4,y))
        result = result2

find()