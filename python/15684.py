# N개의 세로선 / M개의 가로선
# 인접한 세로선 사이에 가로선을 놓을 수 있다
# H : 각각의 세로선마다 가로선 놓을 수 있는 위치 개수 
# 초록선은 세로선 / 초록선과 점선이 교차하는 점 -> 가로선을 놓을 수 있는 점
# 가로선은 인접한 두 세로선을 연결해야 한다.
# 단 두 가로선이 연속하거나 서로 접하면 안된다. -> 가로선은 점선 위에 있어야 함


# 사다리 게임 각각의 세로선 마다 게임을 진행
# 세로선의 가장 위에서 부터 아래방향으로 이동해야한다
# 세로선으로 내려가다가 가로선을 만나면 아래방향으로 이동해야 한다
# i번째 세로선의 결과가 번이 나와야 한다. -> 가로선 개수 최솟값

#입력
# N : 세로선 M : 가로선 H : 세로선마다 가로선을 놓을 수 있는 위치의 개수
# M개의 줄에는 가로선의 정보가 한줄에 하나씩 주어진다

from itertools import combinations
from copy import deepcopy

n,m,h = map(int,input().split())
matrix = [[0]*n for _ in range(h)]
for i in range(m):
    a,b = map(int,input().split())
    # b번 세로선과 b+1번 세로선을 a번 점선위치에서 연결하겠다.    
    if b <= n-1:
        matrix[a-1][b-1] = 1
        #matrix[a-1][b] = 2
        # 아래로 가는거 0
        # 오른쪽 가는거 1
        # 왼쪽 가는거 2

point = []
for i in range(h):
    for j in range(n-1):
        if matrix[i][j] == 0 and matrix[i][j+1] == 0 and matrix[i][j-1] != 1:
            point.append([i,j])
        
def check_correct(matrix):
    k = [ i for i in range(n)]
    for i in range(n):
        for j in range(h):
            if h-j < abs(k[i]-i):
                return False
            elif matrix[j][k[i]] == 1:
                k[i] += 1 
            elif matrix[j][k[i]-1] == 1:
                k[i] -= 1 
        if j == h-1 and k[i] != i:
            return False
    return True

if check_correct(matrix) == True:
    print(0)
else:
    # 1 -> 2 -> 3으로 올라갈때마다 중복을 제거하는 법
    flag = 0
    length = len(point)
    if flag == 0 and length >= 1:
        flag = 1
        check1 = list(combinations(point,1))
        for list1 in check1:
            t_matrix = deepcopy(matrix)
            y = list1[0][0] ; x = list1[0][1]
            t_matrix[y][x] = 1
            #t_matrix[y][x+1] = 2
            if check_correct(t_matrix) == True:
                print(1)
                flag = -1
                break
    if flag == 1 and length >= 2:
        flag =2
        check1 = list(combinations(point,2))
        for list1 in check1:
            t_matrix = deepcopy(matrix)
            y_1 = list1[0][0] ; x_1 = list1[0][1]
            y_2 = list1[1][0] ; x_2 = list1[1][1]
            if y_1 == y_2 and x_1+1 == x+2:
                continue
            t_matrix[y_1][x_1] = 1
          #  t_matrix[y_1][x_1+1] = 2
            t_matrix[y_2][x_2] = 1
          #  t_matrix[y_2][x_2+1] = 2
            if check_correct(t_matrix) == True:
                print(2)
                flag = -1
                break
    if flag == 2 and length >= 3:
        flag =3
        check1 = list(combinations(point,3))
        for list1 in check1:
            t_matrix = deepcopy(matrix)
            y_1 = list1[0][0] ; x_1 = list1[0][1]
            y_2 = list1[1][0] ; x_2 = list1[1][1]
            y_3 = list1[2][0] ; x_3 = list1[2][1]
            if y_1 == y_2 and x_1+1 == x_2:
                continue
            if y_2 == y_3 and x_2+1 == x_3:
                continue
            if y_1 == y_3 and x_1+1 == x_3:
                continue
            t_matrix[y_1][x_1] = 1
       #     t_matrix[y_1][x_1+1] = 2
            t_matrix[y_2][x_2] = 1
        #    t_matrix[y_2][x_2+1] = 2
            t_matrix[y_3][x_3] = 1
        #   t_matrix[y_3][x_3+1] = 2
            if check_correct(t_matrix) == True:
                print(3)
                flag = -1
                break
    if flag != -1:
        print(-1)
