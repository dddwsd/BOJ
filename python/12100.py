''''''
'''
이동 : 보드위의 전체블록 상하좌우 중 하나로 이동 -> 끝까지 이동
같은 값을 같는 두 블록이 충돌하면 하나로 합쳐지게 된다
한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 합쳐질 수 없다
합쳐지는 순서는 해당 방향의 제일 끝부터

최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하라
'''
'''
입력
보드의 크기 N*N
합쳐지는 것은 단한번
1. 보드에서 제일 큰 값을 찾는 지점들 (= m_point)를 알아낸다. 
( 2^n에 아무것도 더하지 않아도 2^(n-1)의 어떠한 수를 더하든 최대 같기 때문)
2. m_point에 속하는 모든 점들이 다른 값과 합쳐질때 까지 지상하좌우로 최대 5번 움직인다 
3. 합쳐질 때 합쳐지는 점을 저장한다.
4. m_point = [max_x,max_y,add_x,add_y]순으로 저장된다.
5, 다 저장되었으면 최대 값을 저장한 후 return
'''
from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

def move(direc,matrix):
    if direc == "L" or direc == "U":
        out_ = lambda x: x.popleft()
        in_ = lambda x, y: x.append(y)
    else:
        out_ = lambda x: x.pop()
        in_ = lambda x, y: x.appendleft(y)
    for i in range(n):
        temp, before, add = deque(),0,0
        t_deque = deque(matrix[i])
        while t_deque:
            if  before == 0:
                before = out_(t_deque)
                continue
            if add == 0:
                add = out_(t_deque)
                continue
            if before and add:
                if before == add:
                    in_(temp,before+add)
                    before, add = 0,0
                else:
                    in_(temp,before)
                    before = add
                    add = 0
        if before != 0 or add != 0:
            if before == add :
                in_(temp,before+add)
            else:
                if before != 0:
                    in_(temp,before)
                if add != 0:
                    in_(temp,add)
        length = n-len(temp)
        for _ in range(length):
            in_(temp,0)
        matrix[i] = list(temp)

def find(matrix,count,result):
    for direc in ["L","R","U","D"]:
        t_matrix = deepcopy(matrix)
        if direc == "L" or direc == "R":
            move(direc,t_matrix)
        elif direc == "U" or direc == "D":
            t_matrix = [list(t) for t in zip(*t_matrix)]
            move(direc,t_matrix)
            t_matrix = [list(t) for t in zip(*t_matrix)]
        if count+1 == 5:
            for i in range(n):
                    result[0] = max(result[0],max(t_matrix[i]))
        else:
            find(deepcopy(t_matrix),count+1,result)

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
result = [0]
find(matrix,0,result)
print(result[0])

