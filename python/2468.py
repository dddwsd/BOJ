# 지역 높이정보 파악
# 많은 빅 ㅏ내렸을 때 물에 잠기지 않는 안전한 영역 최대 몇개
# 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠김
# N*N 행렬
# 물에 잠기지 않은 안전한 영역 
# -> 물에 잠기지 않은 지점들이 상하좌우 인접 그 크기가 최대인 영역
# -> 즉 고립된 영역이 몇개인가를 알아내야함

# 장마철에 물에 잠기지 않는 안전한 영역의 최대개수를 계산
from copy import deepcopy
flag = 0
def sub_matrix(sub_matrix,sub_visited):
    global flag
    for i in range(n):
        for j in range(n):
            sub_matrix[i][j] -= 1
            if sub_matrix[i][j] <= 0:
                sub_visited[i][j] = 0
                flag = 1

def BFS(t_visited,x,y,cnt):
    stack = set([(x,y)])
    
    while stack:
        x,y = stack.pop()
        #상
        if y+1 < n and t_visited[y+1][x] == -1:
            t_visited[y+1][x] = cnt
            stack.add((x,y+1))
        #하
        if y-1 >= 0 and t_visited[y-1][x] == -1:
            t_visited[y-1][x] = cnt
            stack.add((x,y-1))
        #좌
        if x-1 >= 0 and t_visited[y][x-1] == -1:
            t_visited[y][x-1] = cnt
            stack.add((x-1,y))
        #우
        if x+1 < n and t_visited[y][x+1] == -1:
            t_visited[y][x+1] = cnt
            stack.add((x+1,y))

def find_area(t_visited):
    cnt = 0
    if flag == 1:
        for i in range(n):
            while True:
                if -1 in iter(t_visited[i]) :
                    cnt += 1
                    index = t_visited[i].index(-1)
                    t_visited[i][index] = cnt
                    BFS(t_visited,index,i,cnt)
                else:
                    break
    return cnt

            

n = int(input())
# 비가 오지 않는 경우부터
# 비가 제일 많이 오는 경우 -1 까지
# 포문 돌면서 
matrix = []
max_len = 0
for _ in range(n):
    list1 = list(map(int,input().split()))
    max_len = max(max(list1),max_len)
    matrix.append(list1)
max_area = 1
visited = [[-1]*n for _ in range(n)]
for i in range(1,max_len):
    # i가 증가할때 마다 1층 감소
    sub_matrix(matrix,visited)
    # value가 0인 모든 지점 잡아놓음
    # 더이상 퍼질 수 없을 때 value가 0인 지점 있는 지확인
    temp_area = find_area(deepcopy(visited))
    max_area = max(temp_area,max_area)
print(max_area)

    
    


