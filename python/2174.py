'''
matrix = A * B
로봇 n개

초기위치 : (x,y)로 나타낸다.
x는 왼쪽에서부터
y는 아래쪽부터

로봇은 맨 처음에 NWES중 하나의 방향을 향해 서있다.
초기에 서있는 로봇들의 위치는 서로 다르다.

m개의 명령
각각의 명령은 순차적으로 실행
하나의 명령을 한 로봇에서 내렸으면, 
그 명령이 완수될 때까지 그 로봇과 다른 모든 로봇에게 명령 내릴 수 없다

명령
L : 로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전
R : 로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전
F : 로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직인다.

잘못된 명령에는 다음의 두 가지가 있을 수 있다
1. Robot X crashes into the wall : X번 로봇이 벽에 충돌하는 경우 -> 벗어나는 경우
2. Robot X crashes into robot Y : X번 로봇이 움직이다가 Y번 로봇에 충돌하는 경우
'''
from collections import defaultdict


a,b = map(int,input().split())
n,m = map(int,input().split())
matrix = [[0]*a for _ in range(b)]

robot = defaultdict(list)

dd = {'E':0, 'N':1, 'W':2, 'S':3}
for num in range(1,n+1):
    x,y,dire = input().split()
    x = int(x)-1
    y = b-int(y)
    matrix[y][x] = num
    robot[num] = [x,y,dd[dire]]

d = {
    0 : [1,0],
    1 : [0,-1],
    2 : [-1,0],
    3 : [0,1]
}

flag = 0
command = []
for _ in range(m):
    num, com, recur = input().split()
    num = int(num)
    recur = int(recur)
    command.append([num,com,recur])

def solution(matrix, robot):
    for num, com, recur in command:
        x,y,dire = robot[num]
        rx, ry = x, y
        if com == 'F':
            for _ in range(recur):
                rx += d[dire][0]
                ry += d[dire][1]
                if rx<0 or rx>=a or ry<0 or ry>=b:
                    print("Robot {} crashes into the wall".format(num))
                    return 
                if matrix[ry][rx] != 0 :
                    print("Robot {} crashes into robot {}".format(num,matrix[ry][rx]))
                    return
            matrix[ry][rx] = num
            matrix[y][x] = 0
        else:
            if com == 'L':
                dire = (dire + recur)%4
            else:
                recur %= 4
                if dire - recur < 0:
                    dire = 4 + dire - recur
                else:
                    dire -= recur
        
        robot[num] = [rx,ry,dire]
    print("OK")
    return

solution(matrix, robot)