import sys 
a,b = map(int,input().split())
#M=[list(map(lambda x: ord(x)-65,input())) for i in range(a)]
board = []
for i in range(0,a):
    board.append(sys.stdin.readline().rstrip())

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

stack = set([(0,0,board[0][0])])
maxlen = 1
while stack :
    r, c, alp = stack.pop()
    maxlen = max(maxlen, len(alp))
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < a and 0 <= nc < b and board[nr][nc] not in alp :
            stack.add((nr, nc, alp + board[nr][nc]))

print(maxlen) 