'''
치즈 n x m 
n : 세로 
m : 가로

치즈 냉동보관 -> 실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다.

각 치즈 격자의 4변중에서 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 1시간만에 녹는다.

치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정한다.

모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정
주어진 치즈가 모두 녹아 없어지는데 걸리는 시간
'''

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

air = set([(0,0)])
d = [[-1,0],[1,0],[0,-1],[0,1]]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
def bfs(air,points,visited):
    adj_che = set([])
    while True:
        temp = set([])
        while points:
            x,y = points.pop()
            for dx,dy in d:
                rx,ry = x+dx, y+dy
                if 0<=rx<m and 0<=ry<n and visited[ry][rx] == 0:
                    if matrix[ry][rx] == 0:
                        temp.add((rx,ry))
                        visited[ry][rx] = 1
                        air.add((rx,ry))
                    else:
                        adj_che.add((rx,ry))
                        
        if not temp:
            return adj_che
        points = temp.copy()

bc = bfs(air,set([(0,0)]),visited)

'''
1. 공기에 속하는 부분을 구한다
2. cheese를 돌면서 공기에 속하는 부분이 2개 이상 접하는지 구한다 
3. 녹는 치즈에서 bfs하면서 공기에 추가
4. 2부터 다시 반복

'''

def solution(matrix,bc,air,visited):
    cnt = 0
    while True:
        temp = set()
        for x,y in bc:
            adj = 0
            for dx,dy in d:
                rx,ry = x+dx, y+dy
                if (rx,ry) in air:
                    adj += 1
            if adj >=2:
                matrix[y][x] = 0
                visited[y][x] = 1
                
                temp.add((x,y)) 
        air |= temp
        bc -= temp
        bc = bc | bfs(air,temp,visited)
        cnt += 1
        if not bc:
            return cnt


print(solution(matrix,bc,air,visited))
