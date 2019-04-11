# M H N
# n m h


def down():
    wrong_count = 0
    for col in range(M):
        c = col
        for r in range(N):
            if N-r < abs(c-col):
                break
            if graph[r][c] == 1:
                c += 1
            elif c > 0 and graph[r][c - 1] == 1:
                c -= 1
        if c != col:
            wrong_count += 1
    return wrong_count

def dfs(put, r_, c_):
    global min_val
    if put > 3:
        return
    wrong_count = down()
    if wrong_count == 0:
        min_val = min(put, min_val)
        return
    if put == 3:
        return
    if 3 <= wrong_count <= 4 and put >= 2:
        return
    if 5 <= wrong_count <= 6 and put >= 1:
        return
    if wrong_count >= 7:
        return

    for r in range(r_, N):
        if r == r_:
            c__ = c_
        else:
            c__ = 0
        for c in range(c__, M-1):
            if graph[r][c] == 1:
                continue
            if c == 0:
                if graph[r][c+1] == 1:
                    continue
                else:
                    graph[r][c] = 1
                    dfs(put+1, r, c+2)
                    graph[r][c] = 0
            else:
                if graph[r][c-1] == 1 or graph[r][c+1] == 1:
                    continue
                else:
                    graph[r][c] = 1
                    dfs(put+1, r, c+2)
                    graph[r][c] = 0




# f = open('15684.txt','r')
M, H, N = map(int, input().strip().split())
graph = [[0] * M for _ in range(N)]
for _ in range(H):
    a, b = map(int, input().strip().split())
    graph[a - 1][b - 1] = 1

min_val = 999
dfs(0, 0, 0)
print(min_val if min_val <= 3 else -1)