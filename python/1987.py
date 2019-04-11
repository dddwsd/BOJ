def move(x,y):
    global result
    w_list.append(M[x][y])
    
    if x-1 >= 0 and (M[x-1][y] not in w_list):
        move(x-1,y)

    if (x+1 < a) and (M[x+1][y] not in w_list):
        move(x+1,y)

    if (y-1 >= 0) and (M[x][y-1] not in w_list):
        move(x,y-1)

    if (y+1 < b) and (M[x][y+1] not in w_list):
        move(x,y+1)

    if result < len(w_list):
        result = len(w_list)
    w_list.remove(M[x][y])

a,b = map(int,input().split())
M=[list(map(lambda x: ord(x)-65,input())) for i in range(a)]
result = 0
w_list = []
move(0,0)
print(result)