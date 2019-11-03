from pprint import pprint
from copy import deepcopy

def check(matrix,paper,row,col):
    result = []
    for size in range(5,0,-1):
        flag = 0
        if paper[size-1] == 0 or (row+size > 10 or col+size > 10):
            continue
        for i in range(row,row+size):
            for j in range(col,col+size):
                if matrix[i][j] == 0 :
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
          result.append(size)
    return result  

def remove(matrix,paper,row,col,size,val):
    paper[size-1] -= 1
    for i in range(row,row+size):
        for j in range(col,col+size):
            matrix[i][j] = 0

def simulation(matrix,paper,row,col,val,count,s):
    if val[0] > 0 and count >= val[0]:
        return
    for i in range(row,10):
        for j in range(col,10):
            if matrix[i][j] == 1:
                break
        if matrix[i][j] == 1:
            break

    if matrix[i][j] == 1:
        size = check(matrix,paper,i,j)
        if size:
            one2zero = []
            for k in size:
                if s-(k*k) == 0:
                    if val[0] == -1 or count+1 < val[0]:
                        val[0] = count+1
                        continue
                for next_y in range(i,i+k):
                    for next_x in range(j,j+k):
                        matrix[next_y][next_x] = 0 # 1에서 0 으로 바꾸고
                        one2zero.append((next_y,next_x)) # 좌표를 저장
                paper[k-1] -= 1
                simulation(matrix,paper,i,0,val,count+1,s-(k*k))
                paper[k-1] += 1
                for y_x in one2zero:
                    matrix[y_x[0]][y_x[1]] = 1

matrix = [list(map(int,input().split())) for _ in range(10)]
paper = [5 for _ in range(5)]
val = [-1]
rest = 0
for i in range(10):
    for j in range(10):
        if matrix[i][j] == 1:
            rest += 1
if rest == 0 :
    print(0)
else:
    simulation(matrix,paper,0,0,val,0,rest)
    print(val[0])
