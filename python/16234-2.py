'''
인구이동 최선의 속도
인구이동이 일어나는 점을 모두 찾음
점들에서 dfs시작
dfs를 통해 얻은 결과 list를 list에 저장
'''
n,l,r = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

def find_point(matrix):
    global point
    for i in range(n):
        for j in range(n):
            if i == n-1 and j == n-1:
                continue
            elif i == n-1:
                sub = abs(matrix[i][j] - matrix[i][j+1])
                if l<= sub <= r :
                    point.add((j,i))
                    point.add((j+1,i))    
            elif j == n-1:    
                sub = abs(matrix[i][j] - matrix[i+1][j])
                if l<= sub <= r :
                    point.add((j,i))
                    point.add((j,i+1))
            else :
                sub = abs(matrix[i][j] - matrix[i+1][j])
                if l<= sub <= r :
                    point.add((j,i))
                    point.add((j,i+1))
                sub = abs(matrix[i][j] - matrix[i][j+1])
                if l<= sub <= r :
                    point.add((j,i))
                    point.add((j+1,i))         

def find(x,y):
    global visited
    stack = set([(x,y)])
    result = set([(x,y)])
    while stack:
        t_x,t_y = stack.pop()
        visited[t_y][t_x] = 1
        # 상
        if (t_x,t_y+1) in point and visited[t_y+1][t_x] == 0  :
            if l<= abs(matrix[t_y][t_x] - matrix[t_y+1][t_x]) <= r:
                result.add((t_x,t_y+1))
                stack.add((t_x,t_y+1))
        # 하
        if (t_x,t_y-1) in point and visited[t_y-1][t_x] == 0 :
            if l<= abs(matrix[t_y][t_x] - matrix[t_y-1][t_x]) <= r:
                result.add((t_x,t_y-1))
                stack.add((t_x,t_y-1))
        # 좌
        if (t_x-1,t_y) in point and visited[t_y][t_x-1] == 0 :
            if l<= abs(matrix[t_y][t_x] - matrix[t_y][t_x-1]) <= r:
                result.add((t_x-1,t_y))
                stack.add((t_x-1,t_y))
        # 우
        if (t_x+1,t_y) in point and visited[t_y][t_x+1] == 0 :
            if l<= abs(matrix[t_y][t_x] - matrix[t_y][t_x+1]) <= r:
                result.add((t_x+1,t_y))
                stack.add((t_x+1,t_y))
    return result

cnt = 0
while True:
    point = set()
    find_point(matrix)
    if len(point) == 0:
        break
    cnt += 1
    t_area = []
    sep_area = []
    visited = [[0]*n for _ in range(n)]
    for (x,y) in point:
        if (x,y) not in t_area:
            area = find(x,y)
            t_area.extend(area)
            sep_area.append(area)
    for area in sep_area:
        value = 0
        for x,y, in area:
            value += matrix[y][x]
        value = int(value/len(area))
        for x,y in area:
            matrix[y][x] = value
print(cnt)
    

