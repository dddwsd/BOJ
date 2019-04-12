from itertools import product

def sight(y,x,direct):
    t_x,t_y = x,y
    stack = set()
    while 0<=t_x<m and 0<=t_y<n and matrix[t_y][t_x] != 6:
        stack.add((t_x,t_y))
        t_x += direct[0]
        t_y += direct[1]
        
    return stack

n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
cctv = []
zero = 0

for i in range(n):
    for j in range(m):
        a = matrix[i][j]
        if a == 6:
            continue
        zero += 1
        if a == 0:
            continue
        d = sight(i,j,[0,-1])
        u = sight(i,j,[0,1])
        l = sight(i,j,[-1,0])
        r = sight(i,j,[1,0])
        if a == 1:
            cctv.append([d,u,r,l])
        elif a == 2:
            cctv.append([d|u,r|l])
        elif a == 3:
            cctv.append([u|r, u|l, d|l, d|r])
        elif a == 4:
            cctv.append([u|r|l, u|l|d, l|d|r, d|u|r])
        elif a == 5:
            cctv.append([u|l|r|d])
num = n*m
temp =0
def union(sets):
    res = set()
    for s in sets: res|= s
    return res

for i in product(*cctv):
    num = min(num,zero-len(union(i)))
print(num)
