from sys import stdin
r = stdin.readline

R, C = map(int, r().strip().split())
board = [list(r().strip()) for _ in range(R)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

stack = list([(0,0,board[0][0])])
maxlen = 1
while stack :
    r, c, alp = stack.pop()
    maxlen = max(maxlen, len(alp))
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in alp :
            stack.append((nr, nc, alp + board[nr][nc]))
            
print(maxlen)