
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
result = [[[0,0,0] for _ in range(n)] for _ in range(n)]

# 가로 0 세로 1 대각선 2
# 시작 0,0  0,1
result[0][1][0] = 1

for i in range(2,n):
    if matrix[0][i]:
        break
    result[0][i][0] = result[0][i-1][0]

for i in range(1,n):
    for j in range(2,n):
        # 대각선
        if matrix[i-1][j] is 0 and matrix[i][j] is 0 and matrix[i][j-1] is 0:
            result[i][j][2] = result[i-1][j-1][0] + result[i-1][j-1][1] + result[i-1][j-1][2]
        # 세로
        if matrix[i][j] is 0 :
            result[i][j][1] = result[i-1][j][1] + result[i-1][j][2]
        #가로
        if matrix[i][j] is 0:
            result[i][j][0] = result[i][j-1][0] + result[i][j-1][2]
        
print(sum(result[n-1][n-1]))


