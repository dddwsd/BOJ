'''
n*n 크기의 공간
물고기 M / 아기상어 1마리 -> 크기를 갖고 있음
한칸 물고기 최대 1
아기상어 처음 크기 2 -> 1초후 상하좌우 이동
아기상어는 자신보다 큰 물고기가 있는 칸 x / 나머지 칸 o
아기상어는 자신의 크기보다 작은 물고기만 먹을 수 있다 
즉. 크기가 같은 물고기는 못먹지만 지나갈 수 있다

이동하는 방법
1. 먹을 물고기 x -> 엄마상어에게 도움요청
2. 먹을 물고기 1마리 -> 먹으러감
3. 먹을 물고리 여러마리 -> 거리가 가장 가까운 물고기
3-1. 지나야 하는 칸의 개수 최소값
3-2. 거리가 가까운 물고기가 많다면 -> 가장위의 물고기
3-3. 그러한 물고기가 여러마리 라면 -> 가장왼쪽

물고기 먹으면 빈칸
아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기 1증가
몇초동안 도움을 청하지 않는가

0 빈칸
1 ~ 6 : 물고기
9 : 아기상어

'''
from copy import deepcopy
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
l_matrix = [[0]*n for _ in range(n)]
fish = set()
able_eat = set()
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            x,y = j,i
        if 1<= matrix[i][j] <= 6:
            fish.add((j,i,matrix[i][j]))
            if matrix[i][j] >2:
                l_matrix[i][j] = -2
            elif matrix[i][j] < 2:
                able_eat.add((j,i,matrix[i][j]))
dist = 0
s_size = 2
eat = 0
def remove_eating(l_matrix,s_size,able_eat):   
    # 먹은 거를 없애주는 함수 & 먹을 것 추가해주는 함수
    for x,y,size in fish:
        if size <= s_size:
            if size < s_size :
                able_eat.add((x,y,matrix[y][x]))
            l_matrix[y][x] = 0
    
def update_length(x,y,l_matrix,flag):
    global able_eat
    stack = [(x,y,0)]
    t_matrix = deepcopy(l_matrix)
    t_matrix[y][x] = -1
    while stack:
        #상
        x,y,cnt = stack.pop()
        if y+1 < n and (t_matrix[y+1][x] == 0 or t_matrix[y+1][x] > cnt+1):
            t_matrix[y+1][x] = cnt+1
            stack.append((x,y+1,cnt+1))
        #하
        if y-1 >= 0 and (t_matrix[y-1][x] == 0 or t_matrix[y-1][x] > cnt+1):
            t_matrix[y-1][x] = cnt+1
            stack.append((x,y-1,cnt+1))
        #좌
        if x-1 >= 0 and (t_matrix[y][x-1] == 0 or t_matrix[y][x-1] > cnt +1):
            t_matrix[y][x-1] = cnt+1
            stack.append((x-1,y,cnt+1))
        #우
        if x+1 < n and (t_matrix[y][x+1] == 0 or t_matrix[y][x+1]>cnt +1):
            t_matrix[y][x+1] = cnt+1
            stack.append((x+1,y,cnt+1))
    if flag == 1:
        remove = set()
        for x1,y1,size1 in able_eat:
            if t_matrix[y1][x1] == 0 :
                remove.add((x1,y1,size1))
        for x1,y1,size1 in remove:
            able_eat -= set([(x1,y1,size1)])

    return t_matrix

t_matrix = update_length(x,y,l_matrix,1)

def find_min():
    global dist,x,y,fish,eat,s_size,able_eat,t_matrix
    if not able_eat:
        return False
    length = n*n
    r_x,r_y = x,y
    for t_x,t_y,size in able_eat:
        temp = t_matrix[t_y][t_x]
        if temp < length:
            length,f_size,r_x,r_y = temp,size,t_x,t_y
        elif temp == length:
            if r_y == t_y and t_x < r_x:
                r_x,f_size = t_x,size
            elif t_y < r_y:
                r_y,r_x,f_size = t_y,t_x,size
    if r_x == x and r_y == y:
        return
    dist += length
    matrix[r_y][r_x] = 9
    matrix[y][x] = 0
    y,x = r_y,r_x
    fish -= set([(r_x,r_y,f_size)])
    able_eat -= set([(r_x,r_y,f_size)])
    eat += 1
    if eat == s_size:
        s_size += 1
        eat = 0
        remove_eating(l_matrix,s_size,able_eat)
        t_matrix = update_length(x,y,l_matrix,1)
    else:
        t_matrix = update_length(x,y,l_matrix,0)

while True:
    # 가장 거리가 가까운 것을 찾아서 fish에서 제거하고 위치를 기억.
    
    if find_min() == False:
        break
    
print(dist)



