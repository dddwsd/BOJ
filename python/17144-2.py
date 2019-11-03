d = [[0,1],[0,-1],[-1,0],[1,0]]
def spread(matrix):
    t_matrix = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if matrix[i][j] >= 5:
                dust = matrix[i][j]//5
                for dx,dy in d:
                    nx, ny = j+dx,i+dy
                    if 0<= nx < c and 0<= ny < r and matrix[ny][nx] != -1:
                        t_matrix[ny][nx] += dust
                        matrix[i][j] -= dust
    for i in range(r):
        for j in range(c):
            matrix[i][j] += t_matrix[i][j]

def clean(matrix):
    for i in range(a1y-1,0,-1):
        matrix[i][0] = matrix[i-1][0]
    for i in range(0,c-1):
        matrix[0][i] = matrix[0][i+1]
    for i in range(0,a1y):
        matrix[i][c-1] = matrix[i+1][c-1]
    for i in range(c-1,1,-1):
        matrix[a1y][i] = matrix[a1y][i-1]
    matrix[a1y][1] = 0
    for i in range(a2y+1,r-1):
        matrix[i][0] = matrix[i+1][0]
    for i in range(0,c-1):
        matrix[r-1][i] = matrix[r-1][i+1]
    for i in range(r-1,a2y,-1):
        matrix[i][c-1] = matrix[i-1][c-1]
    for i in range(c-1,1,-1):
        matrix[a2y][i] = matrix[a2y][i-1]
    matrix[a2y][1] = 0

r,c,t = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(r)]
for i in range(r):
    if -1 in matrix[i]:
        a1y, a2y = i,i+1
        break
for _ in range(t):
    spread(matrix)
    clean(matrix)
result = 0
for item in matrix:
    result += sum(item)
print(result+2)