# startlink사무실 N*M크기의 직사각형
from copy import deepcopy

n,m = map(int,input().split())
cctv1 = [] ;cctv2 = [] ;cctv3 = [] ;cctv4 = [] ;cctv5 = [] ;wall6 = []
matrix = [[] for _ in range(n)]
list1 = []
for i in range(n):
    list1 = list(map(int,input().split()))
    matrix[i] = list1
    for j in range(m):
        if list1[j] == 1:
            cctv1.append([i,j])
        elif list1[j] == 2:
            cctv2.append([i,j])
        elif list1[j] == 3:
            cctv3.append([i,j])
        elif list1[j] == 4:
            cctv4.append([i,j])
        elif list1[j] == 5:
            cctv5.append([i,j])
        '''
        elif list1[j] == 6:
            wall6.append([i,j])
        '''
#len6 = len(wall6)

# cctv는 감시할 수 있는 방향 칸 전체 감시가능
# cctv는 벽을 통과할 수 없다
# cctv가 감시할 수 없는 영역 사각지대

# cctv회전 가능 / 항상 90도 감시방향이 가로 or 세로
# 1번 : 4방향 / 2번 : 2방향 / 3번 : 4방향 / 4번 : 4방향 / 5번 : 1 방향
# cctv는 통과 가능
# 첫째 줄에 사각 지대의 최소 크기를 출력

# 해결방법
# 우선 5번 cctv를 찾아서 모두 감시상태(-1)로 바꾼다
# 다른 cctv들은 경우의 수 별로 구해서 제일 작은 수 구한다.
# n : 세로 / m : 가로 / 7은 감시 영역
# cctv 5
def print_list(matrix):
    for i in range(n):
        print(matrix[i])

def count_zero(t_matrix):
    total = 0
    for i in range(n):
        total += t_matrix[i].count(0)
    return total

def down(matrix,x,y):
    for a in range(y+1,n):
        if matrix[a][x] == 6:
            break
        if matrix[a][x] == 0:
            matrix[a][x] = 7

def up(matrix,x,y):
    for a in range(y-1,-1,-1):
        if matrix[a][x] == 6:
            break
        if matrix[a][x] == 0:
            matrix[a][x] = 7

def right(matrix,x,y):
     for a in range(x+1,m):
        if matrix[y][a] == 6:
            break
        if matrix[y][a] == 0:
            matrix[y][a] = 7


def left(matrix,x,y):
    for a in range(x-1,-1,-1):
        if matrix[y][a] == 6:
            break
        if matrix[y][a] == 0:
            matrix[y][a] = 7
    
result = n*m

if cctv5 != []:
    for y,x in cctv5:
        up(matrix,x,y)
        down(matrix,x,y)
        left(matrix,x,y)
        right(matrix,x,y)
    result = count_zero(matrix)

# 총 K개의 cctv설치 -> 5가지 종류
# 1번 우
# 2번 좌우
# 3번 상우
# 4번 상좌우
# 5번 상하좌우
# 6번 벽
len1 = len(cctv1)
len2 = len(cctv2)
len3 = len(cctv3)
len4 = len(cctv4)

def find(t_matrix,flag,index):
    global result
    if flag == 1:
        if index == len1 :
            find(t_matrix,flag+1,0)
        else :
            y = cctv1[index][0] ; x = cctv1[index][1]
            #상
            temp = deepcopy(t_matrix)
            up(temp,x,y)
            find(temp,flag,index+1)
            #하
            temp = deepcopy(t_matrix)
            down(temp,x,y)
            find(temp,flag,index+1)
            #좌
            temp = deepcopy(t_matrix)
            left(temp,x,y)
            find(temp,flag,index+1)
            #우
            temp = deepcopy(t_matrix)
            right(temp,x,y)
            find(temp,flag,index+1)       
    elif flag == 2:
        if index == len2:
            find(t_matrix,flag+1,0)
        else:
            y = cctv2[index][0] ; x = cctv2[index][1]
            # 좌우
            temp = deepcopy(t_matrix)
            left(temp,x,y)
            right(temp,x,y)
            find(temp,flag,index+1)
            # 상하
            temp = deepcopy(t_matrix)
            up(temp,x,y)
            down(temp,x,y)
            find(temp,flag,index+1)
    elif flag == 3:
        if index == len3:
            find(t_matrix,flag+1,0)
        else:
            y = cctv3[index][0] ; x = cctv3[index][1]
            # 상우
            temp = deepcopy(t_matrix)
            up(temp,x,y)
            right(temp,x,y)
            find(temp,flag,index+1)
            # 상좌
            temp = deepcopy(t_matrix)
            up(temp,x,y)
            left(temp,x,y)
            find(temp,flag,index+1)
            # 하좌
            temp = deepcopy(t_matrix)
            down(temp,x,y)
            left(temp,x,y)
            find(temp,flag,index+1)
            # 하우
            temp = deepcopy(t_matrix)
            down(temp,x,y)
            right(temp,x,y)
            find(temp,flag,index+1)
    elif flag == 4:
        if index == len4:
            result = min(result,count_zero(t_matrix))
            return
        else:
            y = cctv4[index][0] ; x = cctv4[index][1]
            # 상좌우
            temp = deepcopy(t_matrix)
            up(temp,x,y)
            left(temp,x,y)
            right(temp,x,y)
            find(temp,flag,index+1)
            # 상하좌
            temp = deepcopy(t_matrix)
            up(temp,x,y)
            left(temp,x,y)
            down(temp,x,y)
            find(temp,flag,index+1)
            # 하좌우
            temp = deepcopy(t_matrix)
            down(temp,x,y)
            left(temp,x,y)
            right(temp,x,y)
            find(temp,flag,index+1)
            # 상하우
            temp = deepcopy(t_matrix)
            up(temp,x,y)
            down(temp,x,y)
            right(temp,x,y)
            find(temp,flag,index+1)
        
find(matrix,1,0)
print(result)

