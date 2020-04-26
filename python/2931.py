from collections import defaultdict

r,c = map(int,input().split())
matrix = [list(input()) for _ in range(r)]
for y in range(r):
    for x in range(c):
        if matrix[y][x] == 'M':
            mx,my = x,y
        elif matrix[y][x] == 'Z':
            zx,zy = x,y

def find_direc(x,y,rx,ry,pl):
    if pl == '|':
        if ry-y == 1:
            return 'd'
        elif ry-y == -1 :
            return 'u'
    elif pl == '-':
        if rx-x == 1:
            return 'r'
        elif rx-x == -1:
            return 'l'
    elif pl == '+':
        if rx-x == 1:
            return 'r'
        elif rx-x == -1:
            return 'l'
        elif ry-y == 1:
            return 'd'
        elif ry-y == -1:
            return 'u'
    elif pl == '1':
        if rx-x == -1:
            return 'd'
        elif ry-y == -1:
            return 'r'
    elif pl == '2':
        if rx-x == -1:
            return 'u'
        elif ry-y == 1:
            return 'r'
    elif pl == '3':
        if rx-x == 1:
            return 'u'
        elif ry-y == 1:
            return 'l'
    elif pl == '4':
        if rx-x == 1:
            return 'd'
        elif ry-y == -1:
            return 'l'
    return 'x'

def move(x,y,dire):
    if dire == 'l':
        return x-1,y
    elif dire == 'r':
        return x+1,y
    elif dire == 'u':
        return x,y-1
    elif dire == 'd':
        return x,y+1

d = [[-1,0],[1,0],[0,-1],[0,1]]    
def moving(x,y):
    # find starting block
    for dx,dy in d:
        rx,ry = x+dx, y+dy
        if 0<=rx<c and 0<=ry<r and matrix[ry][rx] != '.':
            dire = find_direc(x,y,rx,ry,matrix[ry][rx])
            break
    if dire == 'x':
        return rx,ry,x,y
    x,y = rx,ry
    while True:
        rx,ry = move(x,y,dire)
        if matrix[ry][rx] == '.':
            return rx,ry,x,y
        rd = find_direc(x,y,rx,ry,matrix[ry][rx])
        x,y,dire = rx,ry,rd
    

sx,sy,mx,my = moving(mx,my)
sx,sy,zx,zy = moving(zx,zy)

def find_pipe(sx,sy,mx,my,zx,zy):
    for pl in ['|','-','+','1','2','3','4']:
        dire = find_direc(mx,my,sx,sy,pl)
        matrix[sy][sx] = pl
        x,y = sx,sy
        while True:
            if dire == 'x':
                break
            rx,ry = move(x,y,dire)
            if rx == zx and ry == zy:
                return pl
            if rx<0 or rx>=c or ry<0 or ry>=r:
                break
            if matrix[ry][rx] == '.':
                break
            dire = find_direc(x,y,rx,ry,matrix[ry][rx])
            x,y = rx,ry
    return -1
            
print("{} {} {}".format(sy+1,sx+1,find_pipe(sx,sy,mx,my,zx,zy)))