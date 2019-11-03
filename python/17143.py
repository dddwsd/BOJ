''''''
'''
격자판 : RxC
r : 행 / c : 열
상어 : 크기와 속도 갖고 있다

낚시왕이 잡은 상어 크기의 합

낚시왕 처음 위치 -1,0
1초 동안 일어나는 일
1. x+1 (오른쪽으로 한칸 이동)
2. 해당 col애서 가장 가까운 상어 잡는다 -> 격자판에서 상어 사라짐
3. 상어 이동

낚시왕의 위치가 c에 도달하면 멈춘다
상어는 주어진 속도로 이동 -> 속도의 단위 : 칸 / 초
상어가 이동하려고 하는 칸이 격자판의 경계인 경우에는 방향을 반대로 바꿔서 이동

상어가 이동을 마친 후 한칸에 상어 2마리 이상 있을 수 있다
-> 이떄 크기가 가장 큰 상어가 나머지 상어를 모두 잡아 먹는다

row col m : row col 상어수
m개의 줄 : 상어의 정보 -> r,c,s,d,z 
1. (c,r) : 상어의 위치
2. s : 속력
3. d : 이동 방향 -> 1 : 위 / 2 : 아래 / 3 : 오른 / 4 : 왼
4. z : 크기

자기 자신으로 돌아오는 횟수
2*(c-1) / 2*(r-1)이면 자신의 위치로 돌아옴
나머지만큼 이동한 후 저장
1 : 위   
t_s = (r-y+s)%(2*r-1)
t_s // r
== 0 : d = 1 / r-t_s 
== 1 : d = 2 / t_s - r + 2

4 : 왼
t_s = (c-x+s)%(2*c-1) 
t_s // c
== 0 : d = 4 & c - t_s
== 1 : d = 3 & t_s - c + 2
          
2 : 아래
t_s = (y-1+s) % (2*r-1) 
t_s // r
== 0 : d = 2 / 1 + t_s
== 1 : d = 1 / 2r - t_s -1

 
3 : 오른
t_s = (x-1+s) % (2*c-1)
t_s // c
== 0 : d = 3 & 1 + t_s
== 1 : d = 4 & 2c - t_s - 1
'''
from collections import deque
dxy = [[],[0,-1],[0,1],[1,0],[-1,0]]
def move(r_x,r_y):
    global shark
    global matrix
    length = len(shark)
    shark = deque(sorted(shark,key = lambda x : x[4],reverse = True))
    for _ in range(length):
        x,y,s,d,z = shark.popleft()
        if x == r_x and y == r_y:
            continue
        if matrix[y][x] == z:
            matrix[y][x] = 0
        if d == 1:
            t_s = (r-y+s) % (2*(r - 1))
            flag = t_s//r
            if flag == 0:
                y = r-t_s
            else:
                d = 2
                y = t_s-r+2
        elif d == 4 :
            t_s = (c-x+s) %(2*(c-1))
            flag = t_s // c
            if flag == 0:
                x = c-t_s
            else:
                d = 3
                x = t_s-c+2
        elif d == 2 :
            t_s = (y-1+s) % (2 * (r - 1))
            flag = t_s // r
            if flag == 0:
                y = 1+t_s
            else:
                d = 1
                y = 2*r-t_s-1
        elif d == 3:
            t_s = (x-1+s) % (2*(c-1))
            flag = t_s//c
            if flag == 0:
                x = 1+t_s
            else:
                d = 4
                x = 2*c-t_s-1
        if matrix[y][x] < z:
            matrix[y][x] = z
            shark.append([x,y,s,d,z])

def solution():
    global shark
    global matrix
    result = 0
    for x in range(1,c+1):
        r_x,r_y = 0,0
        for y in range(1,r+1):
            if matrix[y][x] > 0:
                result += matrix[y][x]
                r_x,r_y = x,y
                matrix[y][x] = 0
                break
        move(r_x,r_y)
    print(result)

r,c,m = map(int,input().split())
if m == 0:
    print(0)
else:
    shark = deque()
    matrix = [[0] * (c+1) for _ in range(r+1)]
    for _ in range(m):
        temp = list(map(int,input().split()))
        temp[0],temp[1] = temp[1],temp[0]
        shark.append(temp)
        matrix[temp[1]][temp[0]] = temp[4]
    solution()