'''
n * n 지도 각 칸에는 높이
지나갈 수 있는 길이 몇개인지?
길 -> 한행 또는 한열 전부를 나타내며 한쪽끝에서 다른쪽 끝으로 가는것
길이 총 2n개

길을 지나갈 수 있으려면 모든 칸의 높이가 같아야한다.
or
경사로를 놓아서 지나갈 수 있다.
경사로 높이 항상 1 길이 L

* 놓을 수 있는 경우
경사로는 낮은 칸에 놓이며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다
낮은 칸과 높은 칸의 높이차이는 1이어야 한다
경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고 L개의 칸이 있어야 한다.

* 놓을 수 없는 경우
경사로를 놓은 곳에 또 경사로 놓는 경우
높이차이가 1이 아닌경우
낮은 칸의 높이가 모두 같지 않거나 L개가 연속되지 않는 경우
경사로를 놓다가 범위 법어나는 경우
'''

n,l = map(int,input().split())
matrix=  [list(map(int,input().split())) for _ in range(n)]
visited_x = [[0]*n for _ in range(n)]
visited_y = [[0]*n for _ in range(n)]

'''
가로로 놓는 경사로와 세로로 놓는 경사로는 상관이 없다.
체크를 2회 진행
1. 내려가는 길
2. 올라가는 길
-> 올라가는 길을 만들어야 하는 곳에 이미 경사로가 있다면 fail
'''

def make_road(t_matrix,flag,visited,start,end,fix):
    if flag == 'x':
        for i in range(start,end):
            if t_matrix[fix][i] != t_matrix[fix][i+1]:
                return -1
            if visited[fix][i] == 1:
                return -1
        if visited[fix][end] == 1:
            return -1
        for i in range(start,end+1):
            visited[fix][i] = 1
    else:
        for i in range(start,end):
            if t_matrix[i][fix] != t_matrix[i+1][fix]:
                return -1
            if visited[i][fix] == 1:
                return -1
        if visited[end][fix] == 1:
            return -1
        for i in range(start,end+1):
            visited[i][fix] = 1


    


#가로
def find_horizontal(matrix):
    
    cnt = 0
    for i in range(n):
        flag = 0
        for j in range(1,n):
            if matrix[i][j-1] - matrix[i][j] == 0:
                continue
            elif matrix[i][j-1] - matrix[i][j] == 1:
                if j+l-1 >= n:
                    flag =1
                    break
                if make_road(matrix,'x',visited_x,j,j+l-1,i) == -1:
                    flag = 1
                    break
            elif matrix[i][j-1] - matrix[i][j] == -1:
                if j-l < 0:
                    flag = 1
                    break
                if make_road(matrix,'x',visited_x,j-l,j-1,i) == -1:
                    flag = 1
                    break
            else:
                flag = 1
                break
        if j == n-1 and flag == 0:
            cnt += 1
    return cnt

#가로
def find_vertical(matrix):
    cnt = 0
    for i in range(n):
        flag = 0
        for j in range(1,n):
            if matrix[j-1][i] - matrix[j][i] == 0:
                continue
            elif matrix[j-1][i] - matrix[j][i] == 1:
                if j+l-1 >= n:
                    flag = 1
                    break
                if make_road(matrix,'y',visited_y,j,j+l-1,i) == -1:
                    flag = 1
                    break
            elif matrix[j-1][i] - matrix[j][i] == -1:
                if j-l < 0:
                    flag = 1
                    break
                if make_road(matrix,'y',visited_y,j-l,j-1,i) == -1:
                    flag = 1
                    break
            else:
                flag = 1
                break
        if j == n-1 and flag == 0:
            cnt += 1
    return cnt
        

cnt = find_horizontal(matrix)
cnt += find_vertical(matrix)
print(cnt)


